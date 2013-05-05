# Copyright (c) 2008 The Board of Trustees of The Leland Stanford Junior University
# Copyright (c) 2011, 2012 Open Networking Foundation
# Copyright (c) 2012, 2013 Big Switch Networks, Inc.

# Automatically generated by LOXI from template instruction.py
# Do not modify

import struct
import action
import const
import util
import loxi.generic_util
import loxi

def unpack_list(reader):
    def deserializer(reader, typ):
        parser = parsers.get(typ)
        if not parser: raise loxi.ProtocolError("unknown instruction type %d" % typ)
        return parser(reader)
    return loxi.generic_util.unpack_list_tlv16(reader, deserializer)

class Instruction(object):
    type = None # override in subclass
    pass

class apply_actions(Instruction):
    type = const.OFPIT_APPLY_ACTIONS

    def __init__(self, actions=None):
        if actions != None:
            self.actions = actions
        else:
            self.actions = []
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append('\x00' * 4)
        packed.append("".join([x.pack() for x in self.actions]))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = apply_actions()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPIT_APPLY_ACTIONS)
        _len = reader.read('!H')[0]
        reader.skip(4)
        obj.actions = action.unpack_list(reader)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.actions != other.actions: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("apply_actions {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("actions = ");
                q.pp(self.actions)
            q.breakable()
        q.text('}')

class clear_actions(Instruction):
    type = const.OFPIT_CLEAR_ACTIONS

    def __init__(self):
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append('\x00' * 4)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = clear_actions()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPIT_CLEAR_ACTIONS)
        _len = reader.read('!H')[0]
        reader.skip(4)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("clear_actions {")
        with q.group():
            with q.indent(2):
                q.breakable()
            q.breakable()
        q.text('}')

class experimenter(Instruction):
    type = const.OFPIT_EXPERIMENTER

    def __init__(self, experimenter=None, data=None):
        if experimenter != None:
            self.experimenter = experimenter
        else:
            self.experimenter = 0
        if data != None:
            self.data = data
        else:
            self.data = ""
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.experimenter))
        packed.append(self.data)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = experimenter()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPIT_EXPERIMENTER)
        _len = reader.read('!H')[0]
        obj.experimenter = reader.read('!L')[0]
        obj.data = str(reader.read_all())
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.experimenter != other.experimenter: return False
        if self.data != other.data: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("experimenter {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("experimenter = ");
                q.text("%#x" % self.experimenter)
                q.text(","); q.breakable()
                q.text("data = ");
                q.pp(self.data)
            q.breakable()
        q.text('}')

class goto_table(Instruction):
    type = const.OFPIT_GOTO_TABLE

    def __init__(self, table_id=None):
        if table_id != None:
            self.table_id = table_id
        else:
            self.table_id = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!B", self.table_id))
        packed.append('\x00' * 3)
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = goto_table()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPIT_GOTO_TABLE)
        _len = reader.read('!H')[0]
        obj.table_id = reader.read('!B')[0]
        reader.skip(3)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.table_id != other.table_id: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("goto_table {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("table_id = ");
                q.text("%#x" % self.table_id)
            q.breakable()
        q.text('}')

class meter(Instruction):
    type = const.OFPIT_METER

    def __init__(self, meter_id=None):
        if meter_id != None:
            self.meter_id = meter_id
        else:
            self.meter_id = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append(struct.pack("!L", self.meter_id))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = meter()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPIT_METER)
        _len = reader.read('!H')[0]
        obj.meter_id = reader.read('!L')[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.meter_id != other.meter_id: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("meter {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("meter_id = ");
                q.text("%#x" % self.meter_id)
            q.breakable()
        q.text('}')

class write_actions(Instruction):
    type = const.OFPIT_WRITE_ACTIONS

    def __init__(self, actions=None):
        if actions != None:
            self.actions = actions
        else:
            self.actions = []
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append('\x00' * 4)
        packed.append("".join([x.pack() for x in self.actions]))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = write_actions()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPIT_WRITE_ACTIONS)
        _len = reader.read('!H')[0]
        reader.skip(4)
        obj.actions = action.unpack_list(reader)
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.actions != other.actions: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("write_actions {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("actions = ");
                q.pp(self.actions)
            q.breakable()
        q.text('}')

class write_metadata(Instruction):
    type = const.OFPIT_WRITE_METADATA

    def __init__(self, metadata=None, metadata_mask=None):
        if metadata != None:
            self.metadata = metadata
        else:
            self.metadata = 0
        if metadata_mask != None:
            self.metadata_mask = metadata_mask
        else:
            self.metadata_mask = 0
        return

    def pack(self):
        packed = []
        packed.append(struct.pack("!H", self.type))
        packed.append(struct.pack("!H", 0)) # placeholder for len at index 1
        packed.append('\x00' * 4)
        packed.append(struct.pack("!Q", self.metadata))
        packed.append(struct.pack("!Q", self.metadata_mask))
        length = sum([len(x) for x in packed])
        packed[1] = struct.pack("!H", length)
        return ''.join(packed)

    @staticmethod
    def unpack(buf):
        obj = write_metadata()
        if type(buf) == loxi.generic_util.OFReader:
            reader = buf
        else:
            reader = loxi.generic_util.OFReader(buf)
        _type = reader.read('!H')[0]
        assert(_type == const.OFPIT_WRITE_METADATA)
        _len = reader.read('!H')[0]
        reader.skip(4)
        obj.metadata = reader.read('!Q')[0]
        obj.metadata_mask = reader.read('!Q')[0]
        return obj

    def __eq__(self, other):
        if type(self) != type(other): return False
        if self.metadata != other.metadata: return False
        if self.metadata_mask != other.metadata_mask: return False
        return True

    def __ne__(self, other):
        return not self.__eq__(other)

    def show(self):
        import loxi.pp
        return loxi.pp.pp(self)

    def pretty_print(self, q):
        q.text("write_metadata {")
        with q.group():
            with q.indent(2):
                q.breakable()
                q.text("metadata = ");
                q.text("%#x" % self.metadata)
                q.text(","); q.breakable()
                q.text("metadata_mask = ");
                q.text("%#x" % self.metadata_mask)
            q.breakable()
        q.text('}')


parsers = {
    const.OFPIT_APPLY_ACTIONS : apply_actions.unpack,
    const.OFPIT_CLEAR_ACTIONS : clear_actions.unpack,
    const.OFPIT_EXPERIMENTER : experimenter.unpack,
    const.OFPIT_GOTO_TABLE : goto_table.unpack,
    const.OFPIT_METER : meter.unpack,
    const.OFPIT_WRITE_ACTIONS : write_actions.unpack,
    const.OFPIT_WRITE_METADATA : write_metadata.unpack,
}
