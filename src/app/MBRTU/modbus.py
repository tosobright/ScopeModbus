# -*- coding: utf-8 -*-
#
# @author: Toso
# @created: 2019-05-01T11:34:15.897Z+08:00
# @comment: ______________
#

import serial
import serial.tools.list_ports
import MBdefines as defines
import struct
import sys
import MBFormat
from PyQt4 import QtCore

PY2 = sys.version_info[0] == 2


class MB(QtCore.QObject):
    MBrecord = QtCore.pyqtSignal(str)

    def ComAutoFind(self):
        self.comboBox_Port = []
        # 先获取所以有USB串口挂载的设备
        self.scomList = list(serial.tools.list_ports.comports())

        if(len(self.scomList) <= 0):
            return self.tr(u"No Port Find")
        else:
            for item in self.scomList:
                self.comboBox_Port.append(item.device)
        return self.comboBox_Port

    def Open(self, DevAddr, Port, Baudrate, Parity, Bytesize, Stopbits, Timeout):
        try:
            self.slaveAddr = DevAddr
            self.serial = serial.Serial(port=Port,
                                        baudrate=Baudrate,
                                        bytesize=Bytesize,
                                        parity=Parity,
                                        stopbits=Stopbits,
                                        xonxoff=0)
            self.serial.timeout = Timeout
            return 0
        except Exception as err:
            raise err

    def Log(self, msg):
        self.MBrecord.emit(msg)

    # 3 0 1 (23,)
    # 3 2 2 (34, 63)

    def read(self, Func, Start, Length):
        try:
            return self.execute(
                self.slaveAddr, Func, Start, Length)
        except Exception as err:
            raise err

    def write(self, Func, Start, val):
        try:
            return self.execute(self.slaveAddr, Func, Start, output_value=val)
        except Exception as err:
            raise err

    def close(self):
        try:
            self.serial.close()
        except:
            pass

    def swap_bytes(self, word_val):
        """swap lsb and msb of a word"""
        msb = (word_val >> 8) & 0xFF
        lsb = word_val & 0xFF
        return (lsb << 8) + msb

    def calculate_crc(self, data):
        """Calculate the CRC16 of a datagram"""
        crc = 0xFFFF
        for i in data:
            if PY2:
                crc = crc ^ ord(i)
            else:
                crc = crc ^ i
            for j in range(8):
                tmp = crc & 1
                crc = crc >> 1
                if tmp:
                    crc = crc ^ 0xA001
        return self.swap_bytes(crc)

    def to_data(self, string_data):
        if PY2:
            return string_data
        else:
            return bytearray(string_data, 'ascii')

    def build_request(self, pdu, slave):
        if (slave < 0) or (slave > 255):
            raise Exception("Invalid address {0}".format(
                slave))
        data = struct.pack(">B", slave) + pdu
        crc = struct.pack(">H", self.calculate_crc(data))
        return data + crc

    def parse_response(self, response, slave):
        if len(response) < 3:
            raise Exception(
                "Response length is invalid {0}".format(len(response)))
        (response_address, ) = struct.unpack(">B", response[0:1])
        if slave != response_address:
            raise Exception(
                "Response address {0} is different from request address {1}".format(
                    response_address, slave
                )
            )
        (crc, ) = struct.unpack(">H", response[-2:])
        if crc != self.calculate_crc(response[:-2]):
            raise Exception("Invalid CRC in response")
        return response[1:-2]

    def execute(self, slave, function_code, starting_address, quantity_of_x=0, output_value=0, data_format="", expected_length=-1):
        pdu = ""
        is_read_function = False
        nb_of_digits = 0

        # Build the modbus pdu and the format of the expected data.
        # It depends of function code. see modbus specifications for details.
        if function_code == defines.READ_COILS or function_code == defines.READ_DISCRETE_INPUTS:
            is_read_function = True
            pdu = struct.pack(">BHH", function_code,
                              starting_address, quantity_of_x)
            byte_count = quantity_of_x // 8
            if (quantity_of_x % 8) > 0:
                byte_count += 1
            nb_of_digits = quantity_of_x
            if not data_format:
                data_format = ">" + (byte_count * "B")
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + bytcodeLen + bytecode + crc1 + crc2
                expected_length = byte_count + 5

        elif function_code == defines.READ_INPUT_REGISTERS or function_code == defines.READ_HOLDING_REGISTERS:
            is_read_function = True
            pdu = struct.pack(">BHH", function_code,
                              starting_address, quantity_of_x)
            if not data_format:
                data_format = ">" + (quantity_of_x * "H")
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + bytcodeLen + bytecode x 2 + crc1 + crc2
                expected_length = 2 * quantity_of_x + 5

        elif (function_code == defines.WRITE_SINGLE_COIL) or (function_code == defines.WRITE_SINGLE_REGISTER):
            if function_code == defines.WRITE_SINGLE_COIL:
                if output_value != 0:
                    output_value = 0xff00
            fmt = ">BH"+("H" if output_value >= 0 else "h")
            pdu = struct.pack(fmt, function_code,
                              starting_address, output_value)
            if not data_format:
                data_format = ">HH"
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + adress1 + adress2 + value1+value2 + crc1 + crc2
                expected_length = 8

        elif function_code == defines.WRITE_MULTIPLE_COILS:
            byte_count = len(output_value) // 8
            if (len(output_value) % 8) > 0:
                byte_count += 1
            pdu = struct.pack(">BHHB", function_code, starting_address, len(
                output_value), byte_count)
            i, byte_value = 0, 0
            for j in output_value:
                if j > 0:
                    byte_value += pow(2, i)
                if i == 7:
                    pdu += struct.pack(">B", byte_value)
                    i, byte_value = 0, 0
                else:
                    i += 1
            if i > 0:
                pdu += struct.pack(">B", byte_value)
            if not data_format:
                data_format = ">HH"
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + adress1 + adress2 + outputQuant1 + outputQuant2 + crc1 + crc2
                expected_length = 8

        elif function_code == defines.WRITE_MULTIPLE_REGISTERS:
            byte_count = 2 * len(output_value)
            pdu = struct.pack(">BHHB", function_code, starting_address, len(
                output_value), byte_count)
            for j in output_value:
                fmt = "H" if j >= 0 else "h"
                pdu += struct.pack(">" + fmt, j)
            if not data_format:
                data_format = ">HH"
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                # slave + func + adress1 + adress2 + outputQuant1 + outputQuant2 + crc1 + crc2
                expected_length = 8

        elif function_code == defines.READ_EXCEPTION_STATUS:
            pdu = struct.pack(">B", function_code)
            data_format = ">B"
            if expected_length < 0:
                # No length was specified and calculated length can be used:
                expected_length = 5

        elif function_code == defines.DIAGNOSTIC:
            # SubFuncCode  are in starting_address
            pdu = struct.pack(">BH", function_code, starting_address)
            if len(output_value) > 0:
                for j in output_value:
                    # copy data in pdu
                    pdu += struct.pack(">B", j)
                if not data_format:
                    data_format = ">" + (len(output_value) * "B")
                if expected_length < 0:
                    # No length was specified and calculated length can be used:
                    # slave + func + SubFunc1 + SubFunc2 + Data + crc1 + crc2
                    expected_length = len(output_value) + 6

        elif function_code == defines.READ_WRITE_MULTIPLE_REGISTERS:
            is_read_function = True
            byte_count = 2 * len(output_value)
            pdu = struct.pack(
                ">BHHHHB",
                function_code, starting_address, quantity_of_x, defines.READ_WRITE_MULTIPLE_REGISTERS,
                len(output_value), byte_count
            )
            for j in output_value:
                fmt = "H" if j >= 0 else "h"
                # copy data in pdu
                pdu += struct.pack(">"+fmt, j)
            if not data_format:
                data_format = ">" + (quantity_of_x * "H")
            if expected_length < 0:
                # No lenght was specified and calculated length can be used:
                # slave + func + bytcodeLen + bytecode x 2 + crc1 + crc2
                expected_length = 2 * quantity_of_x + 5
        else:
            raise Exception(
                "The {0} function code is not supported. ".format(function_code))

        request = self.build_request(pdu, slave)
        #print request
        # self.edt_log.setUpdatesEnabled(False)
        self.Log(MBFormat.currtime() + " Send " + MBFormat.str_to_hex(request))
        self.serial.write(request)

        #######################################################################################################################################

        if slave != 0:
            # receive the data from the slave
            response = self.to_data("")

            while True:
                read_bytes = self.serial.read(
                    expected_length if expected_length > 0 else 1)
                if not read_bytes:
                    break
                response += read_bytes
                if expected_length >= 0 and len(response) >= expected_length:
                    # if the expected number of byte is received consider that the response is done
                    # improve performance by avoiding end-of-response detection by timeout
                    break

            self.Log(MBFormat.currtime() + " Recv " +
                     MBFormat.str_to_hex(response))
            # self.edt_log.setUpdatesEnabled(True)

            # extract the pdu part of the response
            response_pdu = self.parse_response(response, slave)

            # analyze the received data
            (return_code, byte_2) = struct.unpack(">BB", response_pdu[0:2])

            if return_code > 0x80:
                # the slave has returned an error
                exception_code = byte_2
                raise Exception(exception_code)
            else:
                if is_read_function:
                    # get the values returned by the reading function
                    byte_count = byte_2
                    data = response_pdu[2:]
                    if byte_count != len(data):
                        # the byte count in the pdu is invalid
                        raise Exception(
                            "Byte count is {0} while actual number of bytes is {1}. ".format(
                                byte_count, len(data))
                        )
                else:
                    # returns what is returned by the slave after a writing function
                    data = response_pdu[1:]

                # returns the data as a tuple according to the data_format
                # (calculated based on the function or user-defined)
                result = struct.unpack(data_format, data)
                if nb_of_digits > 0:
                    digits = []
                    for byte_val in result:
                        for i in range(8):
                            if len(digits) >= nb_of_digits:
                                break
                            digits.append(byte_val % 2)
                            byte_val = byte_val >> 1
                    result = tuple(digits)
                return result
