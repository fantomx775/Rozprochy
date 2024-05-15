# -*- coding: utf-8 -*-
#
# Copyright (c) ZeroC, Inc. All rights reserved.
#
#
# Ice version 3.7.10
#
# <auto-generated>
#
# Generated from file `Printer.ice'
#
# Warning: do not edit this file.
#
# </auto-generated>
#

from sys import version_info as _version_info_
import Ice, IcePy

# Start of module Demo
_M_Demo = Ice.openModule('Demo')
__name__ = 'Demo'

if 'ValueOutOfRangeException' not in _M_Demo.__dict__:
    _M_Demo.ValueOutOfRangeException = Ice.createTempClass()
    class ValueOutOfRangeException(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Demo::ValueOutOfRangeException'

    _M_Demo._t_ValueOutOfRangeException = IcePy.defineException('::Demo::ValueOutOfRangeException', ValueOutOfRangeException, (), False, None, (('reason', (), IcePy._t_string, False, 0),))
    ValueOutOfRangeException._ice_type = _M_Demo._t_ValueOutOfRangeException

    _M_Demo.ValueOutOfRangeException = ValueOutOfRangeException
    del ValueOutOfRangeException

if 'UnsupportedColorException' not in _M_Demo.__dict__:
    _M_Demo.UnsupportedColorException = Ice.createTempClass()
    class UnsupportedColorException(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Demo::UnsupportedColorException'

    _M_Demo._t_UnsupportedColorException = IcePy.defineException('::Demo::UnsupportedColorException', UnsupportedColorException, (), False, None, (('reason', (), IcePy._t_string, False, 0),))
    UnsupportedColorException._ice_type = _M_Demo._t_UnsupportedColorException

    _M_Demo.UnsupportedColorException = UnsupportedColorException
    del UnsupportedColorException

if 'UnsupportedFragranceException' not in _M_Demo.__dict__:
    _M_Demo.UnsupportedFragranceException = Ice.createTempClass()
    class UnsupportedFragranceException(Ice.UserException):
        def __init__(self, reason=''):
            self.reason = reason

        def __str__(self):
            return IcePy.stringifyException(self)

        __repr__ = __str__

        _ice_id = '::Demo::UnsupportedFragranceException'

    _M_Demo._t_UnsupportedFragranceException = IcePy.defineException('::Demo::UnsupportedFragranceException', UnsupportedFragranceException, (), False, None, (('reason', (), IcePy._t_string, False, 0),))
    UnsupportedFragranceException._ice_type = _M_Demo._t_UnsupportedFragranceException

    _M_Demo.UnsupportedFragranceException = UnsupportedFragranceException
    del UnsupportedFragranceException

_M_Demo._t_Printer = IcePy.defineValue('::Demo::Printer', Ice.Value, -1, (), False, True, None, ())

if 'PrinterPrx' not in _M_Demo.__dict__:
    _M_Demo.PrinterPrx = Ice.createTempClass()
    class PrinterPrx(Ice.ObjectPrx):

        def printString(self, s, context=None):
            return _M_Demo.Printer._op_printString.invoke(self, ((s, ), context))

        def printStringAsync(self, s, context=None):
            return _M_Demo.Printer._op_printString.invokeAsync(self, ((s, ), context))

        def begin_printString(self, s, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Printer._op_printString.begin(self, ((s, ), _response, _ex, _sent, context))

        def end_printString(self, _r):
            return _M_Demo.Printer._op_printString.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.PrinterPrx.ice_checkedCast(proxy, '::Demo::Printer', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.PrinterPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Demo::Printer'
    _M_Demo._t_PrinterPrx = IcePy.defineProxy('::Demo::Printer', PrinterPrx)

    _M_Demo.PrinterPrx = PrinterPrx
    del PrinterPrx

    _M_Demo.Printer = Ice.createTempClass()
    class Printer(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Demo::Printer', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::Printer'

        @staticmethod
        def ice_staticId():
            return '::Demo::Printer'

        def printString(self, s, current=None):
            raise NotImplementedError("servant method 'printString' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_PrinterDisp)

        __repr__ = __str__

    _M_Demo._t_PrinterDisp = IcePy.defineClass('::Demo::Printer', Printer, (), None, ())
    Printer._ice_type = _M_Demo._t_PrinterDisp

    Printer._op_printString = IcePy.Operation('printString', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_string, False, 0),), (), None, ())

    _M_Demo.Printer = Printer
    del Printer

_M_Demo._t_Device = IcePy.defineValue('::Demo::Device', Ice.Value, -1, (), False, True, None, ())

if 'DevicePrx' not in _M_Demo.__dict__:
    _M_Demo.DevicePrx = Ice.createTempClass()
    class DevicePrx(Ice.ObjectPrx):

        def turnOn(self, context=None):
            return _M_Demo.Device._op_turnOn.invoke(self, ((), context))

        def turnOnAsync(self, context=None):
            return _M_Demo.Device._op_turnOn.invokeAsync(self, ((), context))

        def begin_turnOn(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Device._op_turnOn.begin(self, ((), _response, _ex, _sent, context))

        def end_turnOn(self, _r):
            return _M_Demo.Device._op_turnOn.end(self, _r)

        def turnOff(self, context=None):
            return _M_Demo.Device._op_turnOff.invoke(self, ((), context))

        def turnOffAsync(self, context=None):
            return _M_Demo.Device._op_turnOff.invokeAsync(self, ((), context))

        def begin_turnOff(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Device._op_turnOff.begin(self, ((), _response, _ex, _sent, context))

        def end_turnOff(self, _r):
            return _M_Demo.Device._op_turnOff.end(self, _r)

        def getState(self, context=None):
            return _M_Demo.Device._op_getState.invoke(self, ((), context))

        def getStateAsync(self, context=None):
            return _M_Demo.Device._op_getState.invokeAsync(self, ((), context))

        def begin_getState(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Device._op_getState.begin(self, ((), _response, _ex, _sent, context))

        def end_getState(self, _r):
            return _M_Demo.Device._op_getState.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.DevicePrx.ice_checkedCast(proxy, '::Demo::Device', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.DevicePrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Demo::Device'
    _M_Demo._t_DevicePrx = IcePy.defineProxy('::Demo::Device', DevicePrx)

    _M_Demo.DevicePrx = DevicePrx
    del DevicePrx

    _M_Demo.Device = Ice.createTempClass()
    class Device(Ice.Object):

        def ice_ids(self, current=None):
            return ('::Demo::Device', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::Device'

        @staticmethod
        def ice_staticId():
            return '::Demo::Device'

        def turnOn(self, current=None):
            raise NotImplementedError("servant method 'turnOn' not implemented")

        def turnOff(self, current=None):
            raise NotImplementedError("servant method 'turnOff' not implemented")

        def getState(self, current=None):
            raise NotImplementedError("servant method 'getState' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_DeviceDisp)

        __repr__ = __str__

    _M_Demo._t_DeviceDisp = IcePy.defineClass('::Demo::Device', Device, (), None, ())
    Device._ice_type = _M_Demo._t_DeviceDisp

    Device._op_turnOn = IcePy.Operation('turnOn', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Device._op_turnOff = IcePy.Operation('turnOff', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), None, ())
    Device._op_getState = IcePy.Operation('getState', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_bool, False, 0), ())

    _M_Demo.Device = Device
    del Device

_M_Demo._t_Bulbulator = IcePy.defineValue('::Demo::Bulbulator', Ice.Value, -1, (), False, True, None, ())

if 'BulbulatorPrx' not in _M_Demo.__dict__:
    _M_Demo.BulbulatorPrx = Ice.createTempClass()
    class BulbulatorPrx(_M_Demo.DevicePrx):

        def bulbulate(self, b, context=None):
            return _M_Demo.Bulbulator._op_bulbulate.invoke(self, ((b, ), context))

        def bulbulateAsync(self, b, context=None):
            return _M_Demo.Bulbulator._op_bulbulate.invokeAsync(self, ((b, ), context))

        def begin_bulbulate(self, b, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.Bulbulator._op_bulbulate.begin(self, ((b, ), _response, _ex, _sent, context))

        def end_bulbulate(self, _r):
            return _M_Demo.Bulbulator._op_bulbulate.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.BulbulatorPrx.ice_checkedCast(proxy, '::Demo::Bulbulator', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.BulbulatorPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Demo::Bulbulator'
    _M_Demo._t_BulbulatorPrx = IcePy.defineProxy('::Demo::Bulbulator', BulbulatorPrx)

    _M_Demo.BulbulatorPrx = BulbulatorPrx
    del BulbulatorPrx

    _M_Demo.Bulbulator = Ice.createTempClass()
    class Bulbulator(_M_Demo.Device):

        def ice_ids(self, current=None):
            return ('::Demo::Bulbulator', '::Demo::Device', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::Bulbulator'

        @staticmethod
        def ice_staticId():
            return '::Demo::Bulbulator'

        def bulbulate(self, b, current=None):
            raise NotImplementedError("servant method 'bulbulate' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_BulbulatorDisp)

        __repr__ = __str__

    _M_Demo._t_BulbulatorDisp = IcePy.defineClass('::Demo::Bulbulator', Bulbulator, (), None, (_M_Demo._t_DeviceDisp,))
    Bulbulator._ice_type = _M_Demo._t_BulbulatorDisp

    Bulbulator._op_bulbulate = IcePy.Operation('bulbulate', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), ((), IcePy._t_string, False, 0), ())

    _M_Demo.Bulbulator = Bulbulator
    del Bulbulator

if 'Fragrance' not in _M_Demo.__dict__:
    _M_Demo.Fragrance = Ice.createTempClass()
    class Fragrance(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    Fragrance.LAVENDER = Fragrance("LAVENDER", 0)
    Fragrance.CITRUS = Fragrance("CITRUS", 1)
    Fragrance.VANILLA = Fragrance("VANILLA", 2)
    Fragrance.ROSE = Fragrance("ROSE", 3)
    Fragrance.OCEAN = Fragrance("OCEAN", 4)
    Fragrance.FRESHLINEN = Fragrance("FRESHLINEN", 5)
    Fragrance.SANDALWOOD = Fragrance("SANDALWOOD", 6)
    Fragrance.JASMINE = Fragrance("JASMINE", 7)
    Fragrance.PEPPERMINT = Fragrance("PEPPERMINT", 8)
    Fragrance.EUCALYPTUS = Fragrance("EUCALYPTUS", 9)
    Fragrance._enumerators = { 0:Fragrance.LAVENDER, 1:Fragrance.CITRUS, 2:Fragrance.VANILLA, 3:Fragrance.ROSE, 4:Fragrance.OCEAN, 5:Fragrance.FRESHLINEN, 6:Fragrance.SANDALWOOD, 7:Fragrance.JASMINE, 8:Fragrance.PEPPERMINT, 9:Fragrance.EUCALYPTUS }

    _M_Demo._t_Fragrance = IcePy.defineEnum('::Demo::Fragrance', Fragrance, (), Fragrance._enumerators)

    _M_Demo.Fragrance = Fragrance
    del Fragrance

if '_t_Fragrances' not in _M_Demo.__dict__:
    _M_Demo._t_Fragrances = IcePy.defineSequence('::Demo::Fragrances', (), _M_Demo._t_Fragrance)

if 'ScheduleBlock' not in _M_Demo.__dict__:
    _M_Demo.ScheduleBlock = Ice.createTempClass()
    class ScheduleBlock(object):
        def __init__(self, startTime='', endTime='', temperature=0, humidity=0, fragrances=None):
            self.startTime = startTime
            self.endTime = endTime
            self.temperature = temperature
            self.humidity = humidity
            self.fragrances = fragrances

        def __hash__(self):
            _h = 0
            _h = 5 * _h + Ice.getHash(self.startTime)
            _h = 5 * _h + Ice.getHash(self.endTime)
            _h = 5 * _h + Ice.getHash(self.temperature)
            _h = 5 * _h + Ice.getHash(self.humidity)
            if self.fragrances:
                for _i0 in self.fragrances:
                    _h = 5 * _h + Ice.getHash(_i0)
            return _h % 0x7fffffff

        def __compare(self, other):
            if other is None:
                return 1
            elif not isinstance(other, _M_Demo.ScheduleBlock):
                return NotImplemented
            else:
                if self.startTime is None or other.startTime is None:
                    if self.startTime != other.startTime:
                        return (-1 if self.startTime is None else 1)
                else:
                    if self.startTime < other.startTime:
                        return -1
                    elif self.startTime > other.startTime:
                        return 1
                if self.endTime is None or other.endTime is None:
                    if self.endTime != other.endTime:
                        return (-1 if self.endTime is None else 1)
                else:
                    if self.endTime < other.endTime:
                        return -1
                    elif self.endTime > other.endTime:
                        return 1
                if self.temperature is None or other.temperature is None:
                    if self.temperature != other.temperature:
                        return (-1 if self.temperature is None else 1)
                else:
                    if self.temperature < other.temperature:
                        return -1
                    elif self.temperature > other.temperature:
                        return 1
                if self.humidity is None or other.humidity is None:
                    if self.humidity != other.humidity:
                        return (-1 if self.humidity is None else 1)
                else:
                    if self.humidity < other.humidity:
                        return -1
                    elif self.humidity > other.humidity:
                        return 1
                if self.fragrances is None or other.fragrances is None:
                    if self.fragrances != other.fragrances:
                        return (-1 if self.fragrances is None else 1)
                else:
                    if self.fragrances < other.fragrances:
                        return -1
                    elif self.fragrances > other.fragrances:
                        return 1
                return 0

        def __lt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r < 0

        def __le__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r <= 0

        def __gt__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r > 0

        def __ge__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r >= 0

        def __eq__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r == 0

        def __ne__(self, other):
            r = self.__compare(other)
            if r is NotImplemented:
                return r
            else:
                return r != 0

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_ScheduleBlock)

        __repr__ = __str__

    _M_Demo._t_ScheduleBlock = IcePy.defineStruct('::Demo::ScheduleBlock', ScheduleBlock, (), (
        ('startTime', (), IcePy._t_string),
        ('endTime', (), IcePy._t_string),
        ('temperature', (), IcePy._t_int),
        ('humidity', (), IcePy._t_int),
        ('fragrances', (), _M_Demo._t_Fragrances)
    ))

    _M_Demo.ScheduleBlock = ScheduleBlock
    del ScheduleBlock

if '_t_Schedules' not in _M_Demo.__dict__:
    _M_Demo._t_Schedules = IcePy.defineSequence('::Demo::Schedules', (), _M_Demo._t_ScheduleBlock)

_M_Demo._t_HVAC = IcePy.defineValue('::Demo::HVAC', Ice.Value, -1, (), False, True, None, ())

if 'HVACPrx' not in _M_Demo.__dict__:
    _M_Demo.HVACPrx = Ice.createTempClass()
    class HVACPrx(_M_Demo.DevicePrx):

        def setTemperature(self, t, context=None):
            return _M_Demo.HVAC._op_setTemperature.invoke(self, ((t, ), context))

        def setTemperatureAsync(self, t, context=None):
            return _M_Demo.HVAC._op_setTemperature.invokeAsync(self, ((t, ), context))

        def begin_setTemperature(self, t, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.HVAC._op_setTemperature.begin(self, ((t, ), _response, _ex, _sent, context))

        def end_setTemperature(self, _r):
            return _M_Demo.HVAC._op_setTemperature.end(self, _r)

        def getTemperature(self, context=None):
            return _M_Demo.HVAC._op_getTemperature.invoke(self, ((), context))

        def getTemperatureAsync(self, context=None):
            return _M_Demo.HVAC._op_getTemperature.invokeAsync(self, ((), context))

        def begin_getTemperature(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.HVAC._op_getTemperature.begin(self, ((), _response, _ex, _sent, context))

        def end_getTemperature(self, _r):
            return _M_Demo.HVAC._op_getTemperature.end(self, _r)

        def setHumidity(self, h, context=None):
            return _M_Demo.HVAC._op_setHumidity.invoke(self, ((h, ), context))

        def setHumidityAsync(self, h, context=None):
            return _M_Demo.HVAC._op_setHumidity.invokeAsync(self, ((h, ), context))

        def begin_setHumidity(self, h, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.HVAC._op_setHumidity.begin(self, ((h, ), _response, _ex, _sent, context))

        def end_setHumidity(self, _r):
            return _M_Demo.HVAC._op_setHumidity.end(self, _r)

        def getHumidity(self, context=None):
            return _M_Demo.HVAC._op_getHumidity.invoke(self, ((), context))

        def getHumidityAsync(self, context=None):
            return _M_Demo.HVAC._op_getHumidity.invokeAsync(self, ((), context))

        def begin_getHumidity(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.HVAC._op_getHumidity.begin(self, ((), _response, _ex, _sent, context))

        def end_getHumidity(self, _r):
            return _M_Demo.HVAC._op_getHumidity.end(self, _r)

        def setFragrances(self, f, context=None):
            return _M_Demo.HVAC._op_setFragrances.invoke(self, ((f, ), context))

        def setFragrancesAsync(self, f, context=None):
            return _M_Demo.HVAC._op_setFragrances.invokeAsync(self, ((f, ), context))

        def begin_setFragrances(self, f, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.HVAC._op_setFragrances.begin(self, ((f, ), _response, _ex, _sent, context))

        def end_setFragrances(self, _r):
            return _M_Demo.HVAC._op_setFragrances.end(self, _r)

        def getFragrances(self, context=None):
            return _M_Demo.HVAC._op_getFragrances.invoke(self, ((), context))

        def getFragrancesAsync(self, context=None):
            return _M_Demo.HVAC._op_getFragrances.invokeAsync(self, ((), context))

        def begin_getFragrances(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.HVAC._op_getFragrances.begin(self, ((), _response, _ex, _sent, context))

        def end_getFragrances(self, _r):
            return _M_Demo.HVAC._op_getFragrances.end(self, _r)

        def addSchedule(self, s, context=None):
            return _M_Demo.HVAC._op_addSchedule.invoke(self, ((s, ), context))

        def addScheduleAsync(self, s, context=None):
            return _M_Demo.HVAC._op_addSchedule.invokeAsync(self, ((s, ), context))

        def begin_addSchedule(self, s, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.HVAC._op_addSchedule.begin(self, ((s, ), _response, _ex, _sent, context))

        def end_addSchedule(self, _r):
            return _M_Demo.HVAC._op_addSchedule.end(self, _r)

        def getSchedules(self, context=None):
            return _M_Demo.HVAC._op_getSchedules.invoke(self, ((), context))

        def getSchedulesAsync(self, context=None):
            return _M_Demo.HVAC._op_getSchedules.invokeAsync(self, ((), context))

        def begin_getSchedules(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.HVAC._op_getSchedules.begin(self, ((), _response, _ex, _sent, context))

        def end_getSchedules(self, _r):
            return _M_Demo.HVAC._op_getSchedules.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.HVACPrx.ice_checkedCast(proxy, '::Demo::HVAC', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.HVACPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Demo::HVAC'
    _M_Demo._t_HVACPrx = IcePy.defineProxy('::Demo::HVAC', HVACPrx)

    _M_Demo.HVACPrx = HVACPrx
    del HVACPrx

    _M_Demo.HVAC = Ice.createTempClass()
    class HVAC(_M_Demo.Device):

        def ice_ids(self, current=None):
            return ('::Demo::Device', '::Demo::HVAC', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::HVAC'

        @staticmethod
        def ice_staticId():
            return '::Demo::HVAC'

        def setTemperature(self, t, current=None):
            raise NotImplementedError("servant method 'setTemperature' not implemented")

        def getTemperature(self, current=None):
            raise NotImplementedError("servant method 'getTemperature' not implemented")

        def setHumidity(self, h, current=None):
            raise NotImplementedError("servant method 'setHumidity' not implemented")

        def getHumidity(self, current=None):
            raise NotImplementedError("servant method 'getHumidity' not implemented")

        def setFragrances(self, f, current=None):
            raise NotImplementedError("servant method 'setFragrances' not implemented")

        def getFragrances(self, current=None):
            raise NotImplementedError("servant method 'getFragrances' not implemented")

        def addSchedule(self, s, current=None):
            raise NotImplementedError("servant method 'addSchedule' not implemented")

        def getSchedules(self, current=None):
            raise NotImplementedError("servant method 'getSchedules' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_HVACDisp)

        __repr__ = __str__

    _M_Demo._t_HVACDisp = IcePy.defineClass('::Demo::HVAC', HVAC, (), None, (_M_Demo._t_DeviceDisp,))
    HVAC._ice_type = _M_Demo._t_HVACDisp

    HVAC._op_setTemperature = IcePy.Operation('setTemperature', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), None, (_M_Demo._t_ValueOutOfRangeException,))
    HVAC._op_getTemperature = IcePy.Operation('getTemperature', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_int, False, 0), ())
    HVAC._op_setHumidity = IcePy.Operation('setHumidity', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), None, (_M_Demo._t_ValueOutOfRangeException,))
    HVAC._op_getHumidity = IcePy.Operation('getHumidity', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_int, False, 0), ())
    HVAC._op_setFragrances = IcePy.Operation('setFragrances', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Demo._t_Fragrances, False, 0),), (), None, (_M_Demo._t_UnsupportedFragranceException,))
    HVAC._op_getFragrances = IcePy.Operation('getFragrances', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Demo._t_Fragrances, False, 0), ())
    HVAC._op_addSchedule = IcePy.Operation('addSchedule', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Demo._t_ScheduleBlock, False, 0),), (), None, (_M_Demo._t_ValueOutOfRangeException, _M_Demo._t_UnsupportedFragranceException))
    HVAC._op_getSchedules = IcePy.Operation('getSchedules', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Demo._t_Schedules, False, 0), ())

    _M_Demo.HVAC = HVAC
    del HVAC

if 'Color' not in _M_Demo.__dict__:
    _M_Demo.Color = Ice.createTempClass()
    class Color(Ice.EnumBase):

        def __init__(self, _n, _v):
            Ice.EnumBase.__init__(self, _n, _v)

        def valueOf(self, _n):
            if _n in self._enumerators:
                return self._enumerators[_n]
            return None
        valueOf = classmethod(valueOf)

    Color.RED = Color("RED", 0)
    Color.GREEN = Color("GREEN", 1)
    Color.BLUE = Color("BLUE", 2)
    Color.YELLOW = Color("YELLOW", 3)
    Color.PURPLE = Color("PURPLE", 4)
    Color.ORANGE = Color("ORANGE", 5)
    Color.WHITE = Color("WHITE", 6)
    Color.PINK = Color("PINK", 7)
    Color.CYAN = Color("CYAN", 8)
    Color.LIME = Color("LIME", 9)
    Color._enumerators = { 0:Color.RED, 1:Color.GREEN, 2:Color.BLUE, 3:Color.YELLOW, 4:Color.PURPLE, 5:Color.ORANGE, 6:Color.WHITE, 7:Color.PINK, 8:Color.CYAN, 9:Color.LIME }

    _M_Demo._t_Color = IcePy.defineEnum('::Demo::Color', Color, (), Color._enumerators)

    _M_Demo.Color = Color
    del Color

if '_t_Colors' not in _M_Demo.__dict__:
    _M_Demo._t_Colors = IcePy.defineSequence('::Demo::Colors', (), _M_Demo._t_Color)

_M_Demo._t_Light = IcePy.defineValue('::Demo::Light', Ice.Value, -1, (), False, True, None, ())

if 'LightPrx' not in _M_Demo.__dict__:
    _M_Demo.LightPrx = Ice.createTempClass()
    class LightPrx(_M_Demo.DevicePrx):

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.LightPrx.ice_checkedCast(proxy, '::Demo::Light', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.LightPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Demo::Light'
    _M_Demo._t_LightPrx = IcePy.defineProxy('::Demo::Light', LightPrx)

    _M_Demo.LightPrx = LightPrx
    del LightPrx

    _M_Demo.Light = Ice.createTempClass()
    class Light(_M_Demo.Device):

        def ice_ids(self, current=None):
            return ('::Demo::Device', '::Demo::Light', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::Light'

        @staticmethod
        def ice_staticId():
            return '::Demo::Light'

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_LightDisp)

        __repr__ = __str__

    _M_Demo._t_LightDisp = IcePy.defineClass('::Demo::Light', Light, (), None, (_M_Demo._t_DeviceDisp,))
    Light._ice_type = _M_Demo._t_LightDisp

    _M_Demo.Light = Light
    del Light

_M_Demo._t_LightController = IcePy.defineValue('::Demo::LightController', Ice.Value, -1, (), False, True, None, ())

if 'LightControllerPrx' not in _M_Demo.__dict__:
    _M_Demo.LightControllerPrx = Ice.createTempClass()
    class LightControllerPrx(_M_Demo.DevicePrx):

        def setBrightness(self, b, context=None):
            return _M_Demo.LightController._op_setBrightness.invoke(self, ((b, ), context))

        def setBrightnessAsync(self, b, context=None):
            return _M_Demo.LightController._op_setBrightness.invokeAsync(self, ((b, ), context))

        def begin_setBrightness(self, b, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.LightController._op_setBrightness.begin(self, ((b, ), _response, _ex, _sent, context))

        def end_setBrightness(self, _r):
            return _M_Demo.LightController._op_setBrightness.end(self, _r)

        def getBrightness(self, context=None):
            return _M_Demo.LightController._op_getBrightness.invoke(self, ((), context))

        def getBrightnessAsync(self, context=None):
            return _M_Demo.LightController._op_getBrightness.invokeAsync(self, ((), context))

        def begin_getBrightness(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.LightController._op_getBrightness.begin(self, ((), _response, _ex, _sent, context))

        def end_getBrightness(self, _r):
            return _M_Demo.LightController._op_getBrightness.end(self, _r)

        def setColor(self, c, context=None):
            return _M_Demo.LightController._op_setColor.invoke(self, ((c, ), context))

        def setColorAsync(self, c, context=None):
            return _M_Demo.LightController._op_setColor.invokeAsync(self, ((c, ), context))

        def begin_setColor(self, c, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.LightController._op_setColor.begin(self, ((c, ), _response, _ex, _sent, context))

        def end_setColor(self, _r):
            return _M_Demo.LightController._op_setColor.end(self, _r)

        def getColor(self, context=None):
            return _M_Demo.LightController._op_getColor.invoke(self, ((), context))

        def getColorAsync(self, context=None):
            return _M_Demo.LightController._op_getColor.invokeAsync(self, ((), context))

        def begin_getColor(self, _response=None, _ex=None, _sent=None, context=None):
            return _M_Demo.LightController._op_getColor.begin(self, ((), _response, _ex, _sent, context))

        def end_getColor(self, _r):
            return _M_Demo.LightController._op_getColor.end(self, _r)

        @staticmethod
        def checkedCast(proxy, facetOrContext=None, context=None):
            return _M_Demo.LightControllerPrx.ice_checkedCast(proxy, '::Demo::LightController', facetOrContext, context)

        @staticmethod
        def uncheckedCast(proxy, facet=None):
            return _M_Demo.LightControllerPrx.ice_uncheckedCast(proxy, facet)

        @staticmethod
        def ice_staticId():
            return '::Demo::LightController'
    _M_Demo._t_LightControllerPrx = IcePy.defineProxy('::Demo::LightController', LightControllerPrx)

    _M_Demo.LightControllerPrx = LightControllerPrx
    del LightControllerPrx

    _M_Demo.LightController = Ice.createTempClass()
    class LightController(_M_Demo.Device):

        def ice_ids(self, current=None):
            return ('::Demo::Device', '::Demo::LightController', '::Ice::Object')

        def ice_id(self, current=None):
            return '::Demo::LightController'

        @staticmethod
        def ice_staticId():
            return '::Demo::LightController'

        def setBrightness(self, b, current=None):
            raise NotImplementedError("servant method 'setBrightness' not implemented")

        def getBrightness(self, current=None):
            raise NotImplementedError("servant method 'getBrightness' not implemented")

        def setColor(self, c, current=None):
            raise NotImplementedError("servant method 'setColor' not implemented")

        def getColor(self, current=None):
            raise NotImplementedError("servant method 'getColor' not implemented")

        def __str__(self):
            return IcePy.stringify(self, _M_Demo._t_LightControllerDisp)

        __repr__ = __str__

    _M_Demo._t_LightControllerDisp = IcePy.defineClass('::Demo::LightController', LightController, (), None, (_M_Demo._t_DeviceDisp,))
    LightController._ice_type = _M_Demo._t_LightControllerDisp

    LightController._op_setBrightness = IcePy.Operation('setBrightness', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), IcePy._t_int, False, 0),), (), None, (_M_Demo._t_ValueOutOfRangeException,))
    LightController._op_getBrightness = IcePy.Operation('getBrightness', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), IcePy._t_int, False, 0), ())
    LightController._op_setColor = IcePy.Operation('setColor', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (((), _M_Demo._t_Color, False, 0),), (), None, (_M_Demo._t_UnsupportedColorException,))
    LightController._op_getColor = IcePy.Operation('getColor', Ice.OperationMode.Normal, Ice.OperationMode.Normal, False, None, (), (), (), ((), _M_Demo._t_Color, False, 0), ())

    _M_Demo.LightController = LightController
    del LightController

# End of module Demo