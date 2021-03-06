# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: common.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='common.proto',
  package='types',
  syntax='proto3',
  serialized_pb=_b('\n\x0c\x63ommon.proto\x12\x05types\",\n\nFieldTypes\x12\x0c\n\x04name\x18\x01 \x01(\t\x12\x10\n\x08minScore\x18\x02 \x01(\t\"\x7f\n\rAnalyzeResult\x12\x0c\n\x04text\x18\x01 \x01(\t\x12 \n\x05\x66ield\x18\x02 \x01(\x0b\x32\x11.types.FieldTypes\x12\r\n\x05score\x18\x03 \x01(\x02\x12!\n\x08location\x18\x04 \x01(\x0b\x32\x0f.types.Location\x12\x0c\n\x04mask\x18\x05 \x01(\t\"6\n\x08Location\x12\r\n\x05start\x18\x01 \x01(\x11\x12\x0b\n\x03\x65nd\x18\x02 \x01(\x11\x12\x0e\n\x06length\x18\x03 \x01(\x11\"a\n\x05Image\x12\x0c\n\x04\x64\x61ta\x18\x01 \x01(\x0c\x12\x11\n\timageType\x18\x02 \x01(\t\x12)\n\rBoundingboxes\x18\x03 \x03(\x0b\x32\x12.types.Boundingbox\x12\x0c\n\x04text\x18\x04 \x01(\t\"\x8c\x01\n\x0b\x42oundingbox\x12\x11\n\txLocation\x18\x01 \x01(\x02\x12\r\n\x05width\x18\x02 \x01(\x02\x12\x11\n\tyLocation\x18\x03 \x01(\x02\x12\x0e\n\x06height\x18\x04 \x01(\x02\x12\x0c\n\x04text\x18\x05 \x01(\t\x12\x15\n\rstartPosition\x18\x06 \x01(\x11\x12\x13\n\x0b\x65ndPosition\x18\x07 \x01(\x11*\x95\x02\n\x0e\x46ieldTypesEnum\x12\x0f\n\x0b\x43REDIT_CARD\x10\x00\x12\n\n\x06\x43RYPTO\x10\x01\x12\r\n\tDATE_TIME\x10\x02\x12\x0f\n\x0b\x44OMAIN_NAME\x10\x03\x12\x11\n\rEMAIL_ADDRESS\x10\x04\x12\r\n\tIBAN_CODE\x10\x05\x12\x0e\n\nIP_ADDRESS\x10\x06\x12\x07\n\x03NRP\x10\x07\x12\x0c\n\x08LOCATION\x10\x08\x12\n\n\x06PERSON\x10\t\x12\x10\n\x0cPHONE_NUMBER\x10\n\x12\x12\n\x0eUS_BANK_NUMBER\x10\x0b\x12\x15\n\x11US_DRIVER_LICENSE\x10\x0c\x12\x0b\n\x07US_ITIN\x10\r\x12\x0f\n\x0bUS_PASSPORT\x10\x0e\x12\n\n\x06US_SSN\x10\x0f\x12\n\n\x06UK_NHS\x10\x10*;\n\x11\x44\x65tectionTypeEnum\x12\x07\n\x03OCR\x10\x00\x12\r\n\tAZURE_OCR\x10\x01\x12\x0e\n\nAZURE_FACE\x10\x02\x62\x06proto3')
)

_FIELDTYPESENUM = _descriptor.EnumDescriptor(
  name='FieldTypesEnum',
  full_name='types.FieldTypesEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='CREDIT_CARD', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='CRYPTO', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DATE_TIME', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOMAIN_NAME', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='EMAIL_ADDRESS', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IBAN_CODE', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='IP_ADDRESS', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='NRP', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='LOCATION', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PERSON', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='PHONE_NUMBER', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='US_BANK_NUMBER', index=11, number=11,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='US_DRIVER_LICENSE', index=12, number=12,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='US_ITIN', index=13, number=13,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='US_PASSPORT', index=14, number=14,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='US_SSN', index=15, number=15,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='UK_NHS', index=16, number=16,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=497,
  serialized_end=774,
)
_sym_db.RegisterEnumDescriptor(_FIELDTYPESENUM)

FieldTypesEnum = enum_type_wrapper.EnumTypeWrapper(_FIELDTYPESENUM)
_DETECTIONTYPEENUM = _descriptor.EnumDescriptor(
  name='DetectionTypeEnum',
  full_name='types.DetectionTypeEnum',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='OCR', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AZURE_OCR', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='AZURE_FACE', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=776,
  serialized_end=835,
)
_sym_db.RegisterEnumDescriptor(_DETECTIONTYPEENUM)

DetectionTypeEnum = enum_type_wrapper.EnumTypeWrapper(_DETECTIONTYPEENUM)
CREDIT_CARD = 0
CRYPTO = 1
DATE_TIME = 2
DOMAIN_NAME = 3
EMAIL_ADDRESS = 4
IBAN_CODE = 5
IP_ADDRESS = 6
NRP = 7
LOCATION = 8
PERSON = 9
PHONE_NUMBER = 10
US_BANK_NUMBER = 11
US_DRIVER_LICENSE = 12
US_ITIN = 13
US_PASSPORT = 14
US_SSN = 15
UK_NHS = 16
OCR = 0
AZURE_OCR = 1
AZURE_FACE = 2



_FIELDTYPES = _descriptor.Descriptor(
  name='FieldTypes',
  full_name='types.FieldTypes',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='name', full_name='types.FieldTypes.name', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='minScore', full_name='types.FieldTypes.minScore', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=23,
  serialized_end=67,
)


_ANALYZERESULT = _descriptor.Descriptor(
  name='AnalyzeResult',
  full_name='types.AnalyzeResult',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='text', full_name='types.AnalyzeResult.text', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='field', full_name='types.AnalyzeResult.field', index=1,
      number=2, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='score', full_name='types.AnalyzeResult.score', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='location', full_name='types.AnalyzeResult.location', index=3,
      number=4, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='mask', full_name='types.AnalyzeResult.mask', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=69,
  serialized_end=196,
)


_LOCATION = _descriptor.Descriptor(
  name='Location',
  full_name='types.Location',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='start', full_name='types.Location.start', index=0,
      number=1, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='end', full_name='types.Location.end', index=1,
      number=2, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='length', full_name='types.Location.length', index=2,
      number=3, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=198,
  serialized_end=252,
)


_IMAGE = _descriptor.Descriptor(
  name='Image',
  full_name='types.Image',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='data', full_name='types.Image.data', index=0,
      number=1, type=12, cpp_type=9, label=1,
      has_default_value=False, default_value=_b(""),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='imageType', full_name='types.Image.imageType', index=1,
      number=2, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='Boundingboxes', full_name='types.Image.Boundingboxes', index=2,
      number=3, type=11, cpp_type=10, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='types.Image.text', index=3,
      number=4, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=254,
  serialized_end=351,
)


_BOUNDINGBOX = _descriptor.Descriptor(
  name='Boundingbox',
  full_name='types.Boundingbox',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='xLocation', full_name='types.Boundingbox.xLocation', index=0,
      number=1, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='width', full_name='types.Boundingbox.width', index=1,
      number=2, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='yLocation', full_name='types.Boundingbox.yLocation', index=2,
      number=3, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='height', full_name='types.Boundingbox.height', index=3,
      number=4, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=float(0),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='text', full_name='types.Boundingbox.text', index=4,
      number=5, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='startPosition', full_name='types.Boundingbox.startPosition', index=5,
      number=6, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='endPosition', full_name='types.Boundingbox.endPosition', index=6,
      number=7, type=17, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=354,
  serialized_end=494,
)

_ANALYZERESULT.fields_by_name['field'].message_type = _FIELDTYPES
_ANALYZERESULT.fields_by_name['location'].message_type = _LOCATION
_IMAGE.fields_by_name['Boundingboxes'].message_type = _BOUNDINGBOX
DESCRIPTOR.message_types_by_name['FieldTypes'] = _FIELDTYPES
DESCRIPTOR.message_types_by_name['AnalyzeResult'] = _ANALYZERESULT
DESCRIPTOR.message_types_by_name['Location'] = _LOCATION
DESCRIPTOR.message_types_by_name['Image'] = _IMAGE
DESCRIPTOR.message_types_by_name['Boundingbox'] = _BOUNDINGBOX
DESCRIPTOR.enum_types_by_name['FieldTypesEnum'] = _FIELDTYPESENUM
DESCRIPTOR.enum_types_by_name['DetectionTypeEnum'] = _DETECTIONTYPEENUM
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

FieldTypes = _reflection.GeneratedProtocolMessageType('FieldTypes', (_message.Message,), dict(
  DESCRIPTOR = _FIELDTYPES,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:types.FieldTypes)
  ))
_sym_db.RegisterMessage(FieldTypes)

AnalyzeResult = _reflection.GeneratedProtocolMessageType('AnalyzeResult', (_message.Message,), dict(
  DESCRIPTOR = _ANALYZERESULT,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:types.AnalyzeResult)
  ))
_sym_db.RegisterMessage(AnalyzeResult)

Location = _reflection.GeneratedProtocolMessageType('Location', (_message.Message,), dict(
  DESCRIPTOR = _LOCATION,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:types.Location)
  ))
_sym_db.RegisterMessage(Location)

Image = _reflection.GeneratedProtocolMessageType('Image', (_message.Message,), dict(
  DESCRIPTOR = _IMAGE,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:types.Image)
  ))
_sym_db.RegisterMessage(Image)

Boundingbox = _reflection.GeneratedProtocolMessageType('Boundingbox', (_message.Message,), dict(
  DESCRIPTOR = _BOUNDINGBOX,
  __module__ = 'common_pb2'
  # @@protoc_insertion_point(class_scope:types.Boundingbox)
  ))
_sym_db.RegisterMessage(Boundingbox)


# @@protoc_insertion_point(module_scope)
