#!/Users/beezarts/pycode/ambient/venv/bin/python
"""
Synopsis:
    Generate Python classes from XML schema definition.
    Input is read from in_xsd_file or, if "-" (dash) arg, from stdin.
    Output is written to files named in "-o" and "-s" options.
Usage:
    python generateDS.py [ options ] <xsd_file>
    python generateDS.py [ options ] -
Options:
    -h, --help               Display this help information.
    -o <outfilename>         Output file name for data representation classes
    -s <subclassfilename>    Output file name for subclasses
    -p <prefix>              Prefix string to be pre-pended to the class names
    -f                       Force creation of output files.  Do not ask.
    -a <namespaceabbrev>     Namespace abbreviation, e.g. "xsd:".
                             Default = 'xs:'.
    -b <behaviorfilename>    Input file name for behaviors added to subclasses
    -m                       Generate properties for member variables
    -c <xmlcatalogfilename>  Input file name to load an XML catalog
    --one-file-per-xsd       Create a python module for each XSD processed.
    --output-directory="XXX" Used in conjunction with --one-file-per-xsd.
                             The directory where the modules will be created.
    --module-suffix="XXX"    To be used in conjunction with --one-file-per-xsd.
                             Append XXX to the end of each file created.
    --subclass-suffix="XXX"  Append XXX to the generated subclass names.
                             Default="Sub".
    --root-element="XX"      When parsing, assume XX is root element of
    --root-element="XX|YY"   instance docs.  Default is first element defined
                             in schema.  If YY is added, then YY is used as the
                             top level class; if YY omitted XX is the default.
                             class. Also see section "Recognizing the top level
                             element" in the documentation.
    --super="XXX"            Super module name in generated subclass
                             module. Default="???"
    --validator-bodies=path  Path to a directory containing files that provide
                             bodies (implementations) of validator methods.
    --use-old-simpletype-validators
                             Use the old style simpleType validator functions
                             stored in a specified directory, instead of the
                             new style validators generated directly from the
                             XML schema.  See option --validator-bodies.
    --use-getter-setter      Generate getter and setter methods.  Values:
                             "old" - Name getters/setters getVar()/setVar().
                             "new" - Name getters/setters get_var()/set_var().
                             "none" - Do not generate getter/setter methods.
                             Default is "new".
    --use-source-file-as-module-name
                             Used in conjunction with --one-file-per-xsd to
                             use the source XSD file names to determine the
                             module name of the generated classes.
    --user-methods= <file_path>,
    -u <file_path>           Optional module containing user methods.  See
                             section "User Methods" in the documentation.
    --custom-imports-template=<file_path>
                             Optional file with custom imports directives
                             which can be used via the --user-methods option.
    --no-dates               Do not include the current date in the generated
                             files. This is useful if you want to minimize
                             the amount of (no-operation) changes to the
                             generated python code.
    --no-versions            Do not include the current version in the
                             generated files. This is useful if you want
                             to minimize the amount of (no-operation)
                             changes to the generated python code.
    --no-process-includes    Do not use process_includes.py to pre-process
                             included XML schema files.  By default,
                             generateDS.py will insert content from files
                             referenced by xs:include and xs:import elements
                             into the XML schema to be processed and perform
                             several other pre-procesing tasks.  You likely do
                             not want to use this option; its use has been
                             reported to result in errors in generated modules.
                             Consider using --no-collect-includes and/or
                             --no-redefine-groups instead.
    --no-collect-includes    Do not (recursively) collect and insert schemas
                             referenced by xs:include and xs:import elements.
    --no-redefine-groups     Do not pre-process and redefine group definitions.
    --silence                Normally, the code generated with generateDS
                             echoes the information being parsed. To prevent
                             the echo from occurring, use the --silence switch.
                             Also note optional "silence" parameter on
                             generated functions, e.g. parse, parseString, etc.
    --namespacedef='xmlns:abc="http://www.abc.com"'
                             Namespace definition to be passed in as the
                             value for the namespacedef_ parameter of
                             the export() method by the generated
                             parse() and parseString() functions.
                             Default=''.
    --no-namespace-defs      Do not pass namespace definitions as the value
                             for the namespacedef_ parameter of the export
                             method, even if it can be extraced from the
                             schema.
    --external-encoding=<encoding>
                             Encode output written by the generated export
                             methods using this encoding.  Default, if omitted,
                             is the value returned by sys.getdefaultencoding().
                             Example: --external-encoding='utf-8'.
    --member-specs=list|dict
                             Generate member (type) specifications in each
                             class: a dictionary of instances of class
                             MemberSpec_ containing member name, type,
                             and array or not.  Allowed values are
                             "list" or "dict".  Default: do not generate.
    --export=<export-list>   Specifies export functions to be generated.
                             Value is a whitespace separated list of
                             any of the following:
                                 write -- write XML to file
                                 literal -- write out python code
                                 etree -- build element tree (can serialize
                                     to XML)
                                 django -- load XML to django database
                                 sqlalchemy -- load XML to sqlalchemy database
                                 validate -- call all validators for object
                                 generator -- recursive generator method
                             Example: "write etree"
                             Default: "write"
    --always-export-default  Always export elements and attributes that
                             a default value even when the current value
                             is equal to the default.  Default: False.
    --disable-generatedssuper-lookup
                             Disables the generatetion of the lookup logic for
                             presence of an external module from which to load
                             a custom `GeneratedsSuper` base-class definition.
    --disable-xml            Disables generation of all XML build/export
                             methods and command line interface
    --enable-slots           Enables the use of slots for generated class
                             members.  Requires --member-specs=dict.
    --preserve-cdata-tags    Preserve CDATA tags.  Default: False
    --cleanup-name-list=<replacement-map>
                             Specifies list of 2-tuples used for cleaning
                             names.  First element is a regular expression
                             search pattern and second is a replacement.
                             Example: "[('[-:.]', '_'), ('^__', 'Special')]"
                             Default: "[('[-:.]', '_')]"
    --mixed-case-enums       If used, do not uppercase simpleType enums names.
                             Default is to make enum names uppercase.
    --create-mandatory-children
                             If a child is defined with minOccurs="1" and
                             maxOccurs="1" and the child is xs:complexType
                             and the child is not defined with
                             xs:simpleContent, then in the element's
                             constructor generate code that automatically
                             creates an instance of the child.  The default
                             is False, i.e. do not automatically create child.
    --import-path="string"   This value will be pre-pended to the name of
                             files to be imported by the generated module.
                             The default value is the empty string ("").
                             This option enables the user to produce relative
                             import statements in the generated module that
                             restrict the import to some module in a
                             specific package in a package directory
                             structure containing the generated module.
    -q, --no-questions       Do not ask questions, for example,
                             force overwrite.
    --no-warnings            Do not print warning messages.
    --session=mysession.session
                             Load and use options from session file. You can
                             create session file in generateds_gui.py.  Or,
                             copy and edit sample.session from the
                             distribution.
    --fix-type-names="oldname1:newname1;oldname2:newname2;..."
                             Fix up (replace) complex type names.
    --version                Print version and exit.

Usage example:

    $ python generateDS.py -f -o sample_lib.py sample_api.xsd

creates (with force over-write) sample_lib.py from sample_api.xsd.

    $ python generateDS.py -o sample_lib.py -s sample_app1.py \\
            --member-specs=dict sample_api.xsd

creates sample_lib.py superclass and sample_app1.py subclass modules;
also generates member specifications in each class (in a dictionary).

"""


## LICENSE

## Copyright (c) 2003 Dave Kuhlman

## Permission is hereby granted, free of charge, to any person obtaining
## a copy of this software and associated documentation files (the
## "Software"), to deal in the Software without restriction, including
## without limitation the rights to use, copy, modify, merge, publish,
## distribute, sublicense, and/or sell copies of the Software, and to
## permit persons to whom the Software is furnished to do so, subject to
## the following conditions:

## The above copyright notice and this permission notice shall be
## included in all copies or substantial portions of the Software.

## THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND,
## EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF
## MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT.
## IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY
## CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT,
## TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE
## SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.


from __future__ import print_function
from six.moves import input
import requests
import six
import sys
import os.path
import time
import getopt
from xml.sax import handler, make_parser
import logging
import keyword
import hashlib
import operator
import re
import decimal as decimal_
import io
import pprint
import argparse
import json

if sys.version_info.major == 2:
    import StringIO
    import imp
else:
    from functools import reduce
    import importlib
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError

_log = logging.getLogger(__name__)


## import warnings
## warnings.warn('importing IPShellEmbed', UserWarning)
## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\\nHit Ctrl-D to exit')


#
# Global variables etc.
#

#
# Do not modify the following VERSION comments.
# Used by updateversion.py.
##VERSION##
VERSION = '2.40.8'
##VERSION##

BaseStrTypes = six.string_types
GenerateProperties = 0
UseGetterSetter = 'new'
UseOldSimpleTypeValidators = False
UseGeneratedssuperLookup = True
GDSImportPath = ''
SchemaLxmlTree = None
SchemaLxmlTreeMap = None
SchemaRenameMap = None
XsdFileName = []
MemberSpecs = None
DelayedElements = set()
DelayedElements_subclass = set()
AlreadyGenerated = set()
AlreadyGenerated_subclass = set()
PostponedExtensions = []
LoopcheckOneperChecksums = set()
ElementsForSubclasses = []
ElementDict = {}
fqnToElementDict = {}
fqnToModuleNameMap = {}
AllGeneratedClassNames = set()
Force = False
NoQuestions = False
NoDates = False
NoVersion = False
AlwaysExportDefault = False
CreateMandatoryChildren = False
Dirpath = []
ExternalEncoding = ''
Namespacedef = ''
NoNameSpaceDefs = False
CleanupNameList = [(re.compile('[-:.]'), '_')]
PythonIdentifierRegex = re.compile('^[_A-Za-z][_A-Za-z0-9]*$')
UppercaseEnums = True
NameSeparationRegexList = [
    re.compile("(.)([A-Z][a-z]+)"),
    re.compile("(.)([0-9]+)"),
    re.compile("([0-9])([a-zA-Z])"),
    re.compile("([a-z])([A-Z])")
]
NonAlphaNumRegex = re.compile(r"\W+")

NamespacesDict = {}
SchemaNamespaceDict = {}
prefixToNamespaceMap = {}
MappingTypes = {}
Targetnamespace = ""
NamespaceToCustomImportPath = {}

NameTable = {
    'type': 'type_',
    'float': 'float_',
    'build': 'build_',
    'range': 'range_',
    'set': 'set_',
}
for kw in keyword.kwlist:
    NameTable[kw] = '%s_' % kw


SubclassSuffix = 'Sub'
RootElement = None
AttributeGroups = {}
ElementGroups = {}
SubstitutionGroups = {}
#
# SubstitutionGroups can also include simple types that are
#   not (defined) elements.  Keep a list of these simple types.
#   These are simple types defined at top level.
SimpleElementDict = {}
SimpleTypeDict = {}
ValidatorBodiesBasePath = None
UserMethodsPath = None
UserMethodsModule = None
XsdNameSpace = ''
AnyTypeIdentifier = '__ANY__'
ExportWrite = True
ExportEtree = False
GenerateValidatorMethods = False
GenerateRecursiveGenerator = False
ExportLiteral = False
ExportDjango = False
ExportSQLAlchemy = False
XmlDisabled = False
UseSlots = False
FixTypeNames = None
SingleFileOutput = True
UseSourceFileAsModuleName = False
OutputDirectory = None
ModuleSuffix = ""
PreserveCdataTags = False
NoWarnings = False

SchemaToPythonTypeMap = {}

# Initialize constants.
CurrentNamespacePrefix = None
StringType = None
TokenType = None
IntegerType = None
DecimalType = None
PositiveIntegerType = None
NegativeIntegerType = None
NonPositiveIntegerType = None
NonNegativeIntegerType = None
BooleanType = None
FloatType = None
DoubleType = None
NumericTypes = None
ElementType = None
ComplexTypeType = None
GroupType = None
SequenceType = None
HexBinaryType = None
ChoiceType = None
AttributeGroupType = None
AttributeType = None
SchemaType = None
DateTimeType = None
DateType = None
TimeType = None
GYearType = None
GYearMonthType = None
GMonthType = None
GMonthDayType = None
GDayType = None
DateTimeGroupType = None
SimpleContentType = None
ComplexContentType = None
ExtensionType = None
IDType = None
IDREFType = None
IDREFSType = None
IDTypes = None
NameType = None
NCNameType = None
QNameType = None
NameTypes = None
AnyAttributeType = None
SimpleTypeType = None
RestrictionType = None
WhiteSpaceType = None
ListType = None
EnumerationType = None
UnionType = None
AnyType = None
AnnotationType = None
DocumentationType = None
OtherSimpleTypes = None
Base64Type = None


def set_type_constants(nameSpace):
    global CurrentNamespacePrefix, \
        StringType, TokenType, \
        IntegerType, DecimalType, \
        PositiveIntegerType, NegativeIntegerType, \
        NonPositiveIntegerType, NonNegativeIntegerType, \
        BooleanType, FloatType, DoubleType, \
        NumericTypes, HexBinaryType, \
        ElementType, ComplexTypeType, GroupType, SequenceType, ChoiceType, \
        AttributeGroupType, AttributeType, SchemaType, \
        DateTimeType, DateType, TimeType, \
        DateTimeGroupType, Date_Time_DateTime_Type, \
        GYearType, GYearMonthType, GMonthType, GMonthDayType, GDayType, \
        SimpleContentType, ComplexContentType, ExtensionType, \
        IDType, IDREFType, IDREFSType, IDTypes, \
        NameType, NCNameType, QNameType, NameTypes, \
        AnyAttributeType, SimpleTypeType, RestrictionType, \
        WhiteSpaceType, ListType, EnumerationType, UnionType, \
        Base64Type, AnyType, \
        AnnotationType, DocumentationType, \
        OtherSimpleTypes
    CurrentNamespacePrefix = nameSpace
    AttributeGroupType = nameSpace + 'attributeGroup'
    AttributeType = nameSpace + 'attribute'
    BooleanType = nameSpace + 'boolean'
    ChoiceType = nameSpace + 'choice'
    SimpleContentType = nameSpace + 'simpleContent'
    ComplexContentType = nameSpace + 'complexContent'
    ComplexTypeType = nameSpace + 'complexType'
    GroupType = nameSpace + 'group'
    SimpleTypeType = nameSpace + 'simpleType'
    RestrictionType = nameSpace + 'restriction'
    WhiteSpaceType = nameSpace + 'whiteSpace'
    AnyAttributeType = nameSpace + 'anyAttribute'
    DateTimeType = nameSpace + 'dateTime'
    TimeType = nameSpace + 'time'
    DateType = nameSpace + 'date'
    GYearType = nameSpace + 'gYear'
    GYearMonthType = nameSpace + 'gYearMonth'
    GMonthType = nameSpace + 'gMonth'
    GMonthDayType = nameSpace + 'gMonthDay'
    GDayType = nameSpace + 'gDay'
    DateTimeGroupType = (
        DateTimeType, DateType, TimeType,
        GYearType, GYearMonthType, GMonthType, GMonthDayType, GDayType,
    )
    Date_Time_DateTime_Type = (
        DateTimeType, DateType, TimeType,
    )
    IntegerType = (
        nameSpace + 'integer',
        nameSpace + 'unsignedShort',
        nameSpace + 'unsignedLong',
        nameSpace + 'unsignedInt',
        nameSpace + 'unsignedByte',
        nameSpace + 'byte',
        nameSpace + 'short',
        nameSpace + 'long',
        nameSpace + 'int',
    )
    DecimalType = nameSpace + 'decimal'
    PositiveIntegerType = nameSpace + 'positiveInteger'
    NegativeIntegerType = nameSpace + 'negativeInteger'
    NonPositiveIntegerType = nameSpace + 'nonPositiveInteger'
    NonNegativeIntegerType = nameSpace + 'nonNegativeInteger'
    DoubleType = nameSpace + 'double'
    ElementType = nameSpace + 'element'
    ExtensionType = nameSpace + 'extension'
    FloatType = nameSpace + 'float'
    IDREFSType = nameSpace + 'IDREFS'
    IDREFType = nameSpace + 'IDREF'
    IDType = nameSpace + 'ID'
    IDTypes = (IDREFSType, IDREFType, IDType, )
    SchemaType = nameSpace + 'schema'
    SequenceType = nameSpace + 'sequence'
    HexBinaryType = nameSpace + 'hexBinary'
    # The firist item in this tuple is special.
    # It's the primary string type and must stay in the first position.
    StringType = (
        nameSpace + 'string',
        nameSpace + 'duration',
        nameSpace + 'anyURI',
        nameSpace + 'hexBinary',
        nameSpace + 'normalizedString',
        nameSpace + 'NMTOKEN',
        nameSpace + 'ID',
        nameSpace + 'IDREF',
        nameSpace + 'Name',
        nameSpace + 'NCName',
        nameSpace + 'QName',
        nameSpace + 'language',
    )
    NumericTypes = set([
        IntegerType,
        DecimalType,
        PositiveIntegerType,
        NegativeIntegerType,
        NonPositiveIntegerType,
        NonNegativeIntegerType,
        FloatType,
        DoubleType,
    ])
    NumericTypes.update(set(IntegerType))
    Base64Type = nameSpace + 'base64Binary'
    TokenType = nameSpace + 'token'
    NameType = nameSpace + 'Name'
    NCNameType = nameSpace + 'NCName'
    QNameType = nameSpace + 'QName'
    NameTypes = (NameType, NCNameType, QNameType, )
    ListType = nameSpace + 'list'
    EnumerationType = nameSpace + 'enumeration'
    UnionType = nameSpace + 'union'
    AnnotationType = nameSpace + 'annotation'
    DocumentationType = nameSpace + 'documentation'
    AnyType = nameSpace + 'any'
    OtherSimpleTypes = (
        nameSpace + 'ENTITIES',
        nameSpace + 'ENTITY',
        nameSpace + 'ID',
        nameSpace + 'IDREF',
        nameSpace + 'IDREFS',
        nameSpace + 'NCName',
        nameSpace + 'NMTOKEN',
        nameSpace + 'NMTOKENS',
        nameSpace + 'NOTATION',
        nameSpace + 'Name',
        nameSpace + 'QName',
        nameSpace + 'anyURI',
        nameSpace + 'base64Binary',
        nameSpace + 'hexBinary',
        nameSpace + 'boolean',
        nameSpace + 'byte',
        nameSpace + 'date',
        nameSpace + 'dateTime',
        nameSpace + 'time',
        nameSpace + 'decimal',
        nameSpace + 'double',
        nameSpace + 'duration',
        nameSpace + 'float',
        nameSpace + 'gDay',
        nameSpace + 'gMonth',
        nameSpace + 'gMonthDay',
        nameSpace + 'gYear',
        nameSpace + 'gYearMonth',
        nameSpace + 'int',
        nameSpace + 'integer',
        nameSpace + 'language',
        nameSpace + 'long',
        nameSpace + 'negativeInteger',
        nameSpace + 'nonNegativeInteger',
        nameSpace + 'nonPositiveInteger',
        nameSpace + 'normalizedString',
        nameSpace + 'positiveInteger',
        nameSpace + 'short',
        nameSpace + 'string',
        nameSpace + 'time',
        nameSpace + 'token',
        nameSpace + 'unsignedByte',
        nameSpace + 'unsignedInt',
        nameSpace + 'unsignedLong',
        nameSpace + 'unsignedShort',
        nameSpace + 'anySimpleType',
    )

    global SchemaToPythonTypeMap
    SchemaToPythonTypeMap = {
        BooleanType: 'bool',
        DecimalType: 'float',
        DoubleType: 'float',
        FloatType: 'float',
        NegativeIntegerType: 'int',
        NonNegativeIntegerType: 'int',
        NonPositiveIntegerType: 'int',
        PositiveIntegerType: 'int',
    }
    SchemaToPythonTypeMap.update(dict((x, 'int') for x in IntegerType))

#
# For debugging.
#


# Print only if DEBUG is true.
DEBUG = 0


def dbgprint(level, msg):
    if DEBUG and level > 0:
        print(msg)


def pplist(lst):
    for count, item in enumerate(lst):
        print('%d. %s' % (count, item))


# Provide fake function for Python 3 to satisfy code checker.  Never called.
if sys.version_info.major >= 3:
    def unicode(data):
        return(data)


#
# Representation of element definition.
#

def showLevel(outfile, level):
    for idx in range(level):
        outfile.write('    ')


class XschemaElementBase:
    def __init__(self):
        pass


class SimpleTypeElement(XschemaElementBase):
    def __init__(self, name):
        XschemaElementBase.__init__(self)
        self.name = name
        self.base = None
        self.collapseWhiteSpace = 0
        # Attribute definitions for the current attributeGroup, if
        #   there is one.
        self.attributeGroup = None
        # Attribute definitions for the currect element.
        self.attributeDefs = {}
        self.complexType = 0
        # Enumeration values for the current element.
        self.values = list()
        self.values_documentation = dict()
        # The other simple types this is a union of.
        self.unionOf = list()
        self.simpleType = 0
        self.listType = 0
        self.documentation = ''

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setBase(self, base):
        self.base = base

    def getBase(self):
        return self.base

    def setSimpleType(self, simpleType):
        self.simpleType = simpleType

    def getSimpleType(self):
        return self.simpleType

    def getAttributeGroups(self):
        return self.attributeGroups

    def setAttributeGroup(self, attributeGroup):
        self.attributeGroup = attributeGroup

    def getAttributeGroup(self):
        return self.attributeGroup

    def getEnumValues(self):
        return self.values

    def getEnumValueDocumentation(self, value):
        if value in self.values_documentation:
            return ' '.join(self.values_documentation[value].split())

    def setListType(self, listType):
        self.listType = listType

    def isListType(self):
        return self.listType

    def __str__(self):
        s1 = '<"%s" SimpleTypeElement instance at 0x%x>' % \
            (self.getName(), id(self))
        return s1
    __repr__ = __str__

    def resolve_list_type(self):
        if self.isListType():
            return 1
        elif self.getBase() in SimpleTypeDict:
            base = SimpleTypeDict[self.getBase()]
            return base.resolve_list_type()
        else:
            return 0


class XschemaElement(XschemaElementBase):
    def __init__(self, attrs, targetNamespace=None):
        XschemaElementBase.__init__(self)
        _log.debug(
            "ENTER ctor XschemaElement, attrs=%s, targetNamespace=%s" % (
                repr(attrs.items()), repr(targetNamespace)))
        # may be None, when this class is generated from non-xs:element input
        self.elementFormDefault = attrs.get(
            'form', attrs.get('elementFormDefault'))
        self.attributeFormDefault = attrs.get('attributeFormDefault')
        self.mustOverrideTargetNamespace = False
        if ('mustOverrideTargetNamespace' in attrs.keys() and
                attrs['mustOverrideTargetNamespace'] == 'true'):
            _log.debug('Overriding targetNamespace "%s" to "%s".' % (
                str(targetNamespace), attrs['targetNamespace']))
            targetNamespace = attrs['targetNamespace']
            self.mustOverrideTargetNamespace = True

        self.cleanName = ''
        self.attrs = dict(attrs)
        name_val = ''
        type_val = ''
        ref_val = ''
        self.prefix = None
        self.namespace = None
        self.is_root_element = False
        self.targetNamespace = targetNamespace
        self.fullyQualifiedName = None
        self.fullyQualifiedType = None
        self.type = 'NoneType'

        if 'name' in self.attrs:
            self.prefix, name_val = get_prefix_and_value(self.attrs['name'])
            self.fullyQualifiedName = (
                "%s:%s" % (targetNamespace, name_val) if targetNamespace
                else name_val)

        if 'type' in self.attrs:
            if (len(XsdNameSpace) > 0 and
                    self.attrs['type'].startswith(XsdNameSpace)):
                type_val = self.attrs['type']
            else:
                self.prefix, type_val = get_prefix_and_value(
                    self.attrs['type'])
                self.type = type_val
        if 'ref' in self.attrs:
            self.prefix, ref_val = get_prefix_and_value(self.attrs['ref'])
            if self.prefix in prefixToNamespaceMap:
                xmlns = prefixToNamespaceMap[self.prefix]
                fqn = "%s:%s" % (xmlns, ref_val)
                if fqn in fqnToElementDict:
                    referencedElement = fqnToElementDict[fqn]
                    type_val = referencedElement.getType()
                    if type_val == "NoneType":
                        # anonymous types
                        type_val = referencedElement.getName()
                    name_val = ref_val
            if not type_val:
                type_val = ref_val

        if type_val and not name_val:
            name_val = type_val
        if ref_val and not name_val:
            name_val = ref_val
        if ref_val and not type_val:
            type_val = ref_val
        if name_val:
            self.attrs['name'] = name_val
        if type_val:
            self.attrs['type'] = type_val
        if ref_val:
            self.attrs['ref'] = ref_val
        # fix_abstract
        abstract_type = attrs.get('abstract', 'false').lower()
        self.abstract_type = abstract_type in ('1', 'true')
        self.default = self.attrs.get('default')
        self.name = name_val
        self.children = []
        self.optional = False
        self.minOccurs = 1
        self.maxOccurs = 1
        self.complex = 0
        self.complexType = 0
        self.mixed = 0
        self.base = None
        self.mixedExtensionError = 0
        self.collapseWhiteSpace = 0
        # Attribute definitions for the currect element.
        self.attributeDefs = {}
        # Use this to maintain predictable order of attributes.
        self.attributeDefsList = []
        # Attribute definitions for the current attributeGroup, if
        #   there is one.
        self.attributeGroup = None
        # List of names of attributes for this element.
        # We will add the attribute defintions in each of these groups
        #   to this element in annotate().
        self.attributeGroupNameList = []
        # similar things as above, for groups of elements
        self.elementGroup = None
        self.topLevel = 0
        # Does this element contain an anyAttribute?
        self.anyAttribute = 0
        self.explicit_define = 0
        self.simpleType = None
        # Enumeration values for the current element.
        self.values = list()
        self.values_documentation = dict()
        # The parent choice for the current element.
        self.choice = None
        self.choiceGroup = None
        self.listType = 0
        self.simpleBase = []
        self.documentation = ''
        self.restrictionBase = None
        self.simpleContent = False
        self.extended = False
        _log.debug(
            'LEAVE, XSchemaElement "%s" complete, state: %s',
            self.name,
            repr(self.__dict__))

    def addChild(self, element):
        self.children.append(element)

    def getChildren(self):
        return self.children

    def getName(self):
        return self.name

    def getFullyQualifiedName(self):
        return self.fullyQualifiedName

    def getFullyQualifiedType(self):
        typeName = self.type
        if not typeName or typeName == "NoneType":
            typeName = self.name
        if typeName and not self.fullyQualifiedType:
            namespace = self.targetNamespace
            if self.prefix and self.prefix in prefixToNamespaceMap:
                xmlns = prefixToNamespaceMap[self.prefix]
                if xmlns:
                    namespace = xmlns
            self.fullyQualifiedType = "%s:%s" % (namespace, typeName)

        return self.fullyQualifiedType

    def getCleanName(self):
        return self.cleanName

    def getUnmappedCleanName(self):
        return self.unmappedCleanName

    def setName(self, name):
        self.name = name

    def getAttrs(self):
        return self.attrs

    def setAttrs(self, attrs):
        self.attrs = attrs

    def getChoiceGroup(self):
        return self.choiceGroup

    def setChoiceGroup(self, groupId):
        self.choiceGroup = groupId

    def getMinOccurs(self):
        return self.minOccurs

    def getMaxOccurs(self):
        return self.maxOccurs

    def getOptional(self):
        return self.optional

    def getRawType(self):
        return self.type

    def setExplicitDefine(self, explicit_define):
        self.explicit_define = explicit_define

    def isExplicitDefine(self):
        return self.explicit_define

    def isAbstract(self):
        return self.abstract_type

    def setListType(self, listType):
        self.listType = listType

    def isListType(self):
        return self.listType

    def getType(self):
        returnType = self.type
        if self.type in ElementDict:
            typeObj = ElementDict[self.type]
            typeObjType = typeObj.getRawType()
            if is_builtin_simple_type(typeObjType):
                returnType = typeObjType
        return returnType

    def isComplex(self):
        return self.complex

    def setIsRootElement(self, is_root_elem):
        self.is_root_element = is_root_elem

    def isRootElement(self):
        return self.is_root_element

    def getAttributeDefs(self):
        return self.attributeDefs

    def getAttributeDefsList(self):
        return self.attributeDefsList

    def isMixed(self):
        return self.mixed

    def setMixed(self, mixed):
        self.mixed = mixed

    def setBase(self, base):
        self.base = base

    def getBase(self):
        return self.base

    def getMixedExtensionError(self):
        return self.mixedExtensionError

    def getAttributeGroups(self):
        return self.attributeGroups

    def addAttribute(self, name, attribute):
        self.attributeGroups[name] = attribute

    def setAttributeGroup(self, attributeGroup):
        self.attributeGroup = attributeGroup

    def getAttributeGroup(self):
        return self.attributeGroup

    def setElementGroup(self, elementGroup):
        self.elementGroup = elementGroup

    def getElementGroup(self):
        return self.elementGroup

    def setTopLevel(self, topLevel):
        self.topLevel = topLevel

    def getTopLevel(self):
        return self.topLevel

    def setAnyAttribute(self, anyAttribute):
        self.anyAttribute = anyAttribute

    def getAnyAttribute(self):
        return self.anyAttribute

    def setSimpleType(self, simpleType):
        self.simpleType = simpleType

    def getSimpleType(self):
        return self.simpleType

    def setDefault(self, default):
        self.default = default

    def getDefault(self):
        return self.default

    def getSimpleBase(self):
        return self.simpleBase

    def setSimpleBase(self, simpleBase):
        self.simpleBase = simpleBase

    def addSimpleBase(self, simpleBase):
        self.simpleBase.append(simpleBase)

    def getRestrictionBase(self):
        return self.restrictionBase

    def setRestrictionBase(self, base):
        self.restrictionBase = base

    def getRestrictionBaseObj(self):
        rBaseObj = None
        rBaseName = self.getRestrictionBase()
        if rBaseName and rBaseName in ElementDict:
            rBaseObj = ElementDict[rBaseName]
        return rBaseObj

    def setSimpleContent(self, simpleContent):
        self.simpleContent = simpleContent

    def getSimpleContent(self):
        return self.simpleContent

    def getExtended(self):
        return self.extended

    def setExtended(self, extended):
        self.extended = extended

    def show(self, outfile, level):
        if self.name == 'Reference':
            showLevel(outfile, level)
            outfile.write('Name: %s  Type: %s  id: %d\n' % (
                self.name, self.getType(), id(self),))
            showLevel(outfile, level)
            outfile.write('  - Complex: %d  MaxOccurs: %d  '
                          'MinOccurs: %d\n' % (
                              self.complex, self.maxOccurs, self.minOccurs))
            showLevel(outfile, level)
            outfile.write('  - Attrs: %s\n' % self.attrs)
            showLevel(outfile, level)
            #outfile.write('  - AttributeDefs: %s\n' % self.attributeDefs)
            outfile.write('  - AttributeDefs:\n')
            for key, value in self.getAttributeDefs().items():
                showLevel(outfile, level + 1)
                outfile.write('- key: %s  value: %s\n' % (key, value, ))
        for child in self.children:
            child.show(outfile, level + 1)

    def annotate(self):
        # resolve group references within groups
        for grp in ElementGroups.values():
            expandGroupReferences(grp)
        # Recursively expand group references
        visited = set()
        self.expandGroupReferences_tree(visited)
        already_seen = set()
        self.collect_element_dict(already_seen)
        already_seen = set()
        self.annotate_find_type(already_seen)
        element_dict = None
        to_be_removed = None
        already_seen = set()
        self.annotate_tree(
            element_dict=element_dict,
            to_be_removed=to_be_removed,
            already_seen=already_seen)
        already_seen = set()
        self.fix_dup_names(already_seen)
        already_seen = set()
        self.coerce_attr_types(already_seen)
        already_seen = set()
        self.checkMixedBases(already_seen)
        already_seen = set()
        self.markExtendedTypes(already_seen)
        self.raiseDocStrings()

    #
    # The documentation strings for some child elements were possibly
    # attached to the child, instead of to the complexType that contains them.
    # Move them up to the container so that the doc strings will be
    # generated in the containing Python class.
    def raiseDocStrings(self):
        if self.isComplex():
            for child in self.children:
                if child.documentation:
                    self.documentation += child.documentation
                    child.documentation = ''
        for child in self.children:
            child.raiseDocStrings()

    def markExtendedTypes(self, already_seen):
        if self in already_seen:
            return
        already_seen.add(self)
        base = self.getBase()
        if base and base in ElementDict:
            parent = ElementDict[base]
            parent.setExtended(True)
        for child in self.children:
            child.markExtendedTypes(already_seen)

    def expandGroupReferences_tree(self, visited):
        if self.getName() in visited:
            return
        visited.add(self.getName())
        expandGroupReferences(self)
        for child in self.children:
            child.expandGroupReferences_tree(visited)

    def collect_element_dict(self, already_seen):
        if self in already_seen:
            return
        already_seen.add(self)
        base = self.getBase()
        if (self.getTopLevel() or len(self.getChildren()) > 0 or
                len(self.getAttributeDefs()) > 0 or base):
            ElementDict[self.name] = self
        for child in self.children:
            child.collect_element_dict(already_seen)

    def build_element_dict(self, elements):
        base = self.getBase()
        if (self.getTopLevel() or len(self.getChildren()) > 0 or
                len(self.getAttributeDefs()) > 0 or base):
            if self.name not in elements:
                elements[self.name] = self
        for child in self.children:
            child.build_element_dict(elements)

    def get_element(self, element_name):
        if self.element_dict is None:
            self.element_dict = dict()
            self.build_element_dict(self.element_dict)
        return self.element_dict.get(element_name)

    # If it is a mixed-content element and it is defined as
    #   an extension, then all of its bases (base, base of base, ...)
    #   must be mixed-content.  Mark it as an error, if not.
    def checkMixedBases(self, already_seen):
        if self in already_seen:
            return
        already_seen.add(self)
        self.rationalizeMixedBases()
        self.collectSimpleBases()
        self.checkMixedBasesChain(self, self.mixed)
        for child in self.children:
            child.checkMixedBases(already_seen)

    def collectSimpleBases(self):
        if self.base:
            self.addSimpleBase(version_py2_encode(self.base))
        if self.simpleBase:
            base1 = SimpleTypeDict.get(self.simpleBase[0])
            if base1:
                base2 = base1.base or None
            else:
                base2 = None
            while base2:
                self.addSimpleBase(version_py2_encode(base2))
                base2 = SimpleTypeDict.get(base2)
                if base2:
                    base2 = base2.getBase()

    def rationalizeMixedBases(self):
        mixed = self.hasMixedInChain()
        if mixed:
            self.equalizeMixedBases()

    def hasMixedInChain(self):
        if self.isMixed():
            return True
        base = self.getBase()
        if base and base in ElementDict:
            parent = ElementDict[base]
            return parent.hasMixedInChain()
        else:
            return False

    def equalizeMixedBases(self):
        if not self.isMixed():
            self.setMixed(True)
        base = self.getBase()
        if base and base in ElementDict:
            parent = ElementDict[base]
            parent.equalizeMixedBases()

    def checkMixedBasesChain(self, child, childMixed):
        base = self.getBase()
        if base and base in ElementDict:
            parent = ElementDict[base]
            if childMixed != parent.isMixed():
                self.mixedExtensionError = 1
                return
            parent.checkMixedBasesChain(child, childMixed)

    def resolve_type(self):
        self.complex = 0
        # If it has any attributes, then it's complex.
        attrDefs = self.getAttributeDefs()
        if len(attrDefs) > 0:
            self.complex = 1
            # type_val = ''
        type_val = self.resolve_type_1()
        if type_val == AnyType:
            return AnyType
        if type_val in SimpleTypeDict:
            self.addSimpleBase(version_py2_encode(type_val))
            simple_type = SimpleTypeDict[type_val]
            list_type = simple_type.resolve_list_type()
            self.setListType(list_type)
        if type_val:
            if type_val in ElementDict:
                type_val1 = type_val
                # The following loop handles the case where an Element's
                # reference element has no sub-elements and whose type is
                # another simpleType (potentially of the same name). Its
                # fundamental function is to avoid the incorrect
                # categorization of "complex" to Elements which are not and
                # correctly resolve the Element's type as well as its
                # potential values. It also handles cases where the Element's
                # "simpleType" is so-called "top level" and is only available
                # through the global SimpleTypeDict.
                i = 0
                while True:
                    element = ElementDict[type_val1]
                    # Resolve our potential values if present
                    self.values = element.values
                    # If the type is available in the SimpleTypeDict, we
                    # know we've gone far enough in the Element hierarchy
                    # and can return the correct base type.
                    t = element.resolve_type_1()
                    if t in SimpleTypeDict:
                        type_val1 = SimpleTypeDict[t].getBase()
                        if type_val1 and not is_builtin_simple_type(type_val1):
                            type_val1 = strip_namespace(type_val1)
                        break
                    # If the type name is the same as the previous type name
                    # then we know we've fully resolved the Element hierarchy
                    # and the Element is well and truely "complex". There is
                    # also a need to handle cases where the Element name and
                    # its type name are the same (ie. this is our first time
                    # through the loop). For example:
                    #   <xsd:element name="ReallyCool" type="ReallyCool"/>
                    #   <xsd:simpleType name="ReallyCool">
                    #     <xsd:restriction base="xsd:string">
                    #       <xsd:enumeration value="MyThing"/>
                    #     </xsd:restriction>
                    #   </xsd:simpleType>
                    if t == type_val1 and i != 0:
                        break
                    if t not in ElementDict:
                        type_val1 = t
                        break
                    type_val1 = t
                    i += 1
                if is_builtin_simple_type(type_val1):
                    type_val = type_val1
                else:
                    self.complex = 1
            elif type_val in SimpleTypeDict:
                type_val, _ = resolveBaseTypeForSimpleType(type_val)
                # Add the namespace prefix to the simple type if needed.
                if len(type_val.split(':')) == 1:
                    type_val = CurrentNamespacePrefix + type_val
            else:
                if is_builtin_simple_type(type_val):
                    pass
                else:
                    type_val = StringType[0]
        else:
            type_val = StringType[0]
        return type_val

    def resolve_type_1(self):
        type_val = ''
        if 'type' in self.attrs:
            type_val = self.attrs['type']
            if type_val in SimpleTypeDict:
                self.simpleType = type_val
        elif 'ref' in self.attrs:
            type_val = strip_namespace(self.attrs['ref'])
        elif 'name' in self.attrs:
            type_val = strip_namespace(self.attrs['name'])
            #type_val = self.attrs['name']
        return type_val

    def annotate_find_type(self, already_seen):
        if self in already_seen:
            return
        already_seen.add(self)
        if self.type == AnyTypeIdentifier:
            pass
        else:
            type_val = self.resolve_type()
            self.attrs['type'] = type_val
            self.type = type_val
            self.fullyQualifiedType = None
        if not self.complex:
            SimpleElementDict[self.name] = self
        for child in self.children:
            child.annotate_find_type(already_seen)

    def annotate_tree(self, element_dict, to_be_removed, already_seen):
        if self in already_seen:
            self.remove_children(to_be_removed)
            return
        already_seen.add(self)
        name = self.getName()
        if element_dict is not None:
            dup_element = element_dict.get(name)
            if (dup_element is not None and
                    # The element_dict keys are the element name.
                    # So, we do not need to compare names.
                    #dup_element.getName() == name and
                    not self.complexType and
                    not dup_element.complexType):
                # If we've already seen this element (name), and
                # these are both xsd:complexType, then
                # make it a list and throw the previous one away.
                self.maxOccurs = 2
                to_be_removed.append(element_dict[name])
                err_msg(
                    '*** warning.  Removing child with duplicate '
                    'name: "{}"\n'.format(name))
            else:
                element_dict[name] = self
        # If there is a namespace, replace it with an underscore.
        if self.base:
            self.base = strip_namespace(self.base)
        self.unmappedCleanName = cleanupName(self.name)
        self.cleanName = mapName(self.unmappedCleanName)
        self.replace_attributeGroup_names()
        # Resolve "maxOccurs" attribute
        if 'maxOccurs' in self.attrs.keys():
            maxOccurs = self.attrs['maxOccurs']
        else:
            maxOccurs = 1
        if self.choice and 'maxOccurs' in self.choice.attrs.keys():
            # If maxOccurs in enclosing xs:choice is > 1, override this one.
            if (self.choice.attrs['maxOccurs'] != '0' and
                    self.choice.attrs['maxOccurs'] != '1'):
                maxOccurs = self.choice.attrs['maxOccurs']
        # Resolve "minOccurs" attribute
        if 'minOccurs' in self.attrs.keys():
            minOccurs = self.attrs['minOccurs']
        elif self.choice and 'minOccurs' in self.choice.attrs.keys():
            minOccurs = self.choice.attrs['minOccurs']
        else:
            minOccurs = 1
        # Cleanup "minOccurs" and "maxOccurs" attributes
        try:
            minOccurs = int(minOccurs)
            if minOccurs == 0:
                self.optional = True
        except ValueError:
            err_msg('*** %s  minOccurs must be integer.\n' % self.getName())
            sys.exit(1)
        try:
            if maxOccurs == 'unbounded':
                maxOccurs = 9999999
            else:
                maxOccurs = int(maxOccurs)
        except ValueError:
            err_msg('*** %s  maxOccurs must be integer or "unbounded".\n' % (
                self.getName(), ))
            sys.exit(1)
        self.minOccurs = minOccurs
        self.maxOccurs = maxOccurs
        # If it does not have a type, then make the type the same as the name.
        if self.type == 'NoneType' and self.name:
            self.type = self.name
        # Is it a mixed-content element definition?
        if 'mixed' in self.attrs.keys():
            mixed = self.attrs['mixed'].strip()
            if mixed == '1' or mixed.lower() == 'true':
                self.mixed = 1
        # If this element has a base and the base is a simple type and
        #   the simple type is collapseWhiteSpace, then mark this
        #   element as collapseWhiteSpace.
        base = self.getBase()
        if base and base in SimpleTypeDict:
            parent = SimpleTypeDict[base]
            if (isinstance(parent, SimpleTypeElement) and
                    parent.collapseWhiteSpace):
                self.collapseWhiteSpace = 1
        # Do it recursively for all descendents.
        element_dict = {}
        to_be_removed = []
        for child in self.children:
            child.annotate_tree(
                element_dict=element_dict,
                to_be_removed=to_be_removed,
                already_seen=already_seen)
        self.remove_children(to_be_removed)

    def remove_children(self, to_be_removed):
        for element in to_be_removed:
            if element in self.children:
                self.children.remove(element)
            else:
                err_msg("*** warning.  child {} already removed\n".format(
                    element.getName()))

    #
    # For each name in the attributeGroupNameList for this element,
    #   add the attributes defined for that name in the global
    #   attributeGroup dictionary.
    # We do this recursively because an attribute group can reference
    #   other attribute groups.
    def replace_attributeGroup_names(self):
        for groupName in self.attributeGroupNameList:
            self.replace_attributeGroup_names_1(groupName)

    def replace_attributeGroup_names_1(self, groupName):
        key = None
        if groupName in AttributeGroups:
            key = groupName
        else:
            # Looking for name space prefix
            key1 = strip_namespace(groupName)
            if key1 != groupName and key1 in AttributeGroups:
                key = key1
        if key is not None:
            attrGroup = AttributeGroups[key]
            for name in attrGroup.getKeys():
                group = attrGroup.get(name)
                # If group is none, then it's an attributeGroup,
                # not an attribute.
                # Therefore, we might need to follow it recursively.
                if (group is None and
                        (name in AttributeGroups or
                            strip_namespace(name) in AttributeGroups)):
                    self.replace_attributeGroup_names_1(name)
                else:
                    attr = attrGroup.get(name)
                    self.attributeDefs[name] = attr
                    self.attributeDefsList.append(name)
        else:
            err_msg('*** Error. Element %s attributeGroup %s '
                    'not defined.\n' % (
                        self.getName(), groupName, ))

    def __str__(self):
        s1 = '<XschemaElement name: "%s" type: "%s">' % \
            (self.getName(), self.getType(), )
        return s1
    __repr__ = __str__

    def fix_dup_names(self, already_seen):
        # Patch-up names that are used for both a child element and
        #   an attribute.
        #
        if self in already_seen:
            return
        already_seen.add(self)
        attrDefs = self.getAttributeDefs()
        attrDefsList = self.getAttributeDefsList()
        # Collect a list of child element names.
        #   Must do this for base (extension) elements also.
        elementNames = set()
        self.collectElementNames(elementNames, 0)
        replaced = []
        # Create the needed new attributes.
        keys = attrDefs.keys()
        for key in keys:
            attr = attrDefs[key]
            name = attr.getName()
            mappedName = mapName(name)
            if mappedName in elementNames:
                newName = mappedName + '_attr'
                if hasattr(attr, 'fixed'):
                    fixed = attr.fixed
                else:
                    fixed = None
                newAttr = XschemaAttribute(
                    name=newName,
                    data_type=attr.data_type,
                    use=attr.use,
                    default=attr.default,
                    fixed=fixed
                )
                newAttr.setOrig_name(name)
                replaced.append((name, newName, newAttr))
        # Remove the old (replaced) attributes.
        for name, newName, newAttr in replaced:
            del attrDefs[name]
            attrDefs[newName] = newAttr
            try:
                attrDefsList[attrDefsList.index(name)] = newName
            except ValueError:
                pass
        for child in self.children:
            child.fix_dup_names(already_seen)

    def collectElementNames(self, elementNames, count):
        for child in self.children:
            elementNames.add(child.getCleanName())
        base = self.getBase()
        if base and base in ElementDict:
            parent = ElementDict[base]
            count += 1
            if count > 100:
                msg = 'Extension/restriction recursion detected.  ' \
                    'Suggest you check definitions of types ' \
                    '%s and %s.'
                msg = msg % (self.getName(), parent.getName(), )
                raise RuntimeError(msg)
            parent.collectElementNames(elementNames, count)

    def coerce_attr_types(self, already_seen):
        if self in already_seen:
            return
        already_seen.add(self)
        attrDefs = self.getAttributeDefs()
        for idx, name in enumerate(attrDefs):
            attr = attrDefs[name]
            attrType = attr.getData_type()
            if (attrType == IDType or
                    attrType == IDREFType or
                    attrType == IDREFSType):
                attr.setData_type(StringType[0])
        for child in self.children:
            child.coerce_attr_types(already_seen)
# end class XschemaElement


class XschemaAttributeGroup:
    def __init__(self, name='', group=None, keyList=None):
        self.name = name
        if group:
            self.group = group
        else:
            self.group = {}
        if keyList is not None:
            self.keyList = keyList
        else:
            self.keyList = []

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setGroup(self, group):
        self.group = group

    def getGroup(self):
        return self.group

    def get(self, name, default=None):
        if name in self.group:
            return self.group[name]
        else:
            return default

    def getKeys(self):
        return self.keyList

    def add(self, name, attr):
        self.group[name] = attr
        self.keyList.append(name)

    def delete(self, name):
        if name in self.group:
            del self.group[name]
            self.keyList.remove(name)
            return 1
        else:
            return 0
# end class XschemaAttributeGroup


class XschemaGroup:
    def __init__(self, ref):
        self.ref = ref
# end class XschemaGroup


class XschemaAttribute:
    def __init__(
            self,
            name,
            data_type=None,
            use='optional',
            default=None,
            fixed=None):
        self.name = name
        if data_type is None:
            self.data_type = StringType[0]
        else:
            self.data_type = data_type
        self.use = use
        self.default = default
        # treat `fixed` the same as `default`.
        if fixed is not None:
            self.default = fixed
        # Enumeration values for the attribute.
        self.values = list()
        # If we change the name, e.g. because an attribute and child have
        # the same name, save the old name here.
        self.orig_name = None
        self.fully_qualified_name = None

    def setName(self, name):
        self.name = name

    def getName(self):
        return self.name

    def setData_type(self, data_type):
        self.data_type = data_type

    def getData_type(self):
        return self.data_type

    def getFullyQualifiedTypeName(self):
        returnType = self.getType()
        if is_builtin_simple_type(returnType):
            return returnType
        prefix, value = get_prefix_and_value(self.data_type)
        if prefix is not None:
            return prefixToNamespaceMap[prefix] + ":" + value
        return returnType

    def getType(self):
        returnType = self.data_type
        if self.data_type in SimpleElementDict:
            typeObj = SimpleElementDict[self.data_type]
            typeObjType = typeObj.getRawType()

##        if self.data_type in SimpleElementDict:
##            typeObj = SimpleElementDict[self.data_type]
##            typeObjType = typeObj.getRawType()

##        if strip_namespace(self.data_type) in SimpleTypeDict:
##            typeObj = SimpleTypeDict[strip_namespace(self.data_type)]
##            typeObjType = typeObj.getBase()

            if (typeObjType in StringType or
                    typeObjType == TokenType or
                    typeObjType in DateTimeGroupType or
                    typeObjType == Base64Type or
                    typeObjType in IntegerType or
                    typeObjType == DecimalType or
                    typeObjType == PositiveIntegerType or
                    typeObjType == NegativeIntegerType or
                    typeObjType == NonPositiveIntegerType or
                    typeObjType == NonNegativeIntegerType or
                    typeObjType == BooleanType or
                    typeObjType == FloatType or
                    typeObjType == DoubleType):
                returnType = typeObjType
        return returnType

    def getBaseType(self):
        returnType = self.data_type
##        if self.data_type in SimpleElementDict:
##            typeObj = SimpleElementDict[self.data_type]
##            typeObjType = typeObj.getRawType()

##        if self.data_type in SimpleElementDict:
##            typeObj = SimpleElementDict[self.data_type]
##            typeObjType = typeObj.getRawType()

        if strip_namespace(self.data_type) in SimpleTypeDict:
            typeObj = SimpleTypeDict[strip_namespace(self.data_type)]
            typeObjType = typeObj.getBase()

            if (typeObjType in StringType or
                    typeObjType == TokenType or
                    typeObjType in DateTimeGroupType or
                    typeObjType == Base64Type or
                    typeObjType in IntegerType or
                    typeObjType == DecimalType or
                    typeObjType == PositiveIntegerType or
                    typeObjType == NegativeIntegerType or
                    typeObjType == NonPositiveIntegerType or
                    typeObjType == NonNegativeIntegerType or
                    typeObjType == BooleanType or
                    typeObjType == FloatType or
                    typeObjType == DoubleType):
                returnType = typeObjType
        return returnType

    def setUse(self, use):
        self.use = use

    def getUse(self):
        return self.use

    def setDefault(self, default):
        self.default = default

    def getDefault(self):
        return self.default

    def setOrig_name(self, orig_name):
        self.orig_name = orig_name

    def getOrig_name(self):
        return self.orig_name
# end class XschemaAttribute


#
# SAX handler
#
class XschemaHandler(handler.ContentHandler):
    def __init__(self):
        handler.ContentHandler.__init__(self)
        self.stack = []
        self.root = None
        self.inElement = 0
        self.inComplexType = 0
        self.inNonanonymousComplexType = 0
        self.inSequence = 0
        self.sequenceStack = []
        self.inChoice = 1
        self.inAttribute = 0
        self.attributeGroupLevel = 0
        self.inSimpleType = 0
        self.inSimpleContent = 0
        self.inRestrictionType = 0
        self.inAnnotationType = 0
        self.inDocumentationType = 0
        self.inEnumerationType = 0
        # The last attribute we processed.
        self.lastAttribute = None
        # Simple types that exist in the global context and may be used to
        # qualify the type of many elements and/or attributes.
        self.topLevelSimpleTypes = list()
        # The current choice type we're in
        self.currentChoice = None
        self.currentChoiceId = 0
        self.firstElement = True
        self.current_documentation = None
        self.elementStack = []
        self.savedDocString = ""

    def getRoot(self):
        return self.root

    def extractSchemaNamespace(self, attrs):
        schemaUri = 'http://www.w3.org/2001/XMLSchema'
        keys = [x for x, v in attrs.items() if v == schemaUri]
        if not keys:
            return None
        keys = [x[6:] for x in keys if x.startswith('xmlns')]
        if not keys:
            return None
        return keys[0]

    def startElement(self, name, attrs):
        global Targetnamespace, NamespacesDict, XsdNameSpace, fqnToElementDict
        _log.debug("Start element: %s %s", name, repr(attrs.items()))
        if len(self.stack) == 0 and self.firstElement:
            self.firstElement = False
            schemaNamespace = self.extractSchemaNamespace(attrs)
            if schemaNamespace:
                XsdNameSpace = schemaNamespace
                set_type_constants(schemaNamespace + ':')
            else:
                if len(name.split(':')) == 1:
                    XsdNameSpace = ''
                    set_type_constants('')
        if name == SchemaType:
            self.inSchema = 1
            element = XschemaElement(attrs)
            if len(self.stack) == 1:
                element.setTopLevel(1)
            self.stack.append(element)
            # If there is an attribute "xmlns" and its value is
            #   "http://www.w3.org/2001/XMLSchema", then remember and
            #   use that namespace prefix.
            for name, value in attrs.items():
                if name[:6] == 'xmlns:':
                    prefix = name[6:]
                    nameSpace = prefix + ':'
                    NamespacesDict[value] = nameSpace
                    prefixToNamespaceMap[prefix] = value
                elif name == 'targetNamespace':
                    Targetnamespace = value
                    element.targetNamespace = value
        elif (name == ElementType or
                ((name == ComplexTypeType) and (len(self.stack) == 1))):
            self.inElement = 1
            self.inNonanonymousComplexType = 1
            element = XschemaElement(attrs, Targetnamespace)
            fqn = element.getFullyQualifiedName()
            if fqn and name == ComplexTypeType:
                fqnToElementDict[fqn] = element
            if element.prefix in prefixToNamespaceMap:
                element.namespace = prefixToNamespaceMap[element.prefix]
            if self.sequenceStack:
                minOccurs, maxOccurs = self.sequenceStack[-1]
                if 'minOccurs' not in attrs and minOccurs is not None:
                    element.attrs['minOccurs'] = minOccurs
                if 'maxOccurs' not in attrs and maxOccurs is not None:
                    element.attrs['maxOccurs'] = maxOccurs
            if 'type' not in attrs and 'ref' not in attrs:
                element.setExplicitDefine(1)
            if len(self.stack) == 1:
                element.setTopLevel(1)
            if 'substitutionGroup' in attrs and 'name' in attrs:
                substituteName = attrs['name']
                headName = attrs['substitutionGroup']
                _, headName = get_prefix_and_value(headName)
                if headName not in SubstitutionGroups:
                    SubstitutionGroups[headName] = []
                SubstitutionGroups[headName].append(substituteName)
            if name == ComplexTypeType:
                element.complexType = 1
            if self.inChoice and self.currentChoice:
                element.choice = self.currentChoice
            self.elementStack.append(
                (strip_namespace(name), attrs.get('name'), element))
            self.stack.append(element)
        elif name == ComplexTypeType:
            if len(self.stack) > 0:
                element = self.stack[-1]
                self.elementStack.append(
                    (strip_namespace(name), attrs.get('name'), element))
            # If it have any attributes and there is something on the stack,
            #   then copy the attributes to the item on top of the stack.
            if len(self.stack) > 1 and len(attrs) > 0:
                parentDict = self.stack[-1].getAttrs()
                for key in attrs.keys():
                    parentDict[key] = attrs[key]
            self.inComplexType = 1
        elif name == AnyType:
            element = XschemaElement(attrs)
            element.type = AnyTypeIdentifier
            self.stack.append(element)
        elif name == GroupType:
            element = XschemaElement(attrs)
            if len(self.stack) == 1:
                element.setTopLevel(1)
            self.stack.append(element)
        elif name == SequenceType:
            self.inSequence = 1
            self.sequenceStack.append(
                [attrs.get('minOccurs'), attrs.get('maxOccurs')])
        elif name == ChoiceType:
            self.currentChoice = XschemaElement(attrs)
            self.currentChoiceId += 1
            self.currentChoice.setChoiceGroup(self.currentChoiceId)
            self.inChoice = 1
        elif name == AttributeType:
            self.inAttribute = 1
            fully_qualified_name = None
            if 'name' in attrs:
                name = attrs['name']
                fully_qualified_name = capture_fq_attr_name(attrs['name'])
            elif 'ref' in attrs:
                name = strip_namespace(attrs['ref'])
                fully_qualified_name = capture_fq_attr_name(attrs['ref'])
            else:
                name = 'no_attribute_name'
            data_type = StringType[0]
            if 'type' in attrs:
                data_type = attrs['type']
            elif 'ref' in attrs and SchemaLxmlTree is not None:
                nsmap = {'xs': 'http://www.w3.org/2001/XMLSchema'}
                attr_types = SchemaLxmlTree.xpath(
                    "./xs:attribute[@name=$attrname]",
                    namespaces=nsmap, attrname=name)
                if attr_types:
                    data_type1 = attr_types[0].get('type')
                    if data_type1 is not None:
                        data_type = data_type1
            if 'use' in attrs:
                use = attrs['use']
            else:
                use = 'optional'
            if 'default' in attrs:
                default = attrs['default']
            else:
                default = None
            if 'fixed' in attrs:
                fixed = attrs['fixed']
            else:
                fixed = None
            if self.stack[-1].attributeGroup:
                # Add this attribute to a current attributeGroup.
                attribute = XschemaAttribute(
                    name, data_type, use, default, fixed)
                self.stack[-1].attributeGroup.add(name, attribute)
            else:
                # Add this attribute to the element/complexType.
                attribute = XschemaAttribute(
                    name, data_type, use, default, fixed)
                self.stack[-1].attributeDefs[name] = attribute
                self.stack[-1].attributeDefsList.append(name)
            attribute.fully_qualified_name = fully_qualified_name
            self.lastAttribute = attribute
        elif name == AttributeGroupType:
            if self.attributeGroupLevel >= 1:
                # We are in an attribute group and are declaring a reference
                #   to another attribute group.
                if 'ref' in attrs:
                    self.stack[-1].attributeGroup.add(attrs['ref'], None)
            else:
                # If it has attribute 'name', then we are defining a new
                #   attribute group.
                #   Prepare to save it as an attributeGroup.
                if 'name' in attrs:
                    name = strip_namespace(attrs['name'])
                    attributeGroup = XschemaAttributeGroup(name)
                    element = XschemaElement(attrs)
                    if len(self.stack) == 1:
                        element.setTopLevel(1)
                    element.setAttributeGroup(attributeGroup)
                    self.stack.append(element)
                # If it has attribute 'ref', add it to the list of
                #   attributeGroups for this element/complexType.
                if 'ref' in attrs:
                    self.stack[-1].attributeGroupNameList.append(attrs['ref'])
            self.attributeGroupLevel += 1
        elif name == SimpleContentType:
            self.inSimpleContent = 1
            if len(self.stack) > 0:
                self.stack[-1].setSimpleContent(True)
        elif name == ComplexContentType:
            pass
        elif name == ExtensionType:
            if 'base' in attrs and len(self.stack) > 0:
                extensionBase = attrs['base']
                if (extensionBase in StringType or
                        extensionBase in IDTypes or
                        extensionBase in NameTypes or
                        extensionBase == TokenType or
                        extensionBase in DateTimeGroupType or
                        extensionBase == Base64Type or
                        extensionBase in IntegerType or
                        extensionBase == DecimalType or
                        extensionBase == PositiveIntegerType or
                        extensionBase == NegativeIntegerType or
                        extensionBase == NonPositiveIntegerType or
                        extensionBase == NonNegativeIntegerType or
                        extensionBase == BooleanType or
                        extensionBase == FloatType or
                        extensionBase == DoubleType or
                        extensionBase in OtherSimpleTypes):
                    if (len(self.stack) > 0 and
                            isinstance(self.stack[-1], XschemaElement)):
                        self.stack[-1].addSimpleBase(
                            version_py2_encode(extensionBase))
                else:
                    self.stack[-1].setBase(extensionBase)
        elif name == AnyAttributeType:
            # Mark the current element as containing anyAttribute.
            self.stack[-1].setAnyAttribute(1)
        elif name == SimpleTypeType:
            # fixlist
            if self.inAttribute:
                pass
            elif self.inSimpleType <= 0:
                # Save the name of the simpleType, but ignore everything
                #   else about it (for now).
                if 'name' in attrs:
                    stName = attrs['name']
                elif len(self.stack) > 0:
                    stName = self.stack[-1].getName()
                else:
                    stName = None
                element = SimpleTypeElement(stName)
                SimpleTypeDict[stName] = element
                SimpleTypeDict[Targetnamespace + ":" + stName] = element
                self.stack.append(element)
                self.elementStack.append(
                    (strip_namespace(name), attrs.get('name'), element))
            self.inSimpleType += 1
        elif name == RestrictionType:
            if self.inAttribute:
                if 'base' in attrs:
                    self.lastAttribute.setData_type(attrs['base'])
            else:
                # If we are in a simpleType, capture the name of
                #   the restriction base.
                if ((self.inSimpleType >= 1 or self.inSimpleContent) and
                        'base' in attrs):
                    self.stack[-1].setBase(attrs['base'])
                else:
                    if 'base' in attrs:
                        self.stack[-1].setRestrictionBase(attrs['base'])
            self.inRestrictionType = 1
        elif name == EnumerationType:
            if self.inAttribute and 'value' in attrs:
                # We know that the restriction is on an attribute and the
                # attributes of the current element are un-ordered so the
                # instance variable "lastAttribute" will have our attribute.
                self.lastAttribute.values.append(attrs['value'])
            elif self.inElement and 'value' in attrs:
                # We're not in an attribute so the restriction must have
                # been placed on an element and that element will still be
                # in the stack. We search backwards through the stack to
                # find the last element.
                element = None
                if self.stack:
                    for entry in reversed(self.stack):
                        if isinstance(entry, XschemaElement):
                            element = entry
                            break
                if element is None:
                    err_msg('Cannot find element to attach '
                            'enumeration: %s\n' % (attrs['value']), )
                    sys.exit(1)
                element.values.append(attrs['value'])
            elif self.inSimpleType >= 1 and 'value' in attrs:
                # We've been defined as a simpleType on our own.
                self.stack[-1].values.append(attrs['value'])
            self.inEnumerationType = 1
        elif name == UnionType:
            # Union types are only used with a parent simpleType and we want
            # the parent to know what it's a union of.
            parentelement = self.stack[-1]
            if (isinstance(parentelement, SimpleTypeElement) and
                    'memberTypes' in attrs):
                for member in attrs['memberTypes'].split(" "):
                    self.stack[-1].unionOf.append(member)
        elif name == WhiteSpaceType and self.inRestrictionType:
            if 'value' in attrs:
                if attrs.getValue('value') == 'collapse':
                    self.stack[-1].collapseWhiteSpace = 1
        elif name == ListType:
            self.inListType = 1
            # fixlist
            if self.inSimpleType >= 1:
                self.stack[-1].setListType(1)
                if 'itemType' in attrs:
                    self.stack[-1].setBase(attrs['itemType'])
        elif name == AnnotationType:
            self.inAnnotationType = 1
        elif name == DocumentationType:
            if self.inAnnotationType:
                self.inDocumentationType = 1
        _log.debug("Start element stack: %d", len(self.stack))

    def endElement(self, name):
        _log.debug("End element: %s", name)
        _log.debug("End element stack: %d", len(self.stack))
        if name == SimpleTypeType:      # and self.inSimpleType:
            self.inSimpleType -= 1
            if self.inAttribute:
                pass
            elif self.inSimpleType <= 0:
                # If the simpleType is directly off the root, it may be used to
                # qualify the type of many elements and/or attributes so we
                # don't want to loose it entirely.
                simpleType = self.stack.pop()
                # fixlist
                if len(self.stack) == 1:
                    self.topLevelSimpleTypes.append(simpleType)
                    self.stack[-1].setListType(simpleType.isListType())
                self.elementStack.pop()
        elif name == RestrictionType and self.inRestrictionType:
            self.inRestrictionType = 0
        elif (name == ElementType or
                (name == ComplexTypeType and self.stack[-1].complexType)):
            self.inElement = 0
            self.inNonanonymousComplexType = 0
            if len(self.stack) >= 2:
                element = self.stack.pop()
                self.stack[-1].addChild(element)
            if name == ElementType and len(self.stack) == 1:
                element.setIsRootElement(True)
            self.elementStack.pop()
        elif name == AnyType:
            if len(self.stack) >= 2:
                element = self.stack.pop()
                self.stack[-1].addChild(element)
        elif name == ComplexTypeType:
            self.elementStack.pop()
            self.inComplexType = 0
        elif name == SequenceType:
            self.inSequence = 0
            self.sequenceStack.pop()
        elif name == ChoiceType:
            self.currentChoice = None
            self.inChoice = 0
        elif name == AttributeType:
            self.inAttribute = 0
        elif name == AttributeGroupType:
            if self.attributeGroupLevel >= 2:
                # We are inside an attribute group.
                pass
            else:
                if self.stack[-1].attributeGroup:
                    # The top of the stack contains an XschemaElement which
                    #   contains the definition of an attributeGroup.
                    #   Save this attributeGroup in the
                    #   global AttributeGroup dictionary.
                    attributeGroup = self.stack[-1].attributeGroup
                    name = attributeGroup.getName()
                    AttributeGroups[name] = attributeGroup
                    self.stack[-1].attributeGroup = None
                    self.stack.pop()
                else:
                    # This is a reference to an attributeGroup.
                    # We have already added it to the list of
                    # attributeGroup names.
                    # Leave it.  We'll fill it in during annotate.
                    pass
            self.attributeGroupLevel -= 1
        elif name == GroupType:
            element = self.stack.pop()
            name = element.getAttrs()['name']
            elementGroup = XschemaGroup(element.name)
            ref = element.getAttrs().get('ref')
            if len(self.stack) == 1 and ref is None:
                # This is the definition
                ElementGroups[name] = element
            elif len(self.stack) > 1 and ref is not None:
                # This is a reference. Add it to the parent's children. We
                # need to preserve the order of elements.
                element.setElementGroup(elementGroup)
                self.stack[-1].addChild(element)
        elif name == SchemaType:
            self.inSchema = 0
            if len(self.stack) != 1:
                # fixlist
                err_msg('*** error stack.  len(self.stack): %d\n' % (
                    len(self.stack), ))
                sys.exit(1)
            if self.root:       # change made to avoide logging error
                _log.debug("Previous root: %s", self.root.name)
            else:
                _log.debug("Prvious root:   None")
            self.root = self.stack[0]
            if self.root:
                _log.debug("New root: %s", self.root.name)
            else:
                _log.debug("New root: None")
        elif name == SimpleContentType:
            self.inSimpleContent = 0
        elif name == ComplexContentType:
            pass
        elif name == ExtensionType:
            pass
        elif name == ListType:
            self.inListType = 0
        elif name == AnnotationType:
            self.inAnnotationType = 0
        elif name == DocumentationType:
            if self.inAnnotationType:
                self.inDocumentationType = 0
        elif name == EnumerationType:
            self.inEnumerationType = 0
            if self.current_documentation is not None and len(self.stack) > 1:
                element = self.stack[-1]
                if element.values:
                    curr_value = element.values[-1]
                    curr_value = self.current_documentation
                    if curr_value not in element.values_documentation:
                        element.values_documentation[curr_value] = \
                            self.current_documentation
                    else:
                        element.values_documentation[curr_value] += \
                            self.current_documentation
                self.current_documentation = None

    def findEnclosingName(self):
        name = None
        if len(self.stack) >= 1:
            name = self.stack[-1].name
        return name

    def findEnclosingComplexType(self):
        obj = None
        if len(self.elementStack) >= 1:
            obj = self.elementStack[-1][2]
        return obj

    def characters(self, chrs):
        if self.inDocumentationType:
            # If there is an annotation/documentation element, save it.
            if len(self.stack) > 1 and len(chrs) > 0:
                element = self.stack[-1]
                if not self.inEnumerationType:
                    docElement = self.findEnclosingComplexType()
                    if docElement is None:
                        # Apparently we're in an element.  Save the
                        # doc string for the next complexType.
                        self.savedDocString += chrs
                    else:
                        if self.savedDocString:
                            docElement.documentation += '\nx<>xz<>z%s' % chrs
                            self.savedDocString = ""
                        if self.inAttribute and self.lastAttribute is not None:
                            enclosingName = self.lastAttribute.getName()
                        else:
                            enclosingName = self.findEnclosingName()
                        ammendment = '\nx<>xy<>y%s -- ' % enclosingName
                        if (enclosingName is not None and
                                docElement.documentation.find(
                                    ammendment) == -1):
                            docElement.documentation += ammendment
                            docElement.documentation += chrs
                        else:
                            docElement.documentation += '\nx<>xz<>z%s' % chrs
                else:
                    if element.values:
                        curr_value = element.values[-1]
                        if curr_value not in element.values_documentation:
                            element.values_documentation[curr_value] = chrs
                        else:
                            element.values_documentation[curr_value] += chrs
                    else:
                        current_documentation = chrs.strip()
                        if current_documentation:
                            self.current_documentation = current_documentation
        elif self.inElement:
            pass
        elif self.inComplexType:
            pass
        elif self.inSequence:
            pass
        elif self.inChoice:
            pass


#
# Code generation
#

def generateExportFn_1(wrt, child, name, fill):
    cleanName = cleanupName(name)
    mappedName = mapName(cleanName)
    child_type = child.getType()
    if child_type == DateTimeType:
        wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
            "(namespaceprefix_ , self.gds_format_datetime(self.%s, " \
            "input_name='%s'), namespaceprefix_ , eol_))\n" % \
            (fill, name, name, mappedName, name, )
        wrt(s1)
    elif child_type == DateType:
        wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
            "(namespaceprefix_ , self.gds_format_date(self.%s, " \
            "input_name='%s'), namespaceprefix_ , eol_))\n" % \
            (fill, name, name, mappedName, name, )
        wrt(s1)
    elif child_type == TimeType:
        wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
            "(namespaceprefix_ , self.gds_format_time(self.%s, " \
            "input_name='%s'), namespaceprefix_ , eol_))\n" % \
            (fill, name, name, mappedName, name, )
        wrt(s1)
    elif (child_type in StringType or
            child_type == TokenType or
            child_type in DateTimeGroupType):
        wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        # fixlist
        if (child.getSimpleType() in SimpleTypeDict and
                SimpleTypeDict[child.getSimpleType()].isListType()):
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_encode(self.gds_format_string(" \
                "quote_xml" \
                "(' '.join(self.%s)), " \
                "input_name='%s')), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        else:
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_encode(self.gds_format_string(" \
                "quote_xml(self.%s), " \
                "input_name='%s')), " \
                "namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        wrt(s1)
    elif (child_type in IntegerType or
            child_type == PositiveIntegerType or
            child_type == NonPositiveIntegerType or
            child_type == NegativeIntegerType or
            child_type == NonNegativeIntegerType):
        wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_integer_list(self.%s, " \
                "input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        else:
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_integer(self.%s, " \
                "input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        wrt(s1)
    elif child_type == BooleanType:
        wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_boolean_list(" \
                "self.%s, input_name='%s'), " \
                "namespaceprefix_ , eol_))\n" % (
                    fill, name, name, mappedName, name, )
        else:
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_boolean(" \
                "self.%s, input_name='%s'), namespaceprefix_ , eol_))\n" % (
                    fill, name, name, mappedName, name, )
        wrt(s1)
    elif child_type == FloatType:
        wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_float_list(self.%s, " \
                "input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        else:
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_float(self.%s, " \
                "input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        wrt(s1)
    elif child_type == DecimalType:
        wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_decimal_list(self.%s, " \
                "input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        else:
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_decimal(self.%s, " \
                "input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        wrt(s1)
    elif child_type == DoubleType:
        wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_double_list(self.%s, " \
                "input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        else:
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_double(self.%s, " \
                "input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        wrt(s1)
    elif child_type == Base64Type:
        wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        s1 = ("%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% "
              "(namespaceprefix_ , self.gds_format_base64(self.%s, "
              "input_name='%s'), "
              "namespaceprefix_ , eol_))\n" % (
                  fill, name, name, mappedName, name, ))
        wrt(s1)
    else:
        wrt("%s        if self.%s is not None:\n" % (fill, mappedName))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        # name_type_problem
        if False:        # name == child.getType():
            s1 = "%s            self.%s.export(outfile, level, " \
                "namespaceprefix_, namespacedef_='', " \
                "pretty_print=pretty_print)\n" % \
                (fill, mappedName)
        else:
            namespaceprefix = "namespaceprefix_"
            # Prevent namespace prefix definitions from repeating
            # in nested elements.
            namespacedef = "namespacedef_=''"
            if child.prefix and 'ref' in child.attrs:
                namespaceprefix += "='%s:'" % child.prefix
            s1 = "%s            self.%s.export(outfile, level, %s, " \
                "%s, name_='%s', pretty_print=pretty_print)\n" % \
                (fill, mappedName, namespaceprefix, namespacedef, name)
        wrt(s1)
# end generateExportFn_1


def generateExportFn_2(wrt, child, name, fill):
    cleanName = cleanupName(name)
    mappedName = mapName(cleanName)
    child_type = child.getType()
    wrt("%s    for %s_ in self.%s:\n" % (fill, cleanName, mappedName, ))
    if child_type == DateTimeType:
        wrt("%s        namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s        showIndent(outfile, level, pretty_print)\n' % fill)
        s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
            "(namespaceprefix_ , self.gds_format_datetime(%s_, " \
            "input_name='%s')" \
            ", namespaceprefix_ , eol_))\n" % \
            (fill, name, name, cleanName, name, )
        wrt(s1)
    elif child_type == DateType:
        wrt("%s        namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s        showIndent(outfile, level, pretty_print)\n' % fill)
        s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
            "(namespaceprefix_ , self.gds_format_date(%s_, " \
            "input_name='%s'), " \
            "namespaceprefix_ , eol_))\n" % \
            (fill, name, name, cleanName, name, )
        wrt(s1)
    elif child_type == TimeType:
        wrt("%s        namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s        showIndent(outfile, level, pretty_print)\n' % fill)
        s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
            "(namespaceprefix_ , self.gds_format_time(%s_, " \
            "input_name='%s'), " \
            "namespaceprefix_ , eol_))\n" % \
            (fill, name, name, cleanName, name, )
        wrt(s1)
    elif (child_type in StringType or
            child_type == TokenType or
            child_type in DateTimeGroupType):
        wrt("%s        namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s        showIndent(outfile, level, pretty_print)\n' % fill)
        wrt("%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% "
            "(namespaceprefix_ , self.gds_encode(self.gds_format_string("
            "quote_xml(%s_), "
            "input_name='%s')), namespaceprefix_ , eol_))\n" %
            (fill, name, name, cleanName, name,))
    elif (child_type in IntegerType or
            child_type == PositiveIntegerType or
            child_type == NonPositiveIntegerType or
            child_type == NegativeIntegerType or
            child_type == NonNegativeIntegerType):
        wrt("%s        namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s        showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_integer_list(" \
                "%s_, input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, cleanName, name, )
        else:
            s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_integer(%s_, " \
                "input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, cleanName, name, )
        wrt(s1)
    elif child_type == BooleanType:
        wrt("%s        namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s        showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_boolean_list(" \
                "%s_, input_name='%s'), " \
                "namespaceprefix_ , eol_))\n" % \
                (fill, name, name, cleanName, name, )
        else:
            s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_boolean(" \
                "%s_, input_name='%s'), " \
                "namespaceprefix_ , eol_))\n" % \
                (fill, name, name, cleanName, name, )
        wrt(s1)
    elif child_type == FloatType:
        wrt("%s        namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s        showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_float_list(%s_, " \
                "input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, cleanName, name, )
        else:
            s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_float(" \
                "%s_, input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, cleanName, name, )
        wrt(s1)
    elif child_type == DecimalType:
        wrt("%s        namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s        showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_decimal_list(%s_, " \
                "input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, cleanName, name, )
        else:
            s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_decimal(" \
                "%s_, input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, cleanName, name, )
        wrt(s1)
    elif child_type == DoubleType:
        wrt("%s        namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s        showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_double_list(" \
                "%s_, input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, cleanName, name, )
        else:
            s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_double(%s_, " \
                "input_name='%s'), " \
                "namespaceprefix_ , eol_))\n" % \
                (fill, name, name, cleanName, name, )
        wrt(s1)
    elif child_type == Base64Type:
        wrt("%s        namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s        showIndent(outfile, level, pretty_print)\n' % fill)
        s1 = "%s        outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
            "(namespaceprefix_ , self.gds_format_base64(%s_, " \
            "input_name='%s'), " \
            "namespaceprefix_ , eol_))\n" % \
            (fill, name, name, cleanName, name, )
        wrt(s1)
    else:
        # name_type_problem
        if False:        # name == child.getType():
            s1 = "%s        %s_.export(outfile, level, namespaceprefix_, " \
                "pretty_print=pretty_print)\n" % (fill, cleanName)
        else:
            wrt("%s        namespaceprefix_ = self.%s_nsprefix_ + ':' "
                "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                    fill, mappedName, mappedName, ))
            namespaceprefix = 'namespaceprefix_'
            if child.prefix and 'ref' in child.attrs:
                namespaceprefix += "='%s:'" % child.prefix
            s1 = "%s        %s_.export(outfile, level, %s, " \
                "namespacedef_='', " \
                "name_='%s', pretty_print=pretty_print)\n" % \
                (fill, cleanName, namespaceprefix, name)
        wrt(s1)
# end generateExportFn_2


def generateExportFn_3(wrt, child, name, fill):
    cleanName = cleanupName(name)
    mappedName = mapName(cleanName)
    child_type = child.getType()
    # fix_simpletype
    default = child.getDefault()
    if child_type == DateTimeType:
        if default is None or AlwaysExportDefault:
            wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        else:
            wrt('%s        if self.%s != "%s":\n' % (
                fill, mappedName, default, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
            "(namespaceprefix_ , self.gds_format_datetime(" \
            "self.%s, input_name='%s'), namespaceprefix_ , eol_))\n" % \
            (fill, name, name, mappedName, name, )
        wrt(s1)
    elif child_type == DateType:
        if default is None or AlwaysExportDefault:
            wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        else:
            wrt('%s        if self.%s != "%s":\n' % (
                fill, mappedName, default, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
            "(namespaceprefix_ , self.gds_format_date(" \
            "self.%s, input_name='%s'), namespaceprefix_ , eol_))\n" % \
            (fill, name, name, mappedName, name, )
        wrt(s1)
    elif child_type == TimeType:
        if default is None or AlwaysExportDefault:
            wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        else:
            wrt('%s        if self.%s != "%s":\n' % (
                fill, mappedName, default, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
            "(namespaceprefix_ , self.gds_format_time(" \
            "self.%s, input_name='%s'), namespaceprefix_ , eol_))\n" % \
            (fill, name, name, mappedName, name, )
        wrt(s1)
    elif (child_type in StringType or
            child_type == TokenType or
            child_type in DateTimeGroupType):
        if default is None or AlwaysExportDefault:
            wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        else:
            wrt('%s        if self.%s != "%s":\n' % (
                fill, mappedName, default, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        # fixlist
        if (child.getSimpleType() in SimpleTypeDict and
                SimpleTypeDict[child.getSimpleType()].isListType()):
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_encode(self.gds_format_string(" \
                "quote_xml(' '.join(self.%s)), " \
                "input_name='%s')), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        else:
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_encode(self.gds_format_string(" \
                "quote_xml(self.%s), " \
                "input_name='%s')), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        wrt(s1)
    elif (child_type in IntegerType or
            child_type == PositiveIntegerType or
            child_type == NonPositiveIntegerType or
            child_type == NegativeIntegerType or
            child_type == NonNegativeIntegerType):
        if default is None or AlwaysExportDefault:
            wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        else:
            wrt('%s        if self.%s != %s:\n' % (
                fill, mappedName, default, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_, self.gds_format_integer_list(" \
                "self.%s, input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        else:
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_integer(" \
                "self.%s, input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        wrt(s1)
    elif child_type == BooleanType:
        if default is None or AlwaysExportDefault:
            wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        else:
            if default == 'true':
                wrt('%s        if not self.%s:\n' % (fill, mappedName, ))
            elif default == 'false':
                wrt('%s        if self.%s:\n' % (fill, mappedName, ))
            else:
                wrt('%s        if self.%s is not None:\n' % (
                    fill, mappedName, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_boolean_list(" \
                "self.%s, input_name='%s'), " \
                "namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name)
        else:
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_boolean(" \
                "self.%s, input_name='%s'), " \
                "namespaceprefix_ , eol_))\n" % (
                    fill, name, name, mappedName, name)
        wrt(s1)
    elif child_type == FloatType:
        if default is None or AlwaysExportDefault:
            wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        else:
            wrt('%s        if self.%s != %s:\n' % (
                fill, mappedName, default, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_float_list(" \
                "self.%s, input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        else:
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_float(" \
                "self.%s, input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        wrt(s1)
    elif child_type == DecimalType:
        if default is None or AlwaysExportDefault:
            wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        else:
            wrt('%s        if self.%s != %s:\n' % (
                fill, mappedName, default, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_decimal_list(" \
                "self.%s, input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        else:
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_decimal(" \
                "self.%s, input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        wrt(s1)
    elif child_type == DoubleType:
        if default is None or AlwaysExportDefault:
            wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        else:
            wrt('%s        if self.%s != %s:\n' % (
                fill, mappedName, default, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        if child.isListType():
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_double_list(" \
                "self.%s, input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        else:
            s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
                "(namespaceprefix_ , self.gds_format_double(" \
                "self.%s, input_name='%s'), namespaceprefix_ , eol_))\n" % \
                (fill, name, name, mappedName, name, )
        wrt(s1)
    elif child_type == Base64Type:
        wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
            "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                fill, mappedName, mappedName, ))
        wrt('%s            showIndent(outfile, level, pretty_print)\n' % fill)
        s1 = "%s            outfile.write('<%%s%s>%%s</%%s%s>%%s' %% " \
            "(namespaceprefix_ , self.gds_format_base64(" \
            "self.%s, input_name='%s'), namespaceprefix_ , eol_))\n" % \
            (fill, name, name, mappedName, name, )
        wrt(s1)
    else:
        wrt("%s        if self.%s is not None:\n" % (fill, mappedName))
        # name_type_problem
        if False:        # name == child.getType():
            s1 = ("%s            self.%s.export("
                  "outfile, level, namespaceprefix_, "
                  "pretty_print=pretty_print)\n" % (
                      fill, mappedName))
        else:
            wrt("%s            namespaceprefix_ = self.%s_nsprefix_ + ':' "
                "if (UseCapturedNS_ and self.%s_nsprefix_) else ''\n" % (
                    fill, mappedName, mappedName, ))
            namespaceprefix = 'namespaceprefix_'
            if child.prefix and 'ref' in child.attrs:
                namespaceprefix += "='%s:'" % child.prefix
            s1 = "%s            self.%s.export(outfile, level, %s, " \
                "namespacedef_='', " \
                "name_='%s', pretty_print=pretty_print)\n" % \
                (fill, mappedName, namespaceprefix, name)
        wrt(s1)
# end generateExportFn_3


def generateToEtree(wrt, element, theTargetNS):
    _log.debug(
        'ENTER, element: "%s", theTargetNS "%s"',
        repr(element), theTargetNS)

    # override target namespace
    if element.mustOverrideTargetNamespace:
        theTargetNS = element.targetNamespace
    if theTargetNS == "None":
        theTargetNS = ""
    else:
        theTargetNS = "{%s}" % theTargetNS
    name = element.getName()
    wrt("    def to_etree(self, parent_element=None, "
        "name_='%s', mapping_=None, reverse_mapping_=None, nsmap_=None):\n"
        % (name,))
    parentName, parent = getParentName(element)
    if parentName and not element.getRestrictionBaseObj():
        elName = element.getCleanName()
        wrt("        element = super(%s, self).to_etree("
            "parent_element, name_, mapping_, reverse_mapping_, "
            "nsmap_)\n" % (elName, ))
    else:
        if theTargetNS:
            theTargetNS1 = "'%s' + " % theTargetNS
        else:
            theTargetNS1 = ""
        wrt("        if parent_element is None:\n")
        wrt("            element = etree_.Element(%sname_, "
            "nsmap=nsmap_)\n" % (theTargetNS1,))
        wrt("        else:\n")
        wrt("            element = etree_.SubElement(parent_element, "
            "%sname_, nsmap=nsmap_)\n" % (theTargetNS1,))
    if element.getExtended():
        wrt("        if self.extensiontype_ is not None:\n")
        wrt("            element.set("
            "'{http://www.w3.org/2001/XMLSchema-instance}type', "
            "self.extensiontype_)\n")
    generateToEtreeAttributes(wrt, element)
    generateToEtreeChildren(wrt, element, theTargetNS)
    wrt("        if mapping_ is not None:\n")
    wrt("            mapping_[id(self)] = element\n")
    wrt("        if reverse_mapping_ is not None:\n")
    wrt("            reverse_mapping_[element] = self\n")
    wrt("        return element\n")
# end generateToEtree


def generateToEtreeChildren(wrt, element, Targetnamespace):
    if len(element.getChildren()) > 0:
        if element.isMixed():
            wrt("        for item_ in self.content_:\n")
            wrt("            item_.to_etree(element, "
                "mapping_=mapping_, reverse_mapping_=reverse_mapping_, "
                "nsmap_=nsmap_)\n")
        else:
            for child in element.getChildren():
                unmappedName = child.getName()
                name = child.getCleanName()
                child_type = child.getType()
                if child_type == AnyTypeIdentifier:
                    if child.getMaxOccurs() > 1:
                        wrt('        for obj_ in self.anytypeobjs_:\n')
                        wrt("            obj_.to_etree(element, "
                            "mapping_=mapping_, "
                            "reverse_mapping_=reverse_mapping_, "
                            "nsmap_=nsmap_)\n")
                    else:
                        wrt('        if self.anytypeobjs_ is not None:\n')
                        wrt("            self.anytypeobjs_.to_etree("
                            "element, "
                            "mapping_=mapping_, "
                            "reverse_mapping_=reverse_mapping_, "
                            "nsmap_=nsmap_)\n")
                else:
                    if child.getMaxOccurs() > 1:
                        wrt("        for %s_ in self.%s:\n" % (name, name,))
                    else:
                        wrt("        if self.%s is not None:\n" % (name,))
                        wrt("            %s_ = self.%s\n" % (name, name,))
                    if child_type == DateTimeType:
                        wrt("            etree_.SubElement("
                            "element, '%s%s').text = self."
                            "gds_format_datetime(%s_)\n" % (
                                Targetnamespace, unmappedName, name))
                    elif child_type == DateType:
                        wrt("            etree_.SubElement("
                            "element, '%s%s').text = self."
                            "gds_format_date(%s_)\n" % (
                                Targetnamespace, unmappedName, name))
                    elif child_type == TimeType:
                        wrt("            etree_.SubElement("
                            "element, '%s%s').text = self."
                            "gds_format_time(%s_)\n" % (
                                Targetnamespace, unmappedName, name))
                    elif (child_type in StringType or
                            child_type == TokenType or
                            child_type in DateTimeGroupType):
                        wrt("            etree_.SubElement(element, "
                            "'%s%s').text = "
                            "self.gds_format_string(%s_)\n" % (
                                Targetnamespace, unmappedName, name))
                    elif child_type in IntegerType or \
                            child_type == PositiveIntegerType or \
                            child_type == NonPositiveIntegerType or \
                            child_type == NegativeIntegerType or \
                            child_type == NonNegativeIntegerType:
                        if child.isListType():
                            wrt("            etree_.SubElement(element, "
                                "'%s%s').text = self.gds_format_integer_list"
                                "(%s_)\n" % (
                                    Targetnamespace, unmappedName, name))
                        else:
                            wrt("            etree_.SubElement(element, "
                                "'%s%s').text = self.gds_format_integer"
                                "(%s_)\n" % (
                                    Targetnamespace, unmappedName, name))
                    elif child_type == BooleanType:
                        if child.isListType():
                            wrt("            etree_.SubElement(element, "
                                "'%s%s').text = self.gds_format_boolean_list"
                                "(%s_)\n" % (
                                    Targetnamespace, unmappedName, name))
                        else:
                            wrt("            etree_.SubElement(element, "
                                "'%s%s').text = self.gds_format_boolean"
                                "(%s_)\n" % (
                                    Targetnamespace, unmappedName, name))
                    elif child_type == FloatType:
                        if child.isListType():
                            wrt("            etree_.SubElement(element, "
                                "'%s%s').text = self.gds_format_float_list"
                                "(%s_)\n" % (
                                    Targetnamespace, unmappedName, name))
                        else:
                            wrt("            etree_.SubElement(element, "
                                "'%s%s').text = self.gds_format_float"
                                "(%s_)\n" % (
                                    Targetnamespace, unmappedName, name))
                    elif child_type == DecimalType:
                        if child.isListType():
                            wrt("            etree_.SubElement(element, "
                                "'%s%s').text = self.gds_format_decimal_list"
                                "(%s_)\n" % (
                                    Targetnamespace, unmappedName, name))
                        else:
                            wrt("            etree_.SubElement(element, "
                                "'%s%s').text = self.gds_format_decimal"
                                "(%s_)\n" % (
                                    Targetnamespace, unmappedName, name))
                    elif child_type == DoubleType:
                        if child.isListType():
                            wrt("            etree_.SubElement(element, "
                                "'%s%s').text = self.gds_format_double_list"
                                "(%s_)\n" % (
                                    Targetnamespace, unmappedName, name))
                        else:
                            wrt("            etree_.SubElement(element, "
                                "'%s%s').text = self.gds_format_double"
                                "(%s_)\n" % (
                                    Targetnamespace, unmappedName, name))
                    elif child_type == Base64Type:
                        wrt("            etree_.SubElement(element, "
                            "'%s%s').text = self.gds_format_base64"
                            "(%s_)\n" % (
                                Targetnamespace, unmappedName, name))
                    else:
                        wrt("            %s_.to_etree(element, name_='%s', "
                            "mapping_=mapping_, "
                            "reverse_mapping_=reverse_mapping_, "
                            "nsmap_=nsmap_)\n" % (
                                name, unmappedName,))
    else:
        if element.getSimpleContent() or element.isMixed():
            wrt("        if self._hasContent():\n")
            wrt("            element.text = self.gds_format_string"
                "(self.get_valueOf_())\n")
#end generateToEtreeChildren


def generateToEtreeAttributes(wrt, element):
    attrDefs = element.getAttributeDefs()
    for key in element.getAttributeDefsList():
        attrDef = attrDefs[key]
        name = attrDef.getName()
        cleanName = mapName(cleanupName(name))
        attrType = attrDef.getBaseType()
        wrt("        if self.%s is not None:\n" % (cleanName, ))
        if (attrType in StringType or
                attrType in IDTypes or
                attrType == TokenType):
            s1 = '''            element.set('%s', ''' \
                '''self.gds_format_string(self.%s))\n''' % (name, cleanName, )
        elif (attrType in IntegerType or
                attrType == PositiveIntegerType or
                attrType == NonPositiveIntegerType or
                attrType == NegativeIntegerType or
                attrType == NonNegativeIntegerType):
            s1 = '''            element.set('%s', ''' \
                '''self.gds_format_integer(self.%s))\n''' % (
                    name, cleanName, )
        elif attrType == BooleanType:
            s1 = '''            element.set('%s', ''' \
                '''self.gds_format_boolean(self.%s))\n''' % (name, cleanName, )
        elif (attrType == FloatType or
                attrType == DecimalType):
            s1 = '''            element.set('%s', ''' \
                '''self.gds_format_float(self.%s))\n''' % (name, cleanName, )
        elif attrType == DoubleType:
            s1 = '''            element.set('%s', ''' \
                '''self.gds_format_double(self.%s))\n''' % (name, cleanName, )
        elif attrType == DateTimeType:
            s1 = '''            element.set('%s', ''' \
                '''self.gds_format_datetime(self.%s))\n''' % (
                    name, cleanName, )
        elif attrType == DateType:
            s1 = '''            element.set('%s', ''' \
                '''self.gds_format_date(self.%s))\n''' % (name, cleanName, )
        elif attrType == TimeType:
            s1 = '''            element.set('%s', ''' \
                '''self.gds_format_time(self.%s))\n''' % (name, cleanName, )
        else:
            s1 = '''            element.set('%s', self.%s)\n''' % (
                name, cleanName, )
        wrt(s1)
# end generateToEtreeAttributes


def generateExportAttributes(wrt, element, hasAttributes):
    if len(element.getAttributeDefs()) > 0:
        hasAttributes += 1
        attrDefs = element.getAttributeDefs()
        for key in element.getAttributeDefsList():
            attrDef = attrDefs[key]
            name = attrDef.getName()
            if attrDef.fully_qualified_name is not None:
                orig_name = attrDef.fully_qualified_name
            else:
                orig_name = attrDef.getOrig_name()
                if orig_name is None:
                    orig_name = name
            cleanName = mapName(cleanupName(name))
            if True:            # attrDef.getUse() == 'optional':
                default = attrDef.getDefault()
                if attrDef.getUse() == 'required':
                    #s1 = '        if '
                    s1 = '        if self.%s is not None and ' % (cleanName, )
                elif default is None or AlwaysExportDefault:
                    s1 = '        if self.%s is not None and ' % (cleanName, )
                else:
                    attr_type = attrDef.getBaseType()
                    if (attr_type in StringType or
                            attr_type == TokenType or
                            attr_type in DateTimeGroupType):
                        s1 = '        if self.%s != "%s" and ' % (
                            cleanName, default, )
                    elif attr_type == BooleanType:
                        if default == 'true':
                            s1 = '        if not self.%s and ' % (cleanName, )
                        elif default == 'false':
                            s1 = '        if self.%s and ' % (cleanName, )
                        else:
                            s1 = '        if self.%s is not None and ' % (
                                cleanName, )
                    elif attr_type in NumericTypes:
                        s1 = '        if self.%s != %s and ' % (
                            cleanName, default, )
                    else:
                        s1 = '        if self.%s != "%s" and ' % (
                            cleanName, default, )
                s1 += "'%s' not in already_processed:\n" % (cleanName, )
                if sys.version_info.major == 2:
                    s1 = s1.encode('utf-8')
                wrt(s1)
                wrt("            already_processed.add('%s')\n" % (
                    cleanName, ))
                indent = "    "
            else:
                indent = ""
            attrDefType = attrDef.getBaseType()
            if attrDefType == DateTimeType:
                s1 = '''%s        outfile.write(' %s="%%s"' %% ''' \
                    '''self.gds_format_datetime(self.%s, ''' \
                    '''input_name='%s'))\n''' % (
                        indent, orig_name, cleanName, name)
            elif attrDefType == DateType:
                s1 = '''%s        outfile.write(' %s="%%s"' %% ''' \
                    '''self.gds_format_date(self.%s, input_name='%s'))\n''' % (
                        indent, orig_name, cleanName, name)
            elif attrDefType == TimeType:
                s1 = '''%s        outfile.write(' %s="%%s"' %% ''' \
                    '''self.gds_format_time(self.%s, input_name='%s'))\n''' % (
                        indent, orig_name, cleanName, name)
            elif (attrDefType in StringType or
                    attrDefType in IDTypes or
                    attrDefType == TokenType or
                    attrDefType in DateTimeGroupType):
                s1 = '''%s        outfile.write(' %s=%%s' %% ''' \
                    '''(self.gds_encode(self.gds_format_string(''' \
                    '''quote_attrib(self.%s), ''' \
                    '''input_name='%s')), ))\n''' % \
                    (indent, orig_name, cleanName, name, )
            elif (attrDefType in IntegerType or
                    attrDefType == PositiveIntegerType or
                    attrDefType == NonPositiveIntegerType or
                    attrDefType == NegativeIntegerType or
                    attrDefType == NonNegativeIntegerType):
                s1 = '''%s        outfile.write(' %s="%%s"' %% ''' \
                    '''self.gds_format_integer(self.%s, ''' \
                    '''input_name='%s'))\n''' % (
                        indent, orig_name, cleanName, name, )
            elif attrDefType == BooleanType:
                s1 = '''%s        outfile.write(' %s="%%s"' %% ''' \
                    '''self.gds_format_boolean(''' \
                    '''self.%s, input_name='%s'))\n''' % (
                        indent, orig_name, cleanName, name, )
            elif attrDefType == FloatType:
                s1 = '''%s        outfile.write(' %s="%%s"' %% self.''' \
                    '''gds_format_float(self.%s, input_name='%s'))\n''' % (
                        indent, orig_name, cleanName, name)
            elif attrDefType == DecimalType:
                s1 = '''%s        outfile.write(' %s="%%s"' %% self.''' \
                    '''gds_format_decimal(self.%s, input_name='%s'))\n''' % (
                        indent, orig_name, cleanName, name)
            elif attrDefType == DoubleType:
                s1 = '''%s        outfile.write(' %s="%%s"' %% ''' \
                    '''self.gds_format_double(self.%s, ''' \
                    '''input_name='%s'))\n''' % (
                        indent, orig_name, cleanName, name)
            else:
                s1 = '''%s        outfile.write(' %s=%%s' %% ''' \
                    '''(quote_attrib(self.%s), ))\n''' % (
                        indent, orig_name, cleanName, )
            if sys.version_info.major == 2:
                s1 = s1.encode('utf-8')
            wrt(s1)
    if element.getExtended():
        wrt("        if self.extensiontype_ is not None and 'xsi:type' "
            "not in already_processed:\n")
        wrt("            already_processed.add('xsi:type')\n")
        wrt("            outfile.write("
            "' xmlns:xsi=\"http://www.w3.org/2001/XMLSchema-instance\"')\n")
        # fix
        wrt('''            if ":" not in self.extensiontype_:\n'''
            '''                imported_ns_type_prefix_ = '''
            '''GenerateDSNamespaceTypePrefixes_.get('''
            '''self.extensiontype_, '')\n'''
            '''                outfile.write('''
            '''' xsi:type="%s%s"' % (imported_ns_type_prefix_, '''
            '''self.extensiontype_))\n'''
            '''            else:\n'''
            '''                outfile.write('''
            '''' xsi:type="%s"' % self.extensiontype_)\n''')
    return hasAttributes
# end generateExportAttributes


def generateExportChildren(wrt, element, hasChildren, namespace):
    fill = '        '
    if len(element.getChildren()) > 0:
        hasChildren += 1
        if element.isMixed():
            wrt('%sif not fromsubclass_:\n' % (fill, ))
            wrt("%s    for item_ in self.content_:\n" % (fill, ))
            wrt("%s        item_.export(outfile, level, item_.name, "
                "namespaceprefix_, pretty_print=pretty_print)\n" % (fill, ))
        wrt('%sif pretty_print:\n' % (fill, ))
        wrt("%s    eol_ = '\\n'\n" % (fill, ))
        wrt('%selse:\n' % (fill, ))
        wrt("%s    eol_ = ''\n" % (fill, ))
        any_type_child = None
        for child in element.getChildren():
            unmappedName = child.getName()
            name = child.getCleanName()
            # fix_abstract
            type_element = None
            abstract_child = False
            type_name = child.getAttrs().get('type')
            if type_name:
                type_element = ElementDict.get(type_name)
            if type_element and type_element.isAbstract():
                abstract_child = True
            if child.getType() == AnyTypeIdentifier:
                any_type_child = child
            else:
                if abstract_child and child.getMaxOccurs() > 1:
                    wrt("%sfor %s_ in self.%s:\n" % (
                        fill, name, name,))
                    if child.getName() in SubstitutionGroups:
                        wrt("%s    %s_.export(outfile, level, "
                            "namespaceprefix_, namespacedef_='', "
                            "pretty_print=pretty_print)\n" % (
                                fill, name, ))
                    else:
                        wrt("%s    %s_.export(outfile, level, "
                            "namespaceprefix_, name_='%s', namespacedef_='', "
                            "pretty_print=pretty_print)\n" % (
                                fill, name, name, ))
                elif abstract_child:
                    wrt("%sif self.%s is not None:\n" % (fill, name, ))
                    if child.getName() in SubstitutionGroups:
                        wrt("%s    self.%s.export(outfile, level, "
                            "namespaceprefix_, namespacedef_='', "
                            "pretty_print=pretty_print)\n" % (
                                fill, name, ))
                    else:
                        wrt("%s    self.%s.export(outfile, level, "
                            "namespaceprefix_, name_='%s', namespacedef_='', "
                            "pretty_print=pretty_print)\n" % (
                                fill, name, name, ))
                elif child.getMaxOccurs() > 1:
                    generateExportFn_2(
                        wrt, child, unmappedName, '    ')
                else:
                    if (child.getOptional()):
                        generateExportFn_3(
                            wrt, child, unmappedName, '')
                    else:
                        generateExportFn_1(
                            wrt, child, unmappedName, '')
        if any_type_child is not None:
            wrt('        if not fromsubclass_:\n')
            if any_type_child.getMaxOccurs() > 1:
                wrt('            for obj_ in self.anytypeobjs_:\n')
                wrt('                showIndent('
                    'outfile, level, pretty_print)\n')
                wrt("                outfile.write(obj_)\n")
                wrt("                outfile.write('\\n')\n")
            else:
                wrt('            if self.anytypeobjs_ is not None:\n')
                wrt("                content_ = self.anytypeobjs_\n")
                wrt("                outfile.write(content_)\n")
    return hasChildren
# end generateExportChildren


def countChildren(element, count):
    count += len(element.getChildren())
    base = element.getBase()
    if base and base in ElementDict:
        parent = ElementDict[base]
        count = countChildren(parent, count)
    return count


def getParentName(element):
    base = element.getBase()
    rBase = element.getRestrictionBaseObj()
    parentName = None
    parentObj = None
    if base and base in ElementDict:
        parentObj = ElementDict[base]
        parentName = parentObj.getCleanName()
    elif rBase:
        base = element.getRestrictionBase()
        parentObj = ElementDict[base]
        parentName = parentObj.getCleanName()
    return parentName, parentObj


def generateExportFn(wrt, prefix, element, namespace, nameSpacesDef):
    _log.debug(
        'ENTER, prefix: "%s", element: "%s", namespace: "%s", NS Def: "%s"',
        prefix, element, namespace, nameSpacesDef)
    _log.debug('element state: "%s"', repr(element.__dict__))
    childCount = countChildren(element, 0)
    name = element.getName()
    encodedname = version_py2_encode(name)
    base = element.getBase()
    ns_prefix = SchemaNamespaceDict.get(name)
    if ns_prefix is not None and ns_prefix[0] is not None:
        namespacepfx = ns_prefix[0] + ':'
    else:
        namespacepfx = ''
    # Was the --no-namespace-defs command line option used?
    if nameSpacesDef:
        if ns_prefix is not None and ns_prefix[0] is not None:
            namespacepfx = ns_prefix[0] + ':'
            ns_def = 'xmlns:{}'.format(ns_prefix[0])
            if ns_def not in nameSpacesDef:
                nameSpacesDef += ' {}="{}"'.format(ns_def, ns_prefix[1])
    wrt("    def export(self, outfile, level, namespaceprefix_='%s', "
        "namespacedef_='%s', name_='%s', pretty_print=True):\n" %
        (namespacepfx, nameSpacesDef, encodedname, ))
    wrt("        imported_ns_def_ = GenerateDSNamespaceDefs_.get"
        "('%s')\n" % (encodedname, ))
    wrt("        if imported_ns_def_ is not None:\n")
    wrt("            namespacedef_ = imported_ns_def_\n")
    wrt('        if pretty_print:\n')
    wrt("            eol_ = '\\n'\n")
    wrt('        else:\n')
    wrt("            eol_ = ''\n")
    # We need to be able to export the original tag name.
    wrt("        if self.original_tagname_ is not None and name_ == '%s':\n" %
        encodedname)
    wrt("            name_ = self.original_tagname_\n")
    wrt("        if UseCapturedNS_ and self.ns_prefix_:\n")
    wrt("            namespaceprefix_ = self.ns_prefix_ + ':'\n")
    wrt('        showIndent(outfile, level, pretty_print)\n')
    wrt("        outfile.write('<%s%s%s' % (namespaceprefix_, name_, "
        "namespacedef_ and ' ' + namespacedef_ or '', ))\n")
    wrt("        already_processed = set()\n")
    wrt("        self._exportAttributes(outfile, level, "
        "already_processed, namespaceprefix_, name_='%s')\n" %
        (encodedname, ))
    # fix_abstract
    if base and base in ElementDict:
        base_element = ElementDict[base]
        # fix_derived
        if base_element.isAbstract():
            pass
    if childCount == 0 and element.isMixed():
        wrt("        outfile.write('>')\n")
        wrt("        self._exportChildren(outfile, level + 1, "
            "namespaceprefix_, "
            "namespacedef_, "
            "name_, "
            "pretty_print=pretty_print)\n")
        wrt("        outfile.write(self.convert_unicode("
            "self.valueOf_))\n")
        wrt("        outfile.write('</%s%s>%s' % ("
            "namespaceprefix_, name_, eol_))\n")
    else:
        wrt("        if self._hasContent():\n")
        # Added to keep value on the same line as the tag no children.
        if element.getSimpleContent():
            wrt("            outfile.write('>')\n")
            if not element.isMixed():
                wrt("            outfile.write(self.convert_unicode("
                    "self.valueOf_))\n")
        else:
            wrt("            outfile.write('>%s' % (eol_, ))\n")
        wrt("            self._exportChildren(outfile, level + 1, "
            "namespaceprefix_, "
            "namespacedef_, "
            "name_='%s', "
            "pretty_print=pretty_print)\n" %
            (encodedname))
        # Put a condition on the indent to require children.
        if childCount != 0:
            wrt('            showIndent(outfile, level, pretty_print)\n')
        wrt("            outfile.write('</%s%s>%s' % (namespaceprefix_, "
            "name_, eol_))\n")
        wrt("        else:\n")
        wrt("            outfile.write('/>%s' % (eol_, ))\n")
    wrt("    def _exportAttributes(self, outfile, level, "
        "already_processed, namespaceprefix_='%s', name_='%s'):\n" %
        (namespacepfx, encodedname, ))
    hasAttributes = 0
    if element.getAnyAttribute():
        wrt("""\
        unique_counter = 0
        for name, value in self.anyAttributes_.items():
            xsinamespaceprefix = 'xsi'
            xsinamespace1 = 'http://www.w3.org/2001/XMLSchema-instance'
            xsinamespace2 = '{%s}' % (xsinamespace1, )
            if name.startswith(xsinamespace2):
                name1 = name[len(xsinamespace2):]
                name2 = '%s:%s' % (xsinamespaceprefix, name1, )
                if name2 not in already_processed:
                    already_processed.add(name2)
                    outfile.write(' %s=%s' % (name2, quote_attrib(value), ))
            else:
                mo = re_.match(Namespace_extract_pat_, name)
                if mo is not None:
                    namespace, name = mo.group(1, 2)
                    if name not in already_processed:
                        already_processed.add(name)
                        if namespace == 'http://www.w3.org/XML/1998/namespace':
                            outfile.write(' %s=%s' % (
                                name, quote_attrib(value), ))
                        else:
                            unique_counter += 1
                            outfile.write(' xmlns:%d=\"%s\"' % (
                                unique_counter, namespace, ))
                            outfile.write(' %d:%s=%s' % (
                                unique_counter, name, quote_attrib(value), ))
                else:
                    if name not in already_processed:
                        already_processed.add(name)
                        outfile.write(' %s=%s' % (
                            name, quote_attrib(value), ))\n""")
    parentName, parent = getParentName(element)
    if parentName:
        hasAttributes += 1
        elName = element.getCleanName()
        wrt("        super(%s%s, self)._exportAttributes("
            "outfile, level, already_processed, "
            "namespaceprefix_, name_='%s')\n" % (
                prefix, elName, encodedname, ))
    hasAttributes += generateExportAttributes(wrt, element, hasAttributes)
    if hasAttributes == 0:
        wrt("        pass\n")
    wrt("    def _exportChildren(self, outfile, level, "
        "namespaceprefix_='%s', namespacedef_='%s', "
        "name_='%s', fromsubclass_=False, pretty_print=True):\n" %
        (namespacepfx, nameSpacesDef, encodedname, ))
    hasChildren = 0
    # Generate call to _exportChildren in the superclass only if it is
    #  an extension, but *not* if it is a restriction.
    parentName, parent = getParentName(element)
    if parentName and not element.getRestrictionBaseObj():
        hasChildren += 1
        elName = element.getCleanName()
        wrt("        super(%s%s, self)._exportChildren(outfile, level, "
            "namespaceprefix_, namespacedef_, name_, True, "
            "pretty_print=pretty_print)\n" %
            (prefix, elName, ))
    hasChildren += generateExportChildren(wrt, element, hasChildren, namespace)
    if childCount == 0:   # and not element.isMixed():
        wrt("        pass\n")
# end generateExportFn


#
# Generate exportLiteral method.
#

def generateExportLiteralFn_1(wrt, child, name, fill):
    cleanName = cleanupName(name)
    mappedName = mapName(cleanName)
    childType = child.getType()
    if childType == AnyTypeIdentifier:
        wrt('%s        if self.anytypeobjs_ is not None:\n' % (fill, ))
        wrt('%s            showIndent(outfile, level)\n' % fill)
        wrt("%s            outfile.write('anytypeobjs_=model_.anytypeobjs_("
            "\\n')\n" % (fill, ))
        wrt("%s            self.anytypeobjs_.exportLiteral(outfile, level)\n" %
            (fill, ))
        wrt('%s            showIndent(outfile, level)\n' % fill)
        wrt("%s            outfile.write('),\\n')\n" % (fill, ))
    else:
        wrt('%s        if self.%s is not None:\n' % (fill, mappedName, ))
        if childType == DateTimeType:
            wrt('%s            showIndent(outfile, level)\n' % fill)
            wrt("%s            outfile.write('%s="
                "model_.GeneratedsSuper.gds_parse_datetime(\"%%s\"),\\n' %% "
                "self.gds_format_datetime(self.%s, input_name='%s'))\n" %
                (fill, name, mappedName, name, ))
        elif childType == DateType:
            wrt('%s            showIndent(outfile, level)\n' % fill)
            wrt("%s            outfile.write('%s="
                "model_.GeneratedsSuper.gds_parse_date(\"%%s\"),\\n' %% "
                "self.gds_format_date(self.%s, input_name='%s'))\n" %
                (fill, name, mappedName, name, ))
        elif childType == TimeType:
            wrt('%s            showIndent(outfile, level)\n' % fill)
            wrt("%s            outfile.write('%s="
                "model_.GeneratedsSuper.gds_parse_time(\"%%s\"),\\n' %% "
                "self.gds_format_time(self.%s, input_name='%s'))\n" %
                (fill, name, mappedName, name, ))
        elif (childType in StringType or
                childType in IDTypes or
                childType == TokenType or
                childType in DateTimeGroupType):
            wrt('%s            showIndent(outfile, level)\n' % fill)
            if (child.getSimpleType() in SimpleTypeDict and
                    SimpleTypeDict[child.getSimpleType()].isListType()):
                wrt("%s            if self.%s:\n" % (fill, mappedName, ))
                wrt("%s                outfile.write('%s=%%s,\\n' %% "
                    "self.gds_encode(quote_python(' '.join(self.%s)))"
                    ") \n" %
                    (fill, mappedName, mappedName, ))
                wrt("%s            else:\n" % (fill, ))
                wrt("%s                outfile.write('%s=None,\\n')\n" %
                    (fill, mappedName, ))
            else:
                wrt("%s            outfile.write('%s=%%s,\\n' %% "
                    "self.gds_encode(quote_python(self.%s)))\n" %
                    (fill, mappedName, mappedName, ))
        elif (childType in IntegerType or
                childType == PositiveIntegerType or
                childType == NonPositiveIntegerType or
                childType == NegativeIntegerType or
                childType == NonNegativeIntegerType):
            wrt('%s            showIndent(outfile, level)\n' % fill)
            wrt("%s            outfile.write('%s=%%d,\\n' %% self.%s)\n" %
                (fill, mappedName, mappedName, ))
        elif childType == BooleanType:
            wrt('%s            showIndent(outfile, level)\n' % fill)
            wrt("%s            outfile.write('%s=%%s,\\n' %% self.%s)\n" %
                (fill, mappedName, mappedName, ))
        elif (childType == FloatType or
                childType == DecimalType):
            wrt('%s            showIndent(outfile, level)\n' % fill)
            wrt("%s            outfile.write('%s=%%f,\\n' %% self.%s)\n" %
                (fill, mappedName, mappedName, ))
        elif childType == DoubleType:
            wrt('%s            showIndent(outfile, level)\n' % fill)
            wrt("%s            outfile.write("
                "%s=self.gds_format_double(self.%s))\n" % (
                    fill, name, mappedName, ))
        else:
            wrt('%s            showIndent(outfile, level)\n' % fill)
            wrt("%s            outfile.write('%s=model_.%s(\\n')\n" %
                (fill, mappedName, mapName(cleanupName(child.getType()))))
            if name == child.getType():
                s1 = "%s            self.%s.exportLiteral(" \
                    "outfile, level)\n" % \
                    (fill, mappedName)
            else:
                s1 = "%s            self.%s.exportLiteral(" \
                    "outfile, level, name_='%s')\n" % \
                    (fill, mappedName, name)
            wrt(s1)
            wrt('%s            showIndent(outfile, level)\n' % fill)
            wrt("%s            outfile.write('),\\n')\n" % (fill, ))
# end generateExportLiteralFn_1


def generateExportLiteralFn_2(wrt, child, name, fill):
    childType = child.getType()
    if childType == DateTimeType:
        wrt('%s        showIndent(outfile, level)\n' % fill)
        wrt("%s        outfile.write("
            "'model_.GeneratedsSuper.gds_parse_datetime"
            "(\"%%s\"),\\n' %% self.gds_format_datetime("
            "%s_, input_name='%s'))\n" % (fill, name, name, ))
    elif childType == DateType:
        wrt('%s        showIndent(outfile, level)\n' % fill)
        wrt("%s        outfile.write('model_.GeneratedsSuper.gds_parse_date"
            "(\"%%s\"),\\n' %% self.gds_format_date("
            "%s_, input_name='%s'))\n" % (fill, name, name, ))
    elif childType == TimeType:
        wrt('%s        showIndent(outfile, level)\n' % fill)
        wrt("%s        outfile.write('model_.GeneratedsSuper.gds_parse_time"
            "(\"%%s\"),\\n' %% self.gds_format_time("
            "%s_, input_name='%s'))\n" % (fill, name, name, ))
    elif (childType in StringType or
            childType == TokenType or
            childType in DateTimeGroupType):
        wrt('%s        showIndent(outfile, level)\n' % fill)
        wrt("%s        outfile.write('%%s,\\n' %% self.gds_encode("
            "quote_python(%s_)))\n" % (fill, name, ))
    elif (childType in IntegerType or
            childType == PositiveIntegerType or
            childType == NonPositiveIntegerType or
            childType == NegativeIntegerType or
            childType == NonNegativeIntegerType):
        wrt('%s        showIndent(outfile, level)\n' % fill)
        wrt("%s        outfile.write('%%d,\\n' %% %s_)\n" % (fill, name))
    elif childType == BooleanType:
        wrt('%s        showIndent(outfile, level)\n' % fill)
        wrt("%s        outfile.write('%%s,\\n' %% %s_)\n" % (fill, name))
    elif (childType == FloatType or
            childType == DecimalType):
        wrt('%s        showIndent(outfile, level)\n' % fill)
        wrt("%s        outfile.write('%%f,\\n' %% %s_)\n" % (fill, name))
    elif childType == DoubleType:
        wrt('%s        showIndent(outfile, level)\n' % fill)
        wrt("%s        outfile.write('%%e,\\n' %% %s_)\n" % (fill, name))
    else:
        wrt('%s        showIndent(outfile, level)\n' % fill)
        name1 = mapName(cleanupName(child.getType()))
        wrt("%s        outfile.write('model_.%s(\\n')\n" % (fill, name1, ))
        if name == child.getType():
            s1 = "%s        %s_.exportLiteral(outfile, level)\n" % (
                fill, cleanupName(child.getType()), )
        else:
            s1 = "%s        %s_.exportLiteral(outfile, level, name_='%s')\n" \
                % (fill, name, child.getType(), )
        wrt(s1)
        wrt('%s        showIndent(outfile, level)\n' % fill)
        wrt("%s        outfile.write('),\\n')\n" % (fill, ))
# end generateExportLiteralFn_2


def generateExportLiteralFn(wrt, prefix, element):
    wrt("    def exportLiteral(self, outfile, level, name_='%s'):\n" % (
        element.getName(), ))
    wrt("        level += 1\n")
    wrt("        already_processed = set()\n")
    wrt("        self._exportLiteralAttributes(outfile, level, "
        "already_processed, name_)\n")
    wrt("        if self._hasContent():\n")
    wrt("            self._exportLiteralChildren(outfile, level, name_)\n")
    childCount = countChildren(element, 0)
    if element.getSimpleContent() or element.isMixed():
        wrt("        showIndent(outfile, level)\n")
        wrt("        outfile.write('valueOf_ = \"\"\"%s\"\"\",\\n' % "
            "(self.valueOf_,))\n")
    wrt("    def _exportLiteralAttributes(self, outfile, level, "
        "already_processed, name_):\n")
    count = 0
    attrDefs = element.getAttributeDefs()
    for key in element.getAttributeDefsList():
        attrDef = attrDefs[key]
        count += 1
        name = attrDef.getName()
        cleanName = cleanupName(name)
        mappedName = mapName(cleanName)
        attrType = attrDef.getType()
        if attrType in SimpleTypeDict:
            attrType = SimpleTypeDict[attrType].getBase()
        if attrType in SimpleTypeDict:
            attrType = SimpleTypeDict[attrType].getBase()
        wrt("        if self.%s is not None and '%s' not in "
            "already_processed:\n" % (
                mappedName, mappedName, ))
        wrt("            already_processed.add('%s')\n" % (
            mappedName, ))
        if attrType == DateTimeType:
            wrt('            showIndent(outfile, level)\n')
            wrt("            outfile.write('%s="
                "model_.GeneratedsSuper.gds_parse_datetime(\"%%s\"),\\n' %% "
                "self.gds_format_datetime(self.%s, input_name='%s'))\n" %
                (name, mappedName, name, ))
        elif attrType == DateType:
            wrt('            showIndent(outfile, level)\n')
            wrt("            outfile.write('%s="
                "model_.GeneratedsSuper.gds_parse_date(\"%%s\"),\\n' %% "
                "self.gds_format_date(self.%s, input_name='%s'))\n" %
                (name, mappedName, name, ))
        elif attrType == TimeType:
            wrt('            showIndent(outfile, level)\n')
            wrt("            outfile.write('%s="
                "model_.GeneratedsSuper.gds_parse_time(\"%%s\"),\\n' %% "
                "self.gds_format_time(self.%s, input_name='%s'))\n" %
                (name, mappedName, name, ))
        elif (attrType in StringType or
                attrType in IDTypes or
                attrType == TokenType or
                attrType == NCNameType):
            wrt("            showIndent(outfile, level)\n")
            wrt("            outfile.write('%s=\"%%s\",\\n' %% "
                "(self.%s,))\n" %
                (mappedName, mappedName,))
        elif (attrType in IntegerType or
                attrType == PositiveIntegerType or
                attrType == NonPositiveIntegerType or
                attrType == NegativeIntegerType or
                attrType == NonNegativeIntegerType):
            wrt("            showIndent(outfile, level)\n")
            wrt("            outfile.write('%s=%%d,\\n' %% (self.%s,))\n" %
                (mappedName, mappedName,))
        elif attrType == BooleanType:
            wrt("            showIndent(outfile, level)\n")
            wrt("            outfile.write('%s=%%s,\\n' %% (self.%s,))\n" %
                (mappedName, mappedName,))
        elif (attrType == FloatType or
                attrType == DecimalType):
            wrt("            showIndent(outfile, level)\n")
            wrt("            outfile.write('%s=%%f,\\n' %% (self.%s,))\n" %
                (mappedName, mappedName,))
        elif attrType == DoubleType:
            wrt("            showIndent(outfile, level)\n")
            wrt("            outfile.write('%s=%%e,\\n' %% (self.%s,))\n" %
                (mappedName, mappedName,))
        else:
            wrt("            showIndent(outfile, level)\n")
            wrt("            outfile.write('%s=%%s,\\n' %% (self.%s,))\n" %
                (mappedName, mappedName,))
    if element.getAnyAttribute():
        count += 1
        wrt('        for name, value in self.anyAttributes_.items():\n')
        wrt('            showIndent(outfile, level)\n')
        wrt("            outfile.write('%s=\"%s\",\\n' % (name, value,))\n")
    parentName, parent = getParentName(element)
    if parentName:
        count += 1
        elName = element.getCleanName()
        wrt("        super(%s%s, self)._exportLiteralAttributes("
            "outfile, level, already_processed, name_)\n" %
            (prefix, elName, ))
    if count == 0:
        wrt("        pass\n")
    wrt("    def _exportLiteralChildren(self, outfile, level, name_):\n")
    parentName, parent = getParentName(element)
    if parentName:
        elName = element.getCleanName()
        wrt("        super(%s%s, self)._exportLiteralChildren("
            "outfile, level, name_)\n" %
            (prefix, elName, ))
    for child in element.getChildren():
        name = child.getName()
        name = cleanupName(name)
        mappedName = mapName(name)
        if element.isMixed():
            wrt("        showIndent(outfile, level)\n")
            wrt("        outfile.write('content_ = [\\n')\n")
            wrt('        for item_ in self.content_:\n')
            wrt('            item_.exportLiteral(outfile, level, name_)\n')
            wrt("        showIndent(outfile, level)\n")
            wrt("        outfile.write('],\\n')\n")
        else:
            # fix_abstract
            type_element = None
            abstract_child = False
            type_name = child.getAttrs().get('type')
            if type_name:
                type_element = ElementDict.get(type_name)
            if type_element and type_element.isAbstract():
                abstract_child = True
            if abstract_child:
                pass
            else:
                type_name = name
            if child.getMaxOccurs() > 1:
                if child.getType() == AnyTypeIdentifier:
                    wrt("        showIndent(outfile, level)\n")
                    wrt("        outfile.write('anytypeobjs_=[\\n')\n")
                    wrt("        level += 1\n")
                    wrt("        for anytypeobjs_ in self.anytypeobjs_:\n")
                    wrt("            anytypeobjs_.exportLiteral("
                        "outfile, level)\n")
                    wrt("        level -= 1\n")
                    wrt("        showIndent(outfile, level)\n")
                    wrt("        outfile.write('],\\n')\n")
                else:
                    wrt("        showIndent(outfile, level)\n")
                    wrt("        outfile.write('%s=[\\n')\n" % (mappedName, ))
                    wrt("        level += 1\n")
                    wrt("        for %s_ in self.%s:\n" % (name, mappedName))
                    generateExportLiteralFn_2(wrt, child, name, '    ')
                    wrt("        level -= 1\n")
                    wrt("        showIndent(outfile, level)\n")
                    wrt("        outfile.write('],\\n')\n")
            else:
                generateExportLiteralFn_1(wrt, child, type_name, '')
    if childCount == 0 or element.isMixed():
        wrt("        pass\n")
# end generateExportLiteralFn


#
# Generate export to Django ORM.
#
# Notes:
#
# - Must be run inside a Django environment.  Example:
#
#     $ cd mydjangoproject
#     $ python manage.py shell
#

def generateExportDjangoFn(wrt, element):
    generateExportDjango(wrt, element)
    generateExportDjangoAttributes(wrt, element)
    generateExportDjangoChildren(wrt, element)


def generateExportDjango(wrt, element):
    name = cleanupName(element.getName())
    wrt('    def exportDjango(self):\n'
        '        """Export to Django database/ORM.\n'
        '        Must run in the Django environment.\n'
        '        Example:\n'
        '            $ python manage.py shell\n'
        '            IPython 6.5.0 -- An enhanced Interactive Python.\n'
        "            Type '?' for help.\n"
        '            In [1]:\n'
        '            In [1]: %run load_my_data.py mailbox01.xml\n'
        '        where load_my_data.py is a python script that (1) uses a\n'
        '            module generated by generateDS to parse an\n'
        '            XML instance doc, then (2) calls the exportDjango\n'
        '            method.\n'
        '            Example:\n'
        '                import gds_mod\n'
        '                rootObj = gds_mod.parse(infilename, silence=True)\n'
        '                rootObj.exportDjango()\n'
        '        """\n')
    wrt('        self.gds_djo_etl_transform()\n')
    wrt('        dbobj = models_.{}_model()\n'.format(name))
    wrt('        dbobj.save()\n')
    wrt('        self.exportDjangoAttributes(dbobj)\n')
    wrt('        self.exportDjangoChildren(dbobj)\n')
    wrt('        dbobj.save()\n')
    wrt('        self.gds_djo_etl_transform_db_obj(dbobj)\n')
    wrt('        return dbobj\n')
# end generateExportDjango


def generateExportDjangoAttributes(wrt, element):
    wrt('    def exportDjangoAttributes(self, dbobj):\n')
    attrDefs = element.getAttributeDefs()
    attrCount = 0
    for key in element.getAttributeDefsList():
        attrDef = attrDefs[key]
        name = cleanupName(attrDef.getName())
        name = mapName(name)
        djangoName = fixDjangoName(name)
        wrt('        if self.{} is not None:\n'.format(name))
        wrt('            dbobj.{0} = self.{1}\n'.format(djangoName, name))
        attrCount += 1
    if attrCount < 1:
        wrt('        pass\n')
# end generateExportDjangoAttributes


def generateExportDjangoChildren(wrt, element):
    childCount = 0
    wrt('    def exportDjangoChildren(self, dbobj):\n')
    for child in element.getChildren():
        #origName = child.getName()
        name = cleanupName(child.getName())
        #mappedName = mapName(name)
        name = mapName(name)
        djangoName = fixDjangoName(name)
        childType = child.getType()
        if child.isComplex():
            if child.getMaxOccurs() > 1:
                wrt('        for child in self.{0}:\n'.format(
                    name))
                wrt('            child_dbobj = child.exportDjango()\n')
                wrt('            dbobj.'
                    '{1}_model_{0}.add('
                    'child_dbobj)\n'.format(name, childType))
            else:
                wrt('        if self.{} is not None:\n'.format(name))
                wrt('            child_dbobj = '
                    'self.{1}.exportDjango()\n'.format(
                        djangoName, name))
                wrt('            dbobj.{0}Type_model_{0} = '
                    'child_dbobj\n'.format(
                        djangoName, name))
                wrt('            child_dbobj.save()\n')
        else:
            if child.getMaxOccurs() > 1:
                wrt("        dbobj.{0} = json_.dumps("
                    "self.{1}, separators=(',', ':'))\n".format(
                        djangoName, name))
            else:
                wrt('        if self.{} is not None:\n'.format(name))
                wrt('            dbobj.{0} = self.{1}\n'.format(
                    djangoName, name))
        childCount += 1
    if childCount < 1:
        wrt('        pass\n')
# end generateExportDjangoChildren


#
# Generate export to SQLAlchemy ORM.
#
# Notes:
#
# - Must be run inside a SQLAlchemy environment.  Example:
#
#     $ cd mydjangoproject
#     $ python manage.py shell
#

def generateExportSQLAlchemyFn(wrt, element):
    generateExportSQLAlchemy(wrt, element)
    generateExportSQLAlchemyAttributes(wrt, element)
    generateExportSQLAlchemyChildren(wrt, element)


def generateExportSQLAlchemy(wrt, element):
    name = cleanupName(element.getName())
    wrt('    def exportSQLAlchemy(self, session):\n'
        '        """Export to SQLAlchemy database/ORM.\n'
        '        For help with running this code, see:\n'
        '            https://docs.sqlalchemy.org/en/latest/orm/tutorial.html\n'
        '        """\n')
    wrt('        status, dbobj = self.gds_sqa_etl_transform()\n')
    wrt('        if status == 1:\n')
    wrt('            return dbobj\n')
    wrt('        if dbobj is None:\n'.format(name))
    wrt('            dbobj = models_sqa_.{}_model()\n'.format(name))
    wrt('        session.add(dbobj)\n')
    wrt('        self.exportSQLAlchemyAttributes(dbobj)\n')
    wrt('        self.exportSQLAlchemyChildren(session, dbobj)\n')
    wrt('        self.gds_sqa_etl_transform_db_obj(dbobj)\n')
    wrt('        return dbobj\n')
# end generateExportSQLAlchemy


def generateExportSQLAlchemyAttributes(wrt, element):
    wrt('    def exportSQLAlchemyAttributes(self, dbobj):\n')
    attrDefs = element.getAttributeDefs()
    attrCount = 0
    for key in element.getAttributeDefsList():
        attrDef = attrDefs[key]
        name = cleanupName(attrDef.getName())
        name = mapName(name)
        djangoName = fixSQLAlchemyName(name)
        wrt('        if self.{} is not None:\n'.format(name))
        wrt('            dbobj.{0} = self.{1}\n'.format(djangoName, name))
        attrCount += 1
    if attrCount < 1:
        wrt('        pass\n')
# end generateExportSQLAlchemyAttributes


def generateExportSQLAlchemyChildren(wrt, element):
    childCount = 0
    wrt('    def exportSQLAlchemyChildren(self, session, dbobj):\n')
    for child in element.getChildren():
        #origName = child.getName()
        name = cleanupName(child.getName())
        #mappedName = mapName(name)
        name = mapName(name)
        djangoName = fixSQLAlchemyName(name)
        if child.isComplex():
            if child.getMaxOccurs() > 1:
                wrt('        for child in self.{0}:\n'.format(
                    name))
                wrt('            child_dbobj = child.exportSQLAlchemy'
                    '(session)\n')
                wrt('            dbobj.{}.append(' 'child_dbobj)\n'.format(
                    djangoName))
            else:
                wrt('        if self.{} is not None:\n'.format(name))
                wrt('            child_dbobj = '
                    'self.{1}.exportSQLAlchemy(session)\n'.format(
                        djangoName, name))
                wrt('            dbobj.{0} = child_dbobj\n'.format(
                    djangoName, ))
        else:
            if child.getMaxOccurs() > 1:
                wrt("        dbobj.{0} = json_.dumps("
                    "self.{1}, separators=(',', ':'))\n".format(
                        djangoName, name))
            else:
                wrt('        if self.{} is not None:\n'.format(name))
                wrt('            dbobj.{0} = self.{1}\n'.format(
                    djangoName, name))
        childCount += 1
    if childCount < 1:
        wrt('        pass\n')
# end generateExportSQLAlchemyChildren


#
# Generate the method that validates simple types in a complex type
# object and optionally recusively for children.
#

def mapTypeNameToValidatorName(typeName):
    validatorName = None
    baseName = 'gds_validate_'
    if (typeName in StringType or
            typeName == TokenType):
        validatorName = baseName + 'string'
    elif typeName == DateTimeType:
        validatorName = baseName + 'datetime'
    elif typeName == DateType:
        validatorName = baseName + 'date'
    elif typeName == TimeType:
        validatorName = baseName + 'time'
    elif (typeName in IntegerType or
            typeName == PositiveIntegerType or
            typeName == NonPositiveIntegerType or
            typeName == NegativeIntegerType or
            typeName == NonNegativeIntegerType):
        validatorName = baseName + 'integer'
    elif typeName == BooleanType:
        validatorName = baseName + 'boolean'
    elif typeName == FloatType:
        validatorName = baseName + 'float'
    elif typeName == DoubleType:
        validatorName = baseName + 'double'
    elif typeName == DecimalType:
        validatorName = baseName + 'decimal'
    return validatorName
# end mapTypeNameToValidatorName


def is_child_choice(element, child):
    reply = False
    complextypename = element.getName()
    if not SingleFileOutput:
        fqname = element.fullyQualifiedName
        fqsplitnames = fqname.split(':')
        if len(fqsplitnames) == 2:
            lookup = '{%s}%s' % (fqsplitnames[0], fqsplitnames[1],)
            mappedname = SchemaRenameMap.get(lookup)
            if mappedname is not None:
                complextypename = mappedname
    elementname = child.getName()
    items = SchemaLxmlTree.xpath(
        './/xs:complexType[@name=$complextypename]'
        '//xs:element[@name=$elementname]',
        namespaces=SchemaLxmlTreeMap,
        complextypename=complextypename, elementname=elementname,
    )
    if items:
        item = items[0]
        parent = item.getparent()
        if parent.tag == '{%s}choice' % (SchemaLxmlTreeMap.get('xs'), ):
            reply = True
    return reply


def generateValidatorMethods(wrt, element):
    wrt('    def validate_(self, gds_collector, recursive=False):\n')
    wrt('        self.gds_collector_ = gds_collector\n')
    wrt('        message_count = len(self.gds_collector_.get_messages())\n')
    # generate validate built-in and restricted simple type attributes
    wrt('        # validate simple type attributes\n')
    attrDefs = element.getAttributeDefs()
    for key in element.getAttributeDefsList():
        attrDef = attrDefs[key]
        name = cleanupName(attrDef.getName())
        mappedName = mapName(name)
        qualifiedTypeName = attrDef.getType()
        if attrDef.getUse() == 'required':
            required = 'True'
        else:
            required = 'False'
        if qualifiedTypeName:
            typeName = strip_namespace(qualifiedTypeName)
            if typeName and typeName in SimpleTypeDict:
                wrt("        self.gds_validate_defined_ST_(self.validate_{0}, "
                    "self.{1}, '{1}')\n".format(
                        cleanupName(typeName), mappedName, ))
            elif qualifiedTypeName:
                validatorName = mapTypeNameToValidatorName(qualifiedTypeName)
                if validatorName:
                    wrt("        self.gds_validate_builtin_ST_("
                        "self.{0}, self.{1}, '{1}')\n".format(
                            validatorName, mappedName, mappedName, ))
            wrt("        self.gds_check_cardinality_(self.{0}, "
                "'{0}', required={1})\n".format(
                    mappedName, required, ))
    # generate validate built-in and restricted simple type children
    wrt('        # validate simple type children\n')
    for child in element.getChildren():
        name = child.getCleanName()
        mappedName = mapName(name)
        qualifiedTypeName = child.getSimpleType()
        if qualifiedTypeName:
            typeName = strip_namespace(qualifiedTypeName)
            if typeName and typeName in SimpleTypeDict:
                if child.getMaxOccurs() > 1:
                    wrt("        for item in self.{}:\n".format(mappedName))
                    wrt("            self.gds_validate_defined_ST_("
                        "self.validate_{}, item, '{}')\n".format(
                            cleanupName(typeName), mappedName, ))
                else:
                    wrt("        self.gds_validate_defined_ST_("
                        "self.validate_{0}, self.{1}, '{1}')\n".format(
                            cleanupName(typeName), mappedName, ))
                comment = ""
                if is_child_choice(element, child):
                    comment = "#"
                    wrt("        # cardinality check omitted for "
                        "choice item {}\n".format(
                            mappedName, ))
                wrt("        {3}self.gds_check_cardinality_(self.{0}, "
                    "'{0}', min_occurs={1}, max_occurs={2})\n".format(
                        mappedName,
                        child.getMinOccurs(), child.getMaxOccurs(),
                        comment, ))
        else:
            qualifiedTypeName = child.getType()
            validatorName = mapTypeNameToValidatorName(qualifiedTypeName)
            if validatorName is not None:
                if child.getMaxOccurs() > 1:
                    wrt("        for item in self.{}:\n".format(mappedName))
                    wrt("            self.gds_validate_builtin_ST_("
                        "self.{}, "
                        "item, '{}')\n".format(
                            validatorName, mappedName, ))
                else:
                    wrt("        self.gds_validate_builtin_ST_("
                        "self.{0}, "
                        "self.{1}, '{1}')\n".format(
                            validatorName, mappedName, ))
                comment = ""
                if is_child_choice(element, child):
                    comment = "#"
                    wrt("        # cardinality check omitted for "
                        "choice item {}\n".format(
                            mappedName, ))
                wrt("        {3}self.gds_check_cardinality_(self.{0}, "
                    "'{0}', min_occurs={1}, max_occurs={2})\n".format(
                        mappedName,
                        child.getMinOccurs(), child.getMaxOccurs(),
                        comment, ))
    # generate validate complex type children
    wrt('        # validate complex type children\n')
    for child in element.getChildren():
        mappedName = cleanupName(mapName(child.getName()))
        if child.isComplex():
            comment = ""
            #if child.choice:
            if is_child_choice(element, child):
                comment = "#"
                wrt("        # cardinality check omitted for "
                    "choice item {}\n".format(
                        mappedName, ))
            wrt("        {3}self.gds_check_cardinality_(self.{0}, "
                "'{0}', min_occurs={1}, max_occurs={2})\n".format(
                    mappedName,
                    child.getMinOccurs(), child.getMaxOccurs(),
                    comment, ))
    # generate validate for valueOf_
    if not len(element.getChildren()):
        simpleBase = element.getSimpleBase()
        if len(simpleBase) > 0:
            typeName = simpleBase[0]
            if typeName in SimpleTypeDict:
                wrt('        # validate valueOf_\n')
                wrt("        self.gds_validate_defined_ST_("
                    "self.validate_{0}, self.{1}, '{1}')\n".format(
                        cleanupName(typeName), 'valueOf_', ))
    wrt('        if recursive:\n')
    has_children = False
    for child in element.getChildren():
        mappedName = cleanupName(mapName(child.getName()))
        if child.isComplex():
            if child.getMaxOccurs() > 1:
                wrt("            for item in self.{}:\n".format(mappedName))
                wrt("                item.validate_(gds_collector, "
                    "recursive=True)\n")
            else:
                wrt("            if self.{} is not None:\n".format(
                    mappedName, ))
                wrt("                self.{}.validate_(gds_collector, "
                    "recursive=True)\n".format(mappedName, ))
            has_children = True
    if not has_children:
        wrt('            pass\n')
    wrt('        return message_count == len('
        'self.gds_collector_.get_messages())\n')
# end generateValidatorMethods


#
# Generate recursive genorator.
#

def generateRecursiveGenerator(wrt, element):
    wrt("    def generateRecursively_(self, level=0):\n")
    wrt("        yield (self, level)\n")
    firstTime = True
    for child in element.getChildren():
        mappedName = cleanupName(mapName(child.getName()))
        if child.isComplex():
            if firstTime:
                wrt("        # generate complex type children\n")
                wrt("        level += 1\n")
                firstTime = False
            wrt("        if self.{}:\n".format(mappedName))
            if child.getMaxOccurs() > 1:
                wrt("            for o in self.{}:\n".format(mappedName))
                wrt("                yield from o.generateRecursively_(level)\n")
            else:
                wrt("            yield from self.{}.generateRecursively_"
                    "(level)\n".format(mappedName))
# end generateRecursiveGenerator


#
# Generate build method.
#

def generateBuildAttributes(wrt, element, hasAttributes):
    attrDefs = element.getAttributeDefs()
    for key in element.getAttributeDefsList():
        attrDef = attrDefs[key]
        hasAttributes += 1
        name = attrDef.getName()
        orig_name = attrDef.getOrig_name()
        if orig_name is None:
            orig_name = name
        cleanName = cleanupName(name)
        mappedName = mapName(cleanName)
        atype = attrDef.getType()
        _, unqualified_type = get_prefix_and_value(atype)
        is_list = False
        if unqualified_type in SimpleTypeDict:
            atype, is_list = resolveBaseTypeForSimpleType(unqualified_type)
        if attrDef.fully_qualified_name == 'xml:id':
            atype = attrDef.fully_qualified_name
        if atype == DateTimeType:
            wrt("        value = find_attr_value_('%s', node)\n" % (
                orig_name, ))
            wrt("        if value is not None and '%s' not in "
                "already_processed:\n" %
                (name, ))
            wrt("            already_processed.add('%s')\n" % (name, ))
            if is_list:
                wrt("            self.%s = value\n" % (mappedName, ))
            else:
                wrt('            try:\n')
                wrt("                self.%s = self.gds_parse_datetime("
                    "value)\n" % (mappedName, ))
                wrt('            except ValueError as exp:\n')
                wrt("                raise ValueError("
                    "'Bad date-time attribute (%s): %%s' %% exp)\n" %
                    (name, ))
        elif atype == DateType:
            wrt("        value = find_attr_value_('%s', node)\n" % (
                orig_name, ))
            wrt("        if value is not None and '%s' not in "
                "already_processed:\n" %
                (name, ))
            wrt("            already_processed.add('%s')\n" % (name, ))
            if is_list:
                wrt("            self.%s = value\n" % (mappedName, ))
            else:
                wrt('            try:\n')
                wrt("                self.%s = self.gds_parse_date("
                    "value)\n" % (mappedName, ))
                wrt('            except ValueError as exp:\n')
                wrt("                raise ValueError("
                    "'Bad date attribute (%s): %%s' %% exp)\n" %
                    (name, ))
        elif atype == TimeType:
            wrt("        value = find_attr_value_('%s', node)\n" % (
                orig_name, ))
            wrt("        if value is not None and '%s' not in "
                "already_processed:\n" %
                (name, ))
            wrt("            already_processed.add('%s')\n" % (name, ))
            if is_list:
                wrt("            self.%s = value\n" % (mappedName, ))
            else:
                wrt('            try:\n')
                wrt("                self.%s = self.gds_parse_time("
                    "value)\n" % (mappedName, ))
                wrt('            except ValueError as exp:\n')
                wrt("                raise ValueError("
                    "'Bad time attribute (%s): %%s' %% exp)\n" %
                    (name, ))
        elif (atype in IntegerType or
                atype == PositiveIntegerType or
                atype == NonPositiveIntegerType or
                atype == NegativeIntegerType or
                atype == NonNegativeIntegerType):
            wrt("        value = find_attr_value_('%s', node)\n" % (
                orig_name, ))
            wrt("        if value is not None and '%s' not in "
                "already_processed:\n" %
                (name, ))
            wrt("            already_processed.add('%s')\n" % (name, ))
            if is_list:
                wrt("            self.gds_validate_integer_list(value, "
                    "node, '%s')\n" % (
                        mappedName, ))
                wrt("            self.%s = value\n" % (
                    mappedName, ))
            else:
                wrt("            self.%s = self.gds_parse_integer("
                    "value, node, '%s')\n" % (
                        mappedName, name, ))
            if atype == PositiveIntegerType:
                wrt('            if self.%s <= 0:\n' % mappedName)
                wrt("                raise_parse_error("
                    "node, 'Invalid PositiveInteger')\n")
            elif atype == NonPositiveIntegerType:
                wrt('            if self.%s > 0:\n' % mappedName)
                wrt("                raise_parse_error("
                    "node, 'Invalid NonPositiveInteger')\n")
            elif atype == NegativeIntegerType:
                wrt('            if self.%s >= 0:\n' % mappedName)
                wrt("                raise_parse_error("
                    "node, 'Invalid NegativeInteger')\n")
            elif atype == NonNegativeIntegerType:
                wrt('            if self.%s < 0:\n' % mappedName)
                wrt("                raise_parse_error("
                    "node, 'Invalid NonNegativeInteger')\n")
        elif atype == BooleanType:
            wrt("        value = find_attr_value_('%s', node)\n" % (
                orig_name, ))
            wrt("        if value is not None and '%s' not in "
                "already_processed:\n" %
                (name, ))
            wrt("            already_processed.add('%s')\n" % (name, ))
            if is_list:
                wrt("            self.gds_validate_boolean_list(value, "
                    "node, '%s')\n" % (
                        mappedName, ))
                wrt("            self.%s = value\n" % mappedName)
            else:
                wrt("            if value in ('true', '1'):\n")
                wrt("                self.%s = True\n" % mappedName)
                wrt("            elif value in ('false', '0'):\n")
                wrt("                self.%s = False\n" % mappedName)
                wrt('            else:\n')
                wrt("                raise_parse_error("
                    "node, 'Bad boolean attribute')\n")
        elif atype == FloatType or atype == DoubleType or atype == DecimalType:
            parser_name, validator_name = get_parser_validator(atype)
            wrt("        value = find_attr_value_('%s', node)\n" % (
                orig_name, ))
            wrt("        if value is not None and '%s' not in "
                "already_processed:\n" %
                (name, ))
            wrt("            already_processed.add('%s')\n" % (name, ))
            if is_list:
                wrt("            self.%s_list(value, "
                    "node, '%s')\n" % (
                        validator_name, mappedName, ))
            else:
                wrt("            value = self.%s(value, node, '%s')\n" % (
                    parser_name, name, ))
            wrt("            self.%s = value\n" % (mappedName, ))
        elif atype == TokenType:
            wrt("        value = find_attr_value_('%s', node)\n" % (
                orig_name, ))
            wrt("        if value is not None and '%s' not in "
                "already_processed:\n" %
                (name, ))
            wrt("            already_processed.add('%s')\n" % (name, ))
            wrt("            self.%s = value\n" % (mappedName, ))
            wrt("            self.%s = ' '.join(self.%s.split())\n" %
                (mappedName, mappedName, ))
        elif atype == 'xml:id':
            # Assume attr['type'] in StringType or attr['type'] == DateTimeType
            wrt("        value = find_attr_value_('%s', node)\n" % (
                atype, ))
            wrt("        if value is not None and '%s' not in "
                "already_processed:\n" %
                (name, ))
            wrt("            already_processed.add('%s')\n" % (name, ))
            wrt("            self.%s = value\n" % (mappedName, ))
        else:
            # Assume attr['type'] in StringType or attr['type'] == DateTimeType
            wrt("        value = find_attr_value_('%s', node)\n" % (
                orig_name, ))
            wrt("        if value is not None and '%s' not in "
                "already_processed:\n" %
                (name, ))
            wrt("            already_processed.add('%s')\n" % (name, ))
            wrt("            self.%s = value\n" % (mappedName, ))
        typeName = attrDef.getType()
        typeName1 = typeName.split(':')
        if len(typeName1) == 2:
            typeName = typeName1[1]
        if typeName and typeName in SimpleTypeDict:
            if is_list:
                wrt("            self.validate_%s(self.%s.split())    "
                    "# validate type %s\n" %
                    (cleanupName(typeName), mappedName, typeName, ))
            else:
                wrt("            self.validate_%s(self.%s)    "
                    "# validate type %s\n" %
                    (cleanupName(typeName), mappedName, typeName, ))
    if element.getAnyAttribute():
        hasAttributes += 1
        wrt('        self.anyAttributes_ = {}\n')
        wrt('        for name, value in attrs.items():\n')
        wrt("            if name not in already_processed:\n")
        wrt('                self.anyAttributes_[name] = value\n')
    if element.getExtended():
        hasAttributes += 1
        wrt("        value = find_attr_value_('xsi:type', node)\n")
        wrt("        if value is not None and 'xsi:type' not in "
            "already_processed:\n")
        wrt("            already_processed.add('xsi:type')\n")
        wrt("            self.extensiontype_ = value\n")
    return hasAttributes
# end generateBuildAttributes


def generateBuildMixed_1(wrt, prefix, child, headChild, keyword, delayed):
    origName = child.getName()
    name = child.getCleanName()
    childType = child.getType()
    mappedName = mapName(name)
    if (childType in StringType or
            childType == TokenType or
            childType in DateTimeGroupType):
        wrt("        %s nodeName_ == '%s' and child_.text is not None:\n" % (
            keyword, origName, ))
        wrt("            valuestr_ = child_.text\n")
        wrt("            valuestr_ = self.gds_parse_string("
            "valuestr_, node, '%s')\n" %
            (name, ))
        wrt("            valuestr_ = self.gds_validate_string("
            "valuestr_, node, '%s')\n" %
            (name, ))
        if childType == TokenType:
            wrt('            valuestr_ = re_.sub(String_cleanup_pat_, '
                '" ", valuestr_).strip()\n')
        wrt("            obj_ = self.mixedclass_("
            "MixedContainer.CategorySimple,\n")
        wrt("                MixedContainer.TypeString, '%s', valuestr_)\n" %
            origName)
        wrt("            self.content_.append(obj_)\n")
        wrt("            self.%s_nsprefix_ = child_.prefix\n" % (name, ))
    elif (childType in IntegerType or
            childType == PositiveIntegerType or
            childType == NonPositiveIntegerType or
            childType == NegativeIntegerType or
            childType == NonNegativeIntegerType):
        wrt("        %s nodeName_ == '%s' and child_.text is not None:\n" % (
            keyword, origName, ))
        wrt("            sval_ = child_.text\n")
        wrt("            ival_ = self.gds_parse_integer("
            "sval_, node, '%s')\n" % (name, ))
        wrt("            ival_ = self.gds_validate_integer("
            "ival_, node, '%s')\n" % (name, ))
        if childType == PositiveIntegerType:
            wrt("            if ival_ <= 0:\n")
            wrt("                raise_parse_error(child_, "
                "'Invalid positiveInteger')\n")
        if childType == NonPositiveIntegerType:
            wrt("            if ival_ > 0:\n")
            wrt("                raise_parse_error(child_, "
                "'Invalid nonPositiveInteger)\n")
        if childType == NegativeIntegerType:
            wrt("            if ival_ >= 0:\n")
            wrt("                raise_parse_error(child_, "
                "'Invalid negativeInteger')\n")
        if childType == NonNegativeIntegerType:
            wrt("            if ival_ < 0:\n")
            wrt("                raise_parse_error(child_, "
                "'Invalid nonNegativeInteger')\n")
        wrt("            obj_ = self.mixedclass_("
            "MixedContainer.CategorySimple,\n")
        wrt("                MixedContainer.TypeInteger, '%s', ival_)\n" % (
            origName, ))
        wrt("            self.content_.append(obj_)\n")
        wrt("            self.%s_nsprefix_ = child_.prefix\n" % (name, ))
    elif childType == BooleanType:
        wrt("        %s nodeName_ == '%s' and child_.text is not None:\n" % (
            keyword, origName, ))
        wrt("            sval_ = child_.text\n")
        wrt("            ival_ = self.gds_parse_boolean(sval_, "
            "node, '%s')\n" %
            (name, ))
        wrt("            ival_ = self.gds_validate_boolean(ival_, "
            "node, '%s')\n" %
            (name, ))
        wrt("            obj_ = self.mixedclass_("
            "MixedContainer.CategorySimple,\n")
        wrt("            MixedContainer.TypeInteger, '%s', ival_)\n" %
            origName)
        wrt("            self.content_.append(obj_)\n")
        wrt("            self.%s_nsprefix_ = child_.prefix\n" % (name, ))
    elif (childType == FloatType or
            childType == DoubleType or
            childType == DecimalType):
        parser_name, validator_name = get_parser_validator(childType)
        wrt("        %s nodeName_ == '%s' and child_.text is not None:\n" % (
            keyword, origName, ))
        wrt("            sval_ = child_.text\n")
        wrt("            fval_ = self.%s("
            "sval_, node, '%s')\n" % (parser_name, name, ))
        wrt("            fval_ = self.%s("
            "fval_, node, '%s')\n" %
            (validator_name, name, ))
        wrt("            obj_ = self.mixedclass_("
            "MixedContainer.CategorySimple,\n")
        wrt("                MixedContainer.TypeFloat, '%s', fval_)\n" %
            origName)
        wrt("            self.content_.append(obj_)\n")
        wrt("            self.%s_nsprefix_ = child_.prefix\n" % (name, ))
    elif childType == Base64Type:
        wrt("        %s nodeName_ == '%s' and child_.text is not None:\n" % (
            keyword, origName, ))
        wrt("            sval_ = child_.text\n")
        wrt("            try:\n")
        wrt("                bval_ = base64.b64decode(sval_)\n")
        wrt("            except (TypeError, ValueError) as exp:\n")
        wrt("                raise_parse_error(child_, "
            "'requires base64 encoded string: %s' % exp)\n")
        wrt("            obj_ = self.mixedclass_("
            "MixedContainer.CategorySimple,\n")
        wrt("                MixedContainer.TypeBase64, '%s', bval_)\n" %
            origName)
        wrt("            self.content_.append(obj_)\n")
        wrt("            self.%s_nsprefix_ = child_.prefix\n" % (name, ))
    else:
        # Perhaps it's a complexType that is defined right here.
        # Generate (later) a class for the nested types.
        type_element = None
        abstract_child = False
        type_name = child.getAttrs().get('type')
        if type_name:
            type_element = ElementDict.get(type_name)
        if type_element and type_element.isAbstract():
            abstract_child = True
        if not delayed and child not in DelayedElements:
            DelayedElements.add(child)
            DelayedElements_subclass.add(child)
        wrt("        %s nodeName_ == '%s':\n" % (keyword, origName, ))
        if abstract_child:
            wrt(TEMPLATE_ABSTRACT_CHILD % (prefix, mappedName, ))
        else:
            type_obj = ElementDict.get(childType)
            if type_obj is not None:
                if type_obj.getName() != type_obj.getType():
                    childType = type_obj.getType()
            if type_obj is not None and type_obj.getExtended():
                wrt("            class_obj_ = self.get_class_obj_("
                    "child_, %s%s)\n" % (
                        prefix, cleanupName(mapName(childType)), ))
                wrt("            class_obj_ = %s%s.factory("
                    "parent_object_=self)\n" % (
                        prefix, cleanupName(mapName(childType)), ))
            else:
                wrt("            obj_ = %s%s.factory("
                    "parent_object_=self)\n" % (
                        prefix, cleanupName(mapName(childType))))
            wrt("            obj_.build(child_, "
                "gds_collector_=gds_collector_)\n")

        wrt("            obj_ = self.mixedclass_("
            "MixedContainer.CategoryComplex,\n")
        wrt("                MixedContainer.TypeNone, '%s', obj_)\n" %
            origName)
        wrt("            self.content_.append(obj_)\n")

        # Generate code to sort mixed content in their class
        # containers
        s1 = "            if hasattr(self, 'add_%s'):\n" % (origName, )
        s1 += "              self.add_%s(obj_.value)\n" % (origName, )
        s1 += "            elif hasattr(self, 'set_%s'):\n" % (origName, )
        s1 += "              self.set_%s(obj_.value)\n" % (origName, )
        wrt(s1)
# end generateBuildMixed_1


def generateBuildMixed(wrt, prefix, element, keyword, delayed, hasChildren):
    for child in element.getChildren():
        generateBuildMixed_1(wrt, prefix, child, child, keyword, delayed)
        hasChildren += 1
        keyword = 'elif'
        # Does this element have a substitutionGroup?
        #   If so generate a clause for each element in the substitutionGroup.
        if child.getName() in SubstitutionGroups:
            for memberName in SubstitutionGroups[child.getName()]:
                if memberName in ElementDict:
                    member = ElementDict[memberName]
                    generateBuildMixed_1(
                        wrt, prefix, member, child, keyword, delayed)
    wrt("        if not fromsubclass_ and child_.tail is not None:\n")
    wrt("            obj_ = self.mixedclass_(MixedContainer.CategoryText,\n")
    wrt("                MixedContainer.TypeNone, '', child_.tail)\n")
    wrt("            self.content_.append(obj_)\n")
    return hasChildren


def generateBuildStandard_1(
        wrt, prefix, child, headChild, element, keyword, delayed):
    origName = child.getName()
    name = cleanupName(child.getName())
    mappedName = mapName(name)
    attrCount = len(child.getAttributeDefs())
    childType = child.getType()
    if childType == DateTimeType:
        wrt("        %s nodeName_ == '%s':\n" % (keyword, origName, ))
        wrt("            sval_ = child_.text\n")
        wrt("            dval_ = self.gds_parse_datetime(sval_)\n")
        if child.getMaxOccurs() > 1:
            wrt("            self.%s.append(dval_)\n" % (mappedName, ))
        else:
            wrt("            self.%s = dval_\n" % (mappedName, ))
        wrt("            self.%s_nsprefix_ = child_.prefix\n" % (name, ))
    elif childType == DateType:
        wrt("        %s nodeName_ == '%s':\n" % (keyword, origName, ))
        wrt("            sval_ = child_.text\n")
        wrt("            dval_ = self.gds_parse_date(sval_)\n")
        if child.getMaxOccurs() > 1:
            wrt("            self.%s.append(dval_)\n" % (mappedName, ))
        else:
            wrt("            self.%s = dval_\n" % (mappedName, ))
        wrt("            self.%s_nsprefix_ = child_.prefix\n" % (name, ))
    elif childType == TimeType:
        wrt("        %s nodeName_ == '%s':\n" % (keyword, origName, ))
        wrt("            sval_ = child_.text\n")
        wrt("            dval_ = self.gds_parse_time(sval_)\n")
        if child.getMaxOccurs() > 1:
            wrt("            self.%s.append(dval_)\n" % (mappedName, ))
        else:
            wrt("            self.%s = dval_\n" % (mappedName, ))
        wrt("            self.%s_nsprefix_ = child_.prefix\n" % (name, ))
    elif (attrCount == 0 and
            (childType in StringType or
                childType == TokenType or
                childType in DateTimeGroupType or
                child.isListType())):
        wrt("        %s nodeName_ == '%s':\n" % (keyword, origName, ))
        if PreserveCdataTags:
            wrt("            mo_ = PRESERVE_CDATA_TAGS_PAT.search("
                "etree_.tostring(child_).strip().decode())\n")
            wrt("            if mo_ is None:\n")
            wrt("                value_ = ''\n")
            wrt("            else:\n")
            wrt("                value_ = mo_.group(1)\n")
        else:
            wrt("            value_ = child_.text\n")
        if childType == TokenType:
            wrt('            if value_:\n')
            wrt('                value_ = re_.sub('
                'String_cleanup_pat_, " ", value_).strip()\n')
            wrt('            else:\n')
            wrt('                value_ = ""\n')
        if child.isListType():
            if (childType in IntegerType or
                    childType == PositiveIntegerType or
                    childType == NonPositiveIntegerType or
                    childType == NegativeIntegerType or
                    childType == NonNegativeIntegerType):
                wrt("            value_ = self.gds_validate_integer_list("
                    "value_, node, '%s')\n" % (name, ))
            elif childType == BooleanType:
                wrt("            value_ = self.gds_validate_boolean_list("
                    "value_, node, '%s')\n" %
                    (name, ))
            elif childType == FloatType:
                wrt("            value_ = self.gds_validate_float_list("
                    "value_, node, '%s')\n" %
                    (name, ))
            elif childType == DecimalType:
                wrt("            value_ = self.gds_validate_decimal_list("
                    "value_, node, '%s')\n" %
                    (name, ))
            elif childType == DoubleType:
                wrt("            value_ = self.gds_validate_double_list("
                    "value_, node, '%s')\n" %
                    (name, ))
        else:
            wrt("            value_ = self.gds_parse_string("
                "value_, node, '%s')\n" %
                (name, ))
            wrt("            value_ = self.gds_validate_string("
                "value_, node, '%s')\n" %
                (name, ))
        if child.getMaxOccurs() > 1:
            wrt("            self.%s.append(value_)\n" % (mappedName, ))
        else:
            wrt("            self.%s = value_\n" % (mappedName, ))
        wrt("            self.%s_nsprefix_ = child_.prefix\n" % (name, ))
    elif (childType in IntegerType or
            childType == PositiveIntegerType or
            childType == NonPositiveIntegerType or
            childType == NegativeIntegerType or
            childType == NonNegativeIntegerType):
        wrt("        %s nodeName_ == '%s' and child_.text:\n" % (
            keyword, origName, ))
        wrt("            sval_ = child_.text\n")
        wrt("            ival_ = self.gds_parse_integer("
            "sval_, node, '%s')\n" % (name, ))
        if childType == PositiveIntegerType:
            wrt("            if ival_ <= 0:\n")
            wrt("                raise_parse_error("
                "child_, 'requires positiveInteger')\n")
        elif childType == NonPositiveIntegerType:
            wrt("            if ival_ > 0:\n")
            wrt("                raise_parse_error("
                "child_, 'requires nonPositiveInteger')\n")
        elif childType == NegativeIntegerType:
            wrt("            if ival_ >= 0:\n")
            wrt("                raise_parse_error("
                "child_, 'requires negativeInteger')\n")
        elif childType == NonNegativeIntegerType:
            wrt("            if ival_ < 0:\n")
            wrt("                raise_parse_error("
                "child_, 'requires nonNegativeInteger')\n")
        wrt("            ival_ = self.gds_validate_integer("
            "ival_, node, '%s')\n" %
            (name, ))
        if child.getMaxOccurs() > 1:
            wrt("            self.%s.append(ival_)\n" % (mappedName, ))
        else:
            wrt("            self.%s = ival_\n" % (mappedName, ))
        wrt("            self.%s_nsprefix_ = child_.prefix\n" % (name, ))
    elif childType == BooleanType:
        wrt("        %s nodeName_ == '%s':\n" % (keyword, origName, ))
        wrt("            sval_ = child_.text\n")
        wrt("            ival_ = self.gds_parse_boolean(sval_, "
            "node, '%s')\n" %
            (name, ))
        wrt("            ival_ = self.gds_validate_boolean(ival_, "
            "node, '%s')\n" %
            (name, ))
        if child.getMaxOccurs() > 1:
            wrt("            self.%s.append(ival_)\n" % (mappedName, ))
        else:
            wrt("            self.%s = ival_\n" % (mappedName, ))
        wrt("            self.%s_nsprefix_ = child_.prefix\n" % (name, ))
    elif (childType == FloatType or
            childType == DoubleType or
            childType == DecimalType):
        parser_name, validator_name = get_parser_validator(childType)
        wrt("        %s nodeName_ == '%s' and child_.text:\n" % (
            keyword, origName, ))
        wrt("            sval_ = child_.text\n")
        wrt("            fval_ = self.%s("
            "sval_, node, '%s')\n" % (parser_name, name, ))
        wrt("            fval_ = self.%s("
            "fval_, node, '%s')\n" %
            (validator_name, name, ))
        if child.getMaxOccurs() > 1:
            wrt("            self.%s.append(fval_)\n" % (mappedName, ))
        else:
            wrt("            self.%s = fval_\n" % (mappedName, ))
        wrt("            self.%s_nsprefix_ = child_.prefix\n" % (name, ))
    elif childType == Base64Type:
        wrt("        %s nodeName_ == '%s':\n" % (keyword, origName, ))
        wrt("            sval_ = child_.text\n")
        wrt("            if sval_ is not None:\n")
        wrt("                try:\n")
        wrt("                    bval_ = base64.b64decode(sval_)\n")
        wrt("                except (TypeError, ValueError) as exp:\n")
        wrt("                    raise_parse_error(child_, "
            "'requires base64 encoded string: %s' % exp)\n")
        wrt("                bval_ = self.gds_validate_base64("
            "bval_, node, '%s')\n" %
            (name, ))
        wrt("            else:\n")
        wrt("                bval_ = None\n")
        if child.getMaxOccurs() > 1:
            wrt("            self.%s.append(bval_)\n" % (mappedName, ))
        else:
            wrt("            self.%s = bval_\n" % (mappedName, ))
        wrt("            self.%s_nsprefix_ = child_.prefix\n" % (name, ))
    else:
        # Perhaps it's a complexType that is defined right here.
        # Generate (later) a class for these anonymous, nested types.
        # fix_abstract
        type_element = None
        abstract_child = False
        type_name = child.getAttrs().get('type')
        elementDef = ElementDict.get(type_name)
        if elementDef is not None:
            if elementDef.getName() != elementDef.getType():
                type_name = elementDef.getType()
        if type_name:
            type_element = ElementDict.get(type_name)
        if type_element and type_element.isAbstract():
            abstract_child = True
        if not delayed and child not in DelayedElements:
            DelayedElements.add(child)
            DelayedElements_subclass.add(child)
        wrt("        %s nodeName_ == '%s':\n" % (keyword, origName, ))
        # Is this a simple type?
        if child.getSimpleType():
            wrt("            obj_ = None\n")
        else:
            # name_type_problem
            # fix_abstract
            if type_element:
                type_name = type_element.getType()
            elif origName in ElementDict:
                type_name = ElementDict[origName].getType()
            else:
                type_name = childType
            type_name = cleanupName(mapName(type_name))
            if abstract_child:
                wrt(TEMPLATE_ABSTRACT_CHILD % (prefix, mappedName, ))
            else:
                type_obj = ElementDict.get(type_name)
                if type_obj is not None and type_obj.getExtended():
                    wrt("            class_obj_ = self.get_class_obj_("
                        "child_, %s%s)\n" %
                        (prefix, type_name, ))
                    wrt("            obj_ = class_obj_.factory("
                        "parent_object_=self)\n")
                else:
                    wrt("            obj_ = %s%s.factory("
                        "parent_object_=self)\n" % (
                            prefix, type_name, ))
                wrt("            obj_.build(child_, "
                    "gds_collector_=gds_collector_)\n")
        if headChild.getMaxOccurs() > 1:
            # The headChild reflects a possible substitutionGroup.
            name = headChild.getName()
            name = mapName(cleanupName(name))
            s1 = "            self.%s.append(obj_)\n" % (name, )
        else:
            # The headChild reflects a possible substitutionGroup.
            name = headChild.getName()
            name = mapName(cleanupName(name))
            s1 = "            self.%s = obj_\n" % (name, )
        wrt(s1)
        wrt("            obj_.original_tagname_ = '%s'\n" % (origName, ))
    #
    # If this child is defined in a simpleType, then generate
    #   a validator method.
    typeName = None
    if child.getSimpleType():
        #typeName = child.getSimpleType()
        typeName = cleanupName(child.getName())
    elif (childType in ElementDict and
            ElementDict[childType].getSimpleType()):
        typeName = ElementDict[childType].getType()
    # fixlist
    # splitting the list is now done in gds_validate_xxx_list.
##     if (child.getSimpleType() in SimpleTypeDict and
##             SimpleTypeDict[child.getSimpleType()].isListType()):
##         wrt("            self.%s = self.%s.split()\n" % (
##             mappedName, mappedName, ))
    typeName = child.getSimpleType()
    if typeName and typeName in SimpleTypeDict:
        if child.getMaxOccurs() > 1:
            wrt("            # validate type %s\n" % (typeName, ))
            wrt("            self.validate_%s(self.%s[-1])\n" % (
                cleanupName(typeName), mappedName, ))
        else:
            wrt("            # validate type %s\n" % (typeName, ))
            wrt("            self.validate_%s(self.%s)\n" % (
                cleanupName(typeName), mappedName, ))
# end generateBuildStandard_1


def transitiveClosure(m, e, seen):
    t = []
    if e in seen:
        return t
    if e in m:
        t += m[e]
        seen.add(e)
        for f in m[e]:
            t += transitiveClosure(m, f, seen)
    return t


def generateBuildStandard(wrt, prefix, element, keyword, delayed, hasChildren):
    any_type_child = None
    for child in element.getChildren():
        if child.getType() == AnyTypeIdentifier:
            any_type_child = child
        else:
            generateBuildStandard_1(
                wrt, prefix, child, child,
                element, keyword, delayed)
            hasChildren += 1
            keyword = 'elif'
            # Does this element have a substitutionGroup?
            #   If so generate a clause for each element in the
            #   substitutionGroup.
            childName = child.getName()
            if childName in SubstitutionGroups:
                seen = set()
                for memberName in transitiveClosure(
                        SubstitutionGroups, childName, seen):
                    memberName = cleanupName(memberName)
                    if memberName in ElementDict:
                        member = ElementDict[memberName]
                        generateBuildStandard_1(
                            wrt, prefix, member, child,
                            element, keyword, delayed)
    if any_type_child is not None:
        type_name = element.getType()
        if any_type_child.getMaxOccurs() > 1:
            if keyword == 'if':
                fill = ''
            else:
                fill = '    '
                wrt("        else:\n")
            wrt("        %scontent_ = self.gds_build_any(child_, '%s')\n" % (
                fill, type_name, ))
            wrt('        %sself.anytypeobjs_.append(content_)\n' % (fill, ))
        else:
            if keyword == 'if':
                fill = ''
            else:
                fill = '    '
                wrt("        else:\n")
            wrt("        %scontent_ = self.gds_build_any(child_, '%s')\n" % (
                fill, type_name, ))
            wrt('        %sself.set_anytypeobjs_(content_)\n' % (fill, ))
        hasChildren += 1
    return hasChildren
# end generateBuildStandard


def generateBuildFn(wrt, prefix, element, delayed):
    base = element.getBase()
    wrt('    def build(self, node, gds_collector_=None):\n')
    wrt('        self.gds_collector_ = gds_collector_\n')
    wrt('        if SaveElementTreeNode:\n')
    wrt('            self.gds_elementtree_node_ = node\n')
    wrt('        already_processed = set()\n')
    wrt("        self.ns_prefix_ = node.prefix\n")
    wrt('        self._buildAttributes('
        'node, node.attrib, already_processed)\n')
    if element.isMixed() or element.getSimpleContent():
        wrt("        self.valueOf_ = get_all_text_(node)\n")
    if element.isMixed():
        wrt("        if node.text is not None:\n")
        wrt("            obj_ = self.mixedclass_("
            "MixedContainer.CategoryText,\n")
        wrt("                MixedContainer.TypeNone, '', node.text)\n")
        wrt("            self.content_.append(obj_)\n")
    wrt('        for child in node:\n')
    wrt("            nodeName_ = Tag_pattern_.match(child.tag).groups()[-1]\n")
    wrt("            self._buildChildren(child, node, nodeName_, "
        "gds_collector_=gds_collector_)\n")
    wrt('        return self\n')
    wrt('    def _buildAttributes(self, node, attrs, already_processed):\n')
    hasAttributes = 0
    hasAttributes = generateBuildAttributes(wrt, element, hasAttributes)
    parentName, parent = getParentName(element)
    if parentName:
        hasAttributes += 1
        elName = element.getCleanName()
        wrt('        super(%s%s, self)._buildAttributes('
            'node, attrs, already_processed)\n' %
            (prefix, elName, ))
    if hasAttributes == 0:
        wrt('        pass\n')
    wrt('    def _buildChildren(self, child_, node, nodeName_, '
        'fromsubclass_=False, gds_collector_=None):\n')
    keyword = 'if'
    hasChildren = 0
    if element.isMixed():
        hasChildren = generateBuildMixed(
            wrt, prefix, element, keyword, delayed, hasChildren)
    else:      # not element.isMixed()
        hasChildren = generateBuildStandard(
            wrt, prefix, element, keyword, delayed, hasChildren)
    # Generate call to _buildChildren in the superclass only if it is
    #  an extension, but *not* if it is a restriction.
    base = element.getBase()
    if base and not element.getSimpleContent():
        elName = element.getCleanName()
        wrt("        super(%s%s, self)._buildChildren("
            "child_, node, nodeName_, True)\n" % (prefix, elName, ))
    if hasChildren == 0:
        wrt("        pass\n")
# end generateBuildFn


def countElementChildren(element, count):
    count += len(element.getChildren())
    base = element.getBase()
    if base and base in ElementDict:
        parent = ElementDict[base]
        countElementChildren(parent, count)
    return count


def buildCtorArgs_multilevel(element, childCount):
    content = []
    addedArgs = {}
    add = content.append
    buildCtorArgs_multilevel_aux(addedArgs, add, element)
    eltype = element.getType()
    if (element.getSimpleContent() or
            element.isMixed() or
            eltype in SimpleTypeDict or
            CurrentNamespacePrefix + eltype in OtherSimpleTypes):
        add(", valueOf_=None")
    if element.isMixed():
        add(', mixedclass_=None')
        add(', content_=None')
    if element.getExtended():
        add(', extensiontype_=None')
    s1 = ''.join(content)
    return s1


def buildCtorArgs_multilevel_aux(addedArgs, add, element):
    parentName, parentObj = getParentName(element)
    if parentName:
        buildCtorArgs_multilevel_aux(addedArgs, add, parentObj)
    buildCtorArgs_aux(addedArgs, add, element)


def buildCtorArgs_aux(addedArgs, add, element):
    attrDefs = element.getAttributeDefs()
    for key in element.getAttributeDefsList():
        attrDef = attrDefs[key]
        name = attrDef.getName()
        default = attrDef.getDefault()
        mappedName = name.replace(':', '_')
        mappedName = cleanupName(mapName(mappedName))
        if mappedName == element.getCleanName():
            mappedName += '_member'
        if mappedName in addedArgs:
            continue
        addedArgs[mappedName] = 1
        try:
            atype = attrDef.getData_type()
        except KeyError:
            atype = StringType
        if (atype in StringType or
                atype == TokenType or
                atype in DateTimeGroupType):
            if default is None:
                add(", %s=None" % mappedName)
            else:
                default1 = escape_string(default)
                add(", %s='%s'" % (mappedName, default1))
        elif atype in IntegerType:
            if default is None:
                add(', %s=None' % mappedName)
            else:
                add(', %s=%s' % (mappedName, default))
        elif atype == PositiveIntegerType:
            if default is None:
                add(', %s=None' % mappedName)
            else:
                add(', %s=%s' % (mappedName, default))
        elif atype == NonPositiveIntegerType:
            if default is None:
                add(', %s=None' % mappedName)
            else:
                add(', %s=%s' % (mappedName, default))
        elif atype == NegativeIntegerType:
            if default is None:
                add(', %s=None' % mappedName)
            else:
                add(', %s=%s' % (mappedName, default))
        elif atype == NonNegativeIntegerType:
            if default is None:
                add(', %s=None' % mappedName)
            else:
                add(', %s=%s' % (mappedName, default))
        elif atype == BooleanType:
            if default is None:
                add(', %s=None' % mappedName)
            else:
                if default in ('false', '0'):
                    add(', %s=%s' % (mappedName, "False"))
                else:
                    add(', %s=%s' % (mappedName, "True"))
        elif atype == FloatType or atype == DoubleType or atype == DecimalType:
            if default is None:
                add(', %s=None' % mappedName)
            else:
                add(', %s=%s' % (mappedName, default))
        else:
            if default is None:
                add(', %s=None' % mappedName)
            else:
                add(", %s='%s'" % (mappedName, default, ))
    for child in element.getChildren():
        cleanName = child.getCleanName()
        if cleanName == element.getCleanName():
            cleanName += '_member'
        if cleanName in addedArgs:
            continue
        addedArgs[cleanName] = 1
        default = child.getDefault()
        if child.getType() == AnyTypeIdentifier:
            add(', anytypeobjs_=None')
        elif child.getMaxOccurs() > 1:
            add(', %s=None' % cleanName)
        else:
            childType = child.getType()
            if (childType in StringType or
                    childType == TokenType or
                    childType == Base64Type or
                    childType in DateTimeGroupType):
                if default is None:
                    add(", %s=None" % cleanName)
                else:
                    default1 = escape_string(default)
                    add(", %s='%s'" % (cleanName, default1, ))
            elif (childType in IntegerType or
                    childType == PositiveIntegerType or
                    childType == NonPositiveIntegerType or
                    childType == NegativeIntegerType or
                    childType == NonNegativeIntegerType):
                if default is None:
                    add(', %s=None' % cleanName)
                else:
                    add(', %s=%s' % (cleanName, default, ))
            elif childType == BooleanType:
                if default is None:
                    add(', %s=None' % cleanName)
                else:
                    if default in ('false', '0'):
                        add(', %s=%s' % (cleanName, "False", ))
                    else:
                        add(', %s=%s' % (cleanName, "True", ))
            elif (childType == FloatType or
                    childType == DoubleType or
                    childType == DecimalType):
                if default is None:
                    add(', %s=None' % cleanName)
                else:
                    add(', %s=%s' % (cleanName, default, ))
            else:
                add(', %s=None' % cleanName)
# end buildCtorArgs_aux


MixedCtorInitializers = '''\
        if mixedclass_ is None:
            self.mixedclass_ = MixedContainer
        else:
            self.mixedclass_ = mixedclass_
        if content_ is None:
            self.content_ = []
        else:
            self.content_ = content_
        self.valueOf_ = valueOf_
'''


def _lookupNS(elem, m):
    '''Lookup namespace prefix in several places'''
    # try to get "useful" value for namespace attribute
    _log.debug(
        'Looking up namespace prefix for element "%s" in "%s".',
        repr(elem),
        repr(m))
    # can tune precedence here
    candidates = [
        elem.prefix,
        m.get(elem.namespace),
        (m.get(elem.fullyQualifiedName.rsplit(':', 1)[0]) if
         elem.fullyQualifiedName is not None else
         None),
        m.get(elem.targetNamespace),
    ]
    for candidate in candidates:
        _log.debug(
            'Candidate for ns prefix: "%s", type "%s"',
            repr(candidate), repr(type(candidate)))
        if candidate is None:
            continue
        if candidate not in m.values():
            _log.warning('Unknown namespace prefix "%s" used.', candidate)
        _log.debug('Using prefix: "%s"', repr(candidate))
        # don't return string literal "None", use Python None
        if candidate == "None":
            _log.debug('Using prefix Python None instead.')
            return None
        return candidate
    # we should not end here
    err_msg('*** No suitable ns prefix for element "%s".\n' % repr(elem))
    return None


def _generate_ns_prefix(wrt, targetName, element, parent, r_nsmap):
    wrt("        self.")
    if targetName is not None:
        wrt('%s_nsprefix_ = ' % targetName)
    else:
        wrt("ns_prefix_ = ")
    nsprefix = None
    if parent is None and element.elementFormDefault == 'qualified':
        nsprefix = _lookupNS(element, r_nsmap)
    if parent is not None and parent.elementFormDefault == 'qualified':
        nsprefix = _lookupNS(element, r_nsmap)
    _log.debug('Using nsprefix "%s".', nsprefix)
    if nsprefix is not None:
        wrt('"%s"\n' % nsprefix)
    else:
        wrt("None\n")


def generateCtor(wrt, prefix, element, r_nsmap):
    _log.debug(
        'ENTER, prefix: "%s", element: "%s", state: "%s"',
        prefix, element, repr(element.__dict__))
    elName = element.getCleanName()
    childCount = countChildren(element, 0)
    s2 = buildCtorArgs_multilevel(element, childCount)
    if sys.version_info.major == 2:
        s2 = s2.encode('utf-8')
    wrt('    def __init__(self%s, gds_collector_=None, **kwargs_):\n' % s2)
    # Save the original tag name.  This is needed when there is a
    # xs:substitutionGroup and we later (e.g. during export) do not know
    # which member of the xs:substitutionGroup this specific element
    # came from.
    wrt('        self.gds_collector_ = gds_collector_\n')
    if not XmlDisabled:
        wrt('        self.gds_elementtree_node_ = None\n')
        wrt('        self.original_tagname_ = None\n')
        wrt("        self.parent_object_ = kwargs_.get('parent_object_')\n")
        _generate_ns_prefix(wrt, None, element, None, r_nsmap)

    parentName, parent = getParentName(element)
    if parentName:
        if parent.getFullyQualifiedName() in AlreadyGenerated:
            args = buildCtorParams(element, parent, childCount)
            s2 = ''.join(args)
            if len(args) > 254:
                wrt('        arglist_ = (%s)\n' % (s2, ))
                wrt('        super(globals().get("%s%s"), self).__init__('
                    '*arglist_, **kwargs_)\n' % (prefix, elName, ))
            else:
                wrt('        super(globals().get("%s%s"), '
                    'self).__init__(%s **kwargs_)\n' % (
                        prefix, elName, s2, ))
    attrDefs = element.getAttributeDefs()
    for key in element.getAttributeDefsList():
        _log.debug('key: "%s"', repr(key))
        attrDef = attrDefs[key]
        mappedName = cleanupName(attrDef.getName())
        name = mapName(mappedName)
        if name == element.getCleanName():
            mbrname = name + '_member'
        else:
            mbrname = name
        attrType = attrDef.getType()
        if attrType == DateTimeType:
            wrt("        if isinstance(%s, BaseStrType_):\n" % (mbrname, ))
            wrt("            initvalue_ = datetime_.datetime.strptime("
                "%s, '%%Y-%%m-%%dT%%H:%%M:%%S')\n" % (mbrname, ))
            wrt("        else:\n")
            wrt("            initvalue_ = %s\n" % (mbrname, ))
            wrt("        self.%s = initvalue_\n" % (name, ))
        elif attrType == DateType:
            wrt("        if isinstance(%s, BaseStrType_):\n" % (mbrname, ))
            wrt("            initvalue_ = datetime_.datetime.strptime("
                "%s, '%%Y-%%m-%%d').date()\n" % (mbrname, ))
            wrt("        else:\n")
            wrt("            initvalue_ = %s\n" % (mbrname, ))
            wrt("        self.%s = initvalue_\n" % (name, ))
        elif attrType == TimeType:
            wrt("        if isinstance(%s, BaseStrType_):\n" % (mbrname, ))
            wrt("            initvalue_ = datetime_.datetime.strptime("
                "%s, '%%H:%%M:%%S').time()\n" % (mbrname, ))
            wrt("        else:\n")
            wrt("            initvalue_ = %s\n" % (mbrname, ))
            wrt("        self.%s = initvalue_\n" % (name, ))
        else:
            _log.debug(
                'attribute "%s", state: "%s"',
                name, repr(attrDef.__dict__))
            attrType = attrDef.getType()
            fullyQualifiedType = attrDef.getFullyQualifiedTypeName()
            is_list = False
            if fullyQualifiedType in SimpleTypeDict:
                attrType, is_list = resolveBaseTypeForSimpleType(
                    fullyQualifiedType)
            pythonType = SchemaToPythonTypeMap.get(attrType)
            if is_list:
                attrVal = mbrname
            else:
                attrVal = "_cast(%s, %s)" % (pythonType, mbrname, )
            wrt('        self.%s = %s\n' % (name, attrVal, ))
            if not XmlDisabled:
                wrt('        self.%s_nsprefix_ = None\n' % (name, ))

    # Generate member initializers in ctor.
    for child in element.getChildren():
        name = cleanupName(child.getCleanName())
        if name == element.getCleanName():
            mbrname = name + '_member'
        else:
            mbrname = name
        _log.debug(
            'Constructor child: "%s", state: %s',
            name, repr(child.__dict__))
        childType = child.getType()
        childTypeDef = ElementDict.get(childType)
        if childTypeDef is not None:
            childSimpleContent = childTypeDef.getSimpleContent()
        else:
            childSimpleContent = False
        if childType == AnyTypeIdentifier:
            if child.getMaxOccurs() > 1:
                wrt('        if anytypeobjs_ is None:\n')
                wrt('            self.anytypeobjs_ = []\n')
                wrt('        else:\n')
                wrt('            self.anytypeobjs_ = anytypeobjs_\n')
            else:
                wrt('        self.anytypeobjs_ = anytypeobjs_\n')
        elif childType == DateTimeType and child.getMaxOccurs() <= 1:
            wrt("        if isinstance(%s, BaseStrType_):\n" % (mbrname, ))
            wrt("            initvalue_ = datetime_.datetime.strptime("
                "%s, '%%Y-%%m-%%dT%%H:%%M:%%S')\n" % (mbrname, ))
            wrt("        else:\n")
            wrt("            initvalue_ = %s\n" % (mbrname, ))
            if child.getMaxOccurs() > 1:
                wrt("        self.%s.append(initvalue_)\n" % (name, ))
            else:
                wrt("        self.%s = initvalue_\n" % (name, ))
            if not XmlDisabled:
                _generate_ns_prefix(wrt, name, child, element, r_nsmap)

        elif childType == DateType and child.getMaxOccurs() <= 1:
            wrt("        if isinstance(%s, BaseStrType_):\n" % (mbrname, ))
            wrt("            initvalue_ = datetime_.datetime.strptime("
                "%s, '%%Y-%%m-%%d').date()\n" % (mbrname, ))
            wrt("        else:\n")
            wrt("            initvalue_ = %s\n" % (mbrname, ))
            if child.getMaxOccurs() > 1:
                wrt("        self.%s.append(initvalue_)\n" % (name, ))
            else:
                wrt("        self.%s = initvalue_\n" % (name, ))
            if not XmlDisabled:
                _generate_ns_prefix(wrt, name, child, element, r_nsmap)
        elif childType == TimeType and child.getMaxOccurs() <= 1:
            wrt("        if isinstance(%s, BaseStrType_):\n" % (mbrname, ))
            wrt("            initvalue_ = datetime_.datetime.strptime("
                "%s, '%%H:%%M:%%S').time()\n" % (mbrname, ))
            wrt("        else:\n")
            wrt("            initvalue_ = %s\n" % (mbrname, ))
            if child.getMaxOccurs() > 1:
                wrt("        self.%s.append(initvalue_)\n" % (name, ))
            else:
                wrt("        self.%s = initvalue_\n" % (name, ))
            if not XmlDisabled:
                _generate_ns_prefix(wrt, name, child, element, r_nsmap)
        else:
            if child.getMaxOccurs() > 1:
                wrt('        if %s is None:\n' % (mbrname, ))
                wrt('            self.%s = []\n' % (name, ))
                wrt('        else:\n')
                wrt('            self.%s = %s\n' % (name, mbrname))
            elif (CreateMandatoryChildren and
                  child.getMinOccurs() == 1 and
                  child.getMaxOccurs() == 1 and
                  child.isComplex() and
                  not childSimpleContent):
                wrt('        if %s is None:\n' % (mbrname, ))
                className = child.getType()
                className = cleanupName(className)
                wrt('            self.%s = globals()["%s%s"]()\n' % (
                    name, prefix, className, ))
                wrt('        else:\n')
                wrt('            self.%s = %s\n' % (name, mbrname))
            else:
                typeObj = ElementDict.get(child.getType())
                if (child.getDefault() and
                        typeObj is not None and
                        typeObj.getSimpleContent()):
                    wrt('        if %s is None:\n' % (mbrname, ))
                    wrt("            self.%s = globals()['%s%s']('%s')\n" %
                        (name, prefix, child.getType(), child.getDefault(), ))
                    wrt('        else:\n')
                    wrt('            self.%s = %s\n' % (name, mbrname))
                else:
                    wrt('        self.%s = %s\n' % (name, mbrname))
                    # validate if it is a simple type.  Validation shows
                    # a warning so no fear that an error would rise.
                    typeName = child.getSimpleType()
                    if typeName and typeName in SimpleTypeDict:
                        wrt('        self.validate_%s(self.%s)\n' % (
                            cleanupName(typeName), mapName(name)))
            if not XmlDisabled:
                _generate_ns_prefix(wrt, name, child, element, r_nsmap)
    eltype = element.getType()
    if (element.getSimpleContent() or
            element.isMixed() or
            eltype in SimpleTypeDict or
            CurrentNamespacePrefix + eltype in OtherSimpleTypes):
        wrt('        self.valueOf_ = valueOf_\n')
    if element.getAnyAttribute():
        wrt('        self.anyAttributes_ = {}\n')
    if element.getExtended():
        wrt('        self.extensiontype_ = extensiontype_\n')
    if element.isMixed():
        wrt(MixedCtorInitializers)
# end generateCtor


# find the simple type, either a named simpleType or an anonymous one.
def find_simple_type_def(tree, stName, element, child, ns, base):
    st = None
    path1 = ("//xs:complexType[@name=$typeName]"
             "//xs:element[@name=$childName]/xs:simpleType")
    path2 = ("//xs:element[@name=$typeName]/xs:complexType//xs:element"
             "[@name=$childName]/xs:simpleType")
    if stName:
        st_defs = tree.xpath(
            "//xs:simpleType[@name=$n]",
            namespaces=ns, n=stName)
        if st_defs:
            st = st_defs[0]
        elif element is not None and child is not None:
            typeName = element.getType()
            childName = child.getName()
            # search for an anonymous simpleType.
            el_defs = tree.xpath(
                path1,
                namespaces=ns, typeName=typeName, childName=childName)
            if el_defs:
                st = el_defs[0]
            else:
                # search for an anonymous simpleType inside an anonymous
                # complexType.
                el_defs = tree.xpath(
                    path2,
                    namespaces=ns, typeName=typeName, childName=childName)
    return st


def resolveBaseTypeForSimpleType(type_val):
    count = 0
    is_list = False
    type_val1 = type_val
    while True:
        element = SimpleTypeDict.get(type_val1)
        if element is not None:
            if element.isListType():
                is_list = True
        type_val1 = element.getBase()
        if type_val1 and not is_builtin_simple_type(type_val1):
            type_val1 = strip_namespace(type_val1)
        if type_val1 is None:
            # Something seems wrong.  Can't find base simple type.
            #   Give up and use default.
            type_val = StringType[0]
            break
        if type_val1 in SimpleTypeDict:
            count += 1
            if count > 10:
                # Give up.  We're in a loop.  Use default.
                type_val = StringType[0]
                break
        else:
            type_val = type_val1
            break
    return type_val, is_list


def get_target_value(default, stName):
    stObj = SimpleTypeDict.get(stName)
    targetValue = default
    if stObj is not None:
        if stObj.getBase() == DateType:
            targetValue = "self.gds_parse_date('{}')".format(default)
        elif stObj.getBase() == TimeType:
            targetValue = "self.gds_parse_time('{}')".format(default)
        elif stObj.getBase() == DateTimeType:
            targetValue = "self.gds_parse_datetime('{}')".format(default)
    return targetValue


Vbar_repl_pat = re.compile(r'([^\\])\|')


# Replace vertical bars with "$|^", unless escaped with backslash.
def replaceVbars(instr):
    outstr, count = re.subn(Vbar_repl_pat, '\\1$|^', instr)
    return outstr


def replaceBlockNames(instr):
    UNICODE_BLOCKS = {
        'BasicLatin': (u'\u0000', u'\u007F'),
        'Latin-1Supplement': (u'\u0080', u'\u00FF'),
        'LatinExtended-A': (u'\u0100', u'\u017F'),
        'LatinExtended-B': (u'\u0180', u'\u024F'),
        'IPAExtensions': (u'\u0250', u'\u02AF'),
        'SpacingModifierLetters': (u'\u02B0', u'\u02FF'),
        'CombiningDiacriticalMarks': (u'\u0300', u'\u036F'),
        'Greek': (u'\u0370', u'\u03FF'),
        'GreekandCoptic': (u'\u0370', u'\u03FF'),
        'Cyrillic': (u'\u0400', u'\u04FF'),
        'CyrillicSupplementary': (u'\u0500', u'\u052F'),
        'CyrillicSupplement': (u'\u0500', u'\u052F'),
        'Armenian': (u'\u0530', u'\u058F'),
        'Hebrew': (u'\u0590', u'\u05FF'),
        'Arabic': (u'\u0600', u'\u06FF'),
        'Syriac': (u'\u0700', u'\u074F'),
        'ArabicSupplement': (u'\u0750', u'\u077F'),
        'Thaana': (u'\u0780', u'\u07BF'),
        'NKo': (u'\u07C0', u'\u07FF'),
        'Samaritan': (u'\u0800', u'\u083F'),
        'Mandaic': (u'\u0840', u'\u085F'),
        'Devanagari': (u'\u0900', u'\u097F'),
        'Bengali': (u'\u0980', u'\u09FF'),
        'Gurmukhi': (u'\u0A00', u'\u0A7F'),
        'Gujarati': (u'\u0A80', u'\u0AFF'),
        'Oriya': (u'\u0B00', u'\u0B7F'),
        'Tamil': (u'\u0B80', u'\u0BFF'),
        'Telugu': (u'\u0C00', u'\u0C7F'),
        'Kannada': (u'\u0C80', u'\u0CFF'),
        'Malayalam': (u'\u0D00', u'\u0D7F'),
        'Sinhala': (u'\u0D80', u'\u0DFF'),
        'Thai': (u'\u0E00', u'\u0E7F'),
        'Lao': (u'\u0E80', u'\u0EFF'),
        #'Tibetan': (u'\u0F00', u'\u0FBF'),
        'Tibetan': (u'\u0F00', u'\u0FFF'),
        'Myanmar': (u'\u1000', u'\u109F'),
        'Georgian': (u'\u10A0', u'\u10FF'),
        'HangulJamo': (u'\u1100', u'\u11FF'),
        'Ethiopic': (u'\u1200', u'\u137F'),
        'EthiopicSupplement': (u'\u1380', u'\u139F'),
        'Cherokee': (u'\u13A0', u'\u13FF'),
        'UnifiedCanadianAboriginalSyllabics': (u'\u1400', u'\u167F'),
        'Ogham': (u'\u1680', u'\u169F'),
        'Runic': (u'\u16A0', u'\u16FF'),
        'Tagalog': (u'\u1700', u'\u171F'),
        'Hanunoo': (u'\u1720', u'\u173F'),
        'Buhid': (u'\u1740', u'\u175F'),
        'Tagbanwa': (u'\u1760', u'\u177F'),
        'Khmer': (u'\u1780', u'\u17FF'),
        'Mongolian': (u'\u1800', u'\u18AF'),
        'UnifiedCanadianAboriginalSyllabicsExtended': (u'\u18B0', u'\u18FF'),
        'Limbu': (u'\u1900', u'\u194F'),
        'TaiLe': (u'\u1950', u'\u197F'),
        'NewTaiLue': (u'\u1980', u'\u19DF'),
        'KhmerSymbols': (u'\u19E0', u'\u19FF'),
        'Buginese': (u'\u1A00', u'\u1A1F'),
        'TaiTham': (u'\u1A20', u'\u1AAF'),
        'Balinese': (u'\u1B00', u'\u1B7F'),
        'Sundanese': (u'\u1B80', u'\u1BBF'),
        'Batak': (u'\u1BC0', u'\u1BFF'),
        'Lepcha': (u'\u1C00', u'\u1C4F'),
        'OlChiki': (u'\u1C50', u'\u1C7F'),
        'VedicExtensions': (u'\u1CD0', u'\u1CFF'),
        'PhoneticExtensions': (u'\u1D00', u'\u1D7F'),
        'PhoneticExtensionsSupplement': (u'\u1D80', u'\u1DBF'),
        'CombiningDiacriticalMarksSupplement': (u'\u1DC0', u'\u1DFF'),
        'LatinExtendedAdditional': (u'\u1E00', u'\u1EFF'),
        'GreekExtended': (u'\u1F00', u'\u1FFF'),
        'GeneralPunctuation': (u'\u2000', u'\u206F'),
        'SuperscriptsandSubscripts': (u'\u2070', u'\u209F'),
        'CurrencySymbols': (u'\u20A0', u'\u20CF'),
        'CombiningMarksforSymbols': (u'\u20D0', u'\u20FF'),
        'CombiningDiacriticalMarksforSymbols': (u'\u20D0', u'\u20FF'),
        'LetterlikeSymbols': (u'\u2100', u'\u214F'),
        'NumberForms': (u'\u2150', u'\u218F'),
        'Arrows': (u'\u2190', u'\u21FF'),
        'MathematicalOperators': (u'\u2200', u'\u22FF'),
        'MiscellaneousTechnical': (u'\u2300', u'\u23FF'),
        'ControlPictures': (u'\u2400', u'\u243F'),
        'OpticalCharacterRecognition': (u'\u2440', u'\u245F'),
        'EnclosedAlphanumerics': (u'\u2460', u'\u24FF'),
        'BoxDrawing': (u'\u2500', u'\u257F'),
        'BlockElements': (u'\u2580', u'\u259F'),
        'GeometricShapes': (u'\u25A0', u'\u25FF'),
        'MiscellaneousSymbols': (u'\u2600', u'\u26FF'),
        'Dingbats': (u'\u2700', u'\u27BF'),
        'MiscellaneousMathematicalSymbols-A': (u'\u27C0', u'\u27EF'),
        'SupplementalArrows-A': (u'\u27F0', u'\u27FF'),
        'BraillePatterns': (u'\u2800', u'\u28FF'),
        'SupplementalArrows-B': (u'\u2900', u'\u297F'),
        'MiscellaneousMathematicalSymbols-B': (u'\u2980', u'\u29FF'),
        'SupplementalMathematicalOperators': (u'\u2A00', u'\u2AFF'),
        'MiscellaneousSymbolsandArrows': (u'\u2B00', u'\u2BFF'),
        'Glagolitic': (u'\u2C00', u'\u2C5F'),
        'LatinExtended-C': (u'\u2C60', u'\u2C7F'),
        'Coptic': (u'\u2C80', u'\u2CFF'),
        'GeorgianSupplement': (u'\u2D00', u'\u2D2F'),
        'Tifinagh': (u'\u2D30', u'\u2D7F'),
        'EthiopicExtended': (u'\u2D80', u'\u2DDF'),
        'CyrillicExtended-A': (u'\u2DE0', u'\u2DFF'),
        'SupplementalPunctuation': (u'\u2E00', u'\u2E7F'),
        'CJKRadicalsSupplement': (u'\u2E80', u'\u2EFF'),
        'KangxiRadicals': (u'\u2F00', u'\u2FDF'),
        'IdeographicDescriptionCharacters': (u'\u2FF0', u'\u2FFF'),
        'CJKSymbolsandPunctuation': (u'\u3000', u'\u303F'),
        'Hiragana': (u'\u3040', u'\u309F'),
        'Katakana': (u'\u30A0', u'\u30FF'),
        'Bopomofo': (u'\u3100', u'\u312F'),
        'HangulCompatibilityJamo': (u'\u3130', u'\u318F'),
        'Kanbun': (u'\u3190', u'\u319F'),
        'BopomofoExtended': (u'\u31A0', u'\u31BF'),
        'CJKStrokes': (u'\u31C0', u'\u31EF'),
        'KatakanaPhoneticExtensions': (u'\u31F0', u'\u31FF'),
        'EnclosedCJKLettersandMonths': (u'\u3200', u'\u32FF'),
        'CJKCompatibility': (u'\u3300', u'\u33FF'),
        #'CJKUnifiedIdeographsExtensionA': (u'\u3400', u'\u4DB5'),
        'CJKUnifiedIdeographsExtensionA': (u'\u3400', u'\u4DBF'),
        'YijingHexagramSymbols': (u'\u4DC0', u'\u4DFF'),
        'CJKUnifiedIdeographs': (u'\u4E00', u'\u9FFF'),
        'YiSyllables': (u'\uA000', u'\uA48F'),
        'YiRadicals': (u'\uA490', u'\uA4CF'),
        'Lisu': (u'\uA4D0', u'\uA4FF'),
        'Vai': (u'\uA500', u'\uA63F'),
        'CyrillicExtended-B': (u'\uA640', u'\uA69F'),
        'Bamum': (u'\uA6A0', u'\uA6FF'),
        'ModifierToneLetters': (u'\uA700', u'\uA71F'),
        'LatinExtended-D': (u'\uA720', u'\uA7FF'),
        'SylotiNagri': (u'\uA800', u'\uA82F'),
        'CommonIndicNumberForms': (u'\uA830', u'\uA83F'),
        'Phags-pa': (u'\uA840', u'\uA87F'),
        'Saurashtra': (u'\uA880', u'\uA8DF'),
        'DevanagariExtended': (u'\uA8E0', u'\uA8FF'),
        'KayahLi': (u'\uA900', u'\uA92F'),
        'Rejang': (u'\uA930', u'\uA95F'),
        'HangulJamoExtended-A': (u'\uA960', u'\uA97F'),
        'Javanese': (u'\uA980', u'\uA9DF'),
        'Cham': (u'\uAA00', u'\uAA5F'),
        'MyanmarExtended-A': (u'\uAA60', u'\uAA7F'),
        'TaiViet': (u'\uAA80', u'\uAADF'),
        'EthiopicExtended-A': (u'\uAB00', u'\uAB2F'),
        'MeeteiMayek': (u'\uABC0', u'\uABFF'),
        #'HangulSyllables': (u'\uAC00', u'\uD7A3'),
        'HangulSyllables': (u'\uAC00', u'\uD7AF'),
        'HangulJamoExtended-B': (u'\uD7B0', u'\uD7FF'),
        'HighSurrogates': (u'\uD800', u'\uDB7F'),
        'LowSurrogates': (u'\uDC00', u'\uDFFF'),
        'CJKCompatibilityIdeographs': (u'\uF900', u'\uFAFF'),
        'AlphabeticPresentationForms': (u'\uFB00', u'\uFB4F'),
        'ArabicPresentationForms-A': (u'\uFB50', u'\uFDFF'),
        'VariationSelectors': (u'\uFE00', u'\uFE0F'),
        'VerticalForms': (u'\uFE10', u'\uFE1F'),
        'CombiningHalfMarks': (u'\uFE20', u'\uFE2F'),
        'CJKCompatibilityForms': (u'\uFE30', u'\uFE4F'),
        'SmallFormVariants': (u'\uFE50', u'\uFE6F'),
        'ArabicPresentationForms-B': (u'\uFE70', u'\uFEFF'),
        'HalfwidthandFullwidthForms': (u'\uFF00', u'\uFFEF'),
    }
    outstr = instr
    for block, limits in UNICODE_BLOCKS.items():
        escaped_is_format = re.escape('{{Is{}}}'.format(block))
        iter = re.finditer('(?<!\\\)(\\\([pP]){})'.format(escaped_is_format),  # noqa: W605,E501
                           outstr)
        for m in iter:
            up, down = limits
            if m.group(2) == 'p':
                block_limit = u'{}-{}'.format(limits[0], limits[1])
            else:
                block_limit = u'\u0000-{}{}-\uFFFF'.format(
                    limits[0], limits[1])
            pre = outstr[:m.span(1)[0]]
            if len(re.findall('(?<!\\\)\[', pre)) == \
                    len(re.findall('(?<!\\\)\]', pre)):  # noqa: W605
                block_limit = u'[{}]'.format(block_limit)
            outstr = pre + block_limit + outstr[m.span(1)[1]:]
    return outstr


def convertHexBinaryLength(base, stName, length, facet):
    try:
        if base == HexBinaryType:
            length = str(2 * int(length))
    except ValueError:
        err_msg(
            '*** warning: simpleType {stName} {facet} '
            '"{length}" is not an integer\n'.format(
                length=length, stName=stName, facet=facet))
    return length


# Generate validation code for each restriction.
# Recursivly call to process possible chain of base types.
def processValidatorBodyRestrictions(
        tree, s1, restrictions, st, ns, stName, base,
        patterns1):
    for restriction in restrictions:
        #
        # pattern
        pats1 = restriction.xpath(
            "./xs:pattern/@value", namespaces=ns)
        if pats1:
            #pats2 = [u'^{}$'.format(replaceVbars(p1)) for p1 in pats1]
            pats2 = [u'^({})$'.format(replaceBlockNames(p1)) for p1 in pats1]
            patterns1.append(pats2)
        #
        # Check for and generate code for each possible type of restriction.
        #
        # enumerations
        stBaseType = find_simple_type_base(base)
        pyType, pyTypeStr = determinePythonType(stBaseType)
        enumerations = restriction.xpath(
            "./xs:enumeration/@value", namespaces=ns)
        if pyType is not None and pyTypeStr != 'str':
            try:
                enumerations = [pyType(item) for item in enumerations]
            except ValueError:
                msg = ("*** Warning.  Can't convert simple type enumeration "
                       "restrictions ({}) "
                       "to target type ({}).\n".format(
                           enumerations, pyTypeStr, ))
                err_msg(msg)
        if enumerations:
            if pyType == decimal_.Decimal:
                items = ['decimal_.Decimal({})'.format(str(item))
                         for item in enumerations]
                enumerationStr = '[{}]'.format(', '.join(items))
            else:
                enumerationStr = "%(enumerations)s" % {
                    'enumerations': enumerations}
            toencode = '% {"value" : encode_str_2_3(value), "lineno": lineno}'
            s1 += "            value = value\n"
            s1 += "            enumerations = %(enumerations)s\n" % {
                'enumerations': enumerationStr}
            s1 += "            if value not in enumerations:\n"
            s1 += "                lineno = self.gds_get_node_lineno_()\n"
            s1 += ("                self.gds_collector_."
                   "add_message('Value \"%(val)s\"%(lineno)s "
                   "does not match xsd enumeration restriction on "
                   "%(typename)s' %(express)s )\n" % {
                       "val": '%(value)s',
                       "lineno": '%(lineno)s',
                       "typename": stName,
                       "express": toencode}
                   )
            s1 += "                result = False\n"
        #
        # maxLength
        maxLength = restriction.xpath(
            "./xs:maxLength/@value", namespaces=ns)
        if maxLength:
            maxLength = maxLength[0]
            maxLength = convertHexBinaryLength(
                base, stName, maxLength, 'maxLength')
            toencode = '% {"value": value, "lineno": lineno}'
            valuestring = '(value)'
            if 'string' in base:
                toencode = ('% {"value" : encode_str_2_3(value), '
                            '"lineno": lineno}')
            s1 += "            if len%(valuestr)s > %(maxLen)s:\n" % {
                'maxLen': maxLength, "valuestr": valuestring}
            s1 += "                lineno = self.gds_get_node_lineno_()\n"
            s1 += ("                self.gds_collector_."
                   "add_message('Value \"%(val)s\"%(lineno)s "
                   "does not match xsd maxLength restriction on "
                   "%(typename)s' %(express)s )\n" % {
                       "val": '%(value)s',
                       "lineno": '%(lineno)s',
                       "typename": stName,
                       "express": toencode}
                   )
            s1 += "                result = False\n"
        #
        # minLength
        minLength = restriction.xpath(
            "./xs:minLength/@value", namespaces=ns)
        if minLength:
            minLength = minLength[0]
            minLength = convertHexBinaryLength(
                base, stName, minLength, 'minLength')
            toencode = '% {"value" : value, "lineno": lineno}'
            valuestring = '(value)'
            if 'string' in base:
                toencode = ('% {"value" : encode_str_2_3(value), '
                            '"lineno": lineno}')
            s1 += "            if len%(valuestr)s < %(minLen)s:\n" % {
                'minLen': minLength, "valuestr": valuestring}
            s1 += "                lineno = self.gds_get_node_lineno_()\n"
            s1 += ("                self.gds_collector_."
                   "add_message('Value \"%(val)s\"%(lineno)s "
                   "does not match xsd minLength restriction on "
                   "%(typename)s' %(express)s )\n" % {
                       "val": '%(value)s',
                       "lineno": '%(lineno)s',
                       "typename": stName,
                       "express": toencode}
                   )
            s1 += "                result = False\n"
        #
        # length
        length = restriction.xpath(
            "./xs:length/@value", namespaces=ns)
        if length:
            length = length[0]
            length = convertHexBinaryLength(base, stName, length, 'length')
            toencode = '% {"value": value, "lineno": lineno}'
            valuestring = '(value)'
            if 'string' in base:
                toencode = ('% {"value": encode_str_2_3(value), '
                            '"lineno": lineno}')
            s1 += "            if len%(valuestring)s != %(length)s:\n" % {
                'length': length, "valuestring": valuestring}
            s1 += "                lineno = self.gds_get_node_lineno_()\n"
            s1 += ("                self.gds_collector_.add_message"
                   "('Value \"%(val)s\"%(lineno)s "
                   "does not match xsd length restriction on "
                   "%(typename)s' %(express)s )\n" % {
                       "val": '%(value)s',
                       "lineno": '%(lineno)s',
                       "typename": stName,
                       "express": toencode}
                   )
            s1 += "                result = False\n"
        #
        # minInclusive
        minInclusive = restriction.xpath(
            "./xs:minInclusive/@value", namespaces=ns)
        if minInclusive:
            minIncl = minInclusive[0]
            minIncl = convertHexBinaryLength(
                base, stName, minIncl, 'minInclusive')
            toencode = '% {"value": value, "lineno": lineno}'
            valuestring = 'value'
            if 'string' in base:
                valuestring = 'len(value)'
                toencode = ('% {"value": encode_str_2_3(value), '
                            '"lineno": lineno}')
            targetValue = get_target_value(minIncl, stName)
            if base in {GYearType, GYearMonthType}:
                s1 += "            if %(valuestring)s < '%(minIncl)s':\n" % {
                    'minIncl': targetValue, "valuestring": valuestring}
            else:
                s1 += "            if %(valuestring)s < %(minIncl)s:\n" % {
                    'minIncl': targetValue, "valuestring": valuestring}
            s1 += "                lineno = self.gds_get_node_lineno_()\n"
            s1 += ("                self.gds_collector_."
                   "add_message('Value \"%(val)s\"%(lineno)s "
                   "does not match xsd minInclusive restriction on "
                   "%(typename)s' %(express)s )\n" % {
                       "val": '%(value)s',
                       "lineno": '%(lineno)s',
                       "typename": stName,
                       "express": toencode}
                   )
            s1 += "                result = False\n"
        #
        # maxInclusive
        maxInclusive = restriction.xpath(
            "./xs:maxInclusive/@value", namespaces=ns)
        if maxInclusive:
            maxIncl = maxInclusive[0]
            maxIncl = convertHexBinaryLength(
                base, stName, maxIncl, 'maxInclusive')
            toencode = '% {"value": value, "lineno": lineno}'
            valuestring = 'value'
            if 'string' in base:
                valuestring = 'len(value)'
                toencode = ('% {"value": encode_str_2_3(value), '
                            '"lineno": lineno}')
            targetValue = get_target_value(maxIncl, stName)
            if base in {GYearType, GYearMonthType}:
                s1 += "            if %(valuestring)s > '%(maxIncl)s':\n" % {
                    'maxIncl': targetValue, "valuestring": valuestring}
            else:
                s1 += "            if %(valuestring)s > %(maxIncl)s:\n" % {
                    'maxIncl': targetValue, "valuestring": valuestring}
            s1 += "                lineno = self.gds_get_node_lineno_()\n"
            s1 += ("                self.gds_collector_."
                   "add_message('Value \"%(val)s\"%(lineno)s "
                   "does not match xsd maxInclusive restriction on "
                   "%(typename)s' %(express)s )\n" % {
                       "val": '%(value)s',
                       "lineno": '%(lineno)s',
                       "typename": stName,
                       "express": toencode}
                   )
            s1 += "                result = False\n"
        #
        # minExclusive
        minExclusive = restriction.xpath(
            "./xs:minExclusive/@value", namespaces=ns)
        if minExclusive:
            minExclusive = minExclusive[0]
            minExclusive = convertHexBinaryLength(
                base, stName, minExclusive, 'minExclusive')
            toencode = '% {"value": value, "lineno": lineno}'
            valstr = 'value'
            if 'string' in base:
                valstr = 'len(value)'
                toencode = ('% {"value": encode_str_2_3(value), '
                            '"lineno": lineno}')
            targetValue = get_target_value(minExclusive, stName)
            if base in {GYearType, GYearMonthType}:
                s1 += "            if %(valstr)s <= '%(minExclusive)s':\n" % {
                    'minExclusive': targetValue, "valstr": valstr}
            else:
                s1 += "            if %(valstr)s <= %(minExclusive)s:\n" % {
                    'minExclusive': targetValue, "valstr": valstr}
            s1 += "                lineno = self.gds_get_node_lineno_()\n"
            s1 += ("                self.gds_collector_."
                   "add_message('Value \"%(val)s\"%(lineno)s "
                   "does not match xsd minExclusive restriction on "
                   "%(typename)s' %(express)s )\n" % {
                       "val": '%(value)s',
                       "lineno": '%(lineno)s',
                       "typename": stName,
                       "express": toencode}
                   )
            s1 += "                result = False\n"
        #
        # maxExclusive
        maxExclusive = restriction.xpath(
            "./xs:maxExclusive/@value", namespaces=ns)
        if maxExclusive:
            maxExclusive = maxExclusive[0]
            maxExclusive = convertHexBinaryLength(
                base, stName, maxExclusive, 'maxExclusive')
            toencode = '% {"value": value, "lineno": lineno}'
            valstr = 'value'
            if 'string' in base:
                valstr = 'len(value)'
                toencode = ('% {"value": encode_str_2_3(value), '
                            '"lineno": lineno}')
            targetValue = get_target_value(maxExclusive, stName)
            if base in {GYearType, GYearMonthType}:
                s1 += "            if %(valstr)s >= '%(maxExclusive)s':\n" % {
                    'maxExclusive': targetValue, "valstr": valstr}
            else:
                s1 += "            if %(valstr)s >= %(maxExclusive)s:\n" % {
                    'maxExclusive': targetValue, "valstr": valstr}
            s1 += "                lineno = self.gds_get_node_lineno_()\n"
            s1 += ("                self.gds_collector_."
                   "add_message('Value \"%(val)s\"%(lineno)s "
                   "does not match xsd maxExclusive restriction on "
                   "%(typename)s' %(express)s )\n" % {
                       "val": '%(value)s',
                       "lineno": '%(lineno)s',
                       "typename": stName,
                       "express": toencode}
                   )
            s1 += "                result = False\n"
        #
        # totalDigits
        totalDigits = restriction.xpath(
            "./xs:totalDigits/@value", namespaces=ns)
        if totalDigits:
            totalDigits = totalDigits[0]
            toencode = '% {"value": value, "lineno": lineno}'
            valstr = '(str(value))'
            if 'string' in base:
                valstr = '(value)'
                toencode = ('% {"value": encode_str_2_3(value), '
                            '"lineno": lineno}')
            s1 += "            if len%(valstr)s >= %(totalDigits)s:\n" % {
                'totalDigits': totalDigits, "valstr": valstr}
            s1 += "                lineno = self.gds_get_node_lineno_()\n"
            s1 += ("                self.gds_collector_."
                   "add_message('Value \"%(val)s\"%(lineno)s "
                   "does not match xsd totalDigits restriction on "
                   "%(typename)s' %(express)s )\n" % {
                       "val": '%(value)s',
                       "lineno": '%(lineno)s',
                       "typename": stName,
                       "express": toencode}
                   )
            s1 += "                result = False\n"
        #
        # Recurse into base simpleType, if it exists.
        base1 = restriction.get('base')
        if base1 is not None:
            #base1 = lookup_prefix_and_name(base1)
            if ":" in base1:
                base1 = base1.split(":")[1]
            # Check special case: simpletype that restricts xs:simpletype.
            # Prevent infinite recursion.
            if st.get('name') != base1:
                st1 = find_simple_type_def(tree, base1, None, None, ns, base)
                if st1 is not None:
                    restrictions1 = st1.xpath(
                        "./xs:restriction",
                        namespaces=ns, n=stName, b=base)
                    if restrictions1:
                        s2 = processValidatorBodyRestrictions(
                            tree, '', restrictions1, st1, ns, stName,
                            base1, patterns1)
                        s1 += s2
    return s1
# end processValidatorBodyRestrictions


def lookup_prefix_and_name(prefix_name):
    prefix, name = get_prefix_and_value(prefix_name)
    key = '{%s}%s' % (prefix, name, )
    if SchemaRenameMap is not None and key in SchemaRenameMap:
        name = SchemaRenameMap.get(key)
    return name


def find_simple_type_base(base, element=None):
    stBaseType = base
    loopCount = 0
    while loopCount <= 100:
        loopCount += 1
        typeSpec = stBaseType
        if stBaseType is None:
            break
        if ":" not in stBaseType and XsdNameSpace:
            typeSpec = "{}:{}".format(XsdNameSpace, typeSpec)
        if typeSpec in OtherSimpleTypes:
            break
        else:
            stBaseType = lookup_prefix_and_name(stBaseType)
            items = SchemaLxmlTree.xpath(
                './/xs:simpleType[@name=$typename]/xs:restriction',
                namespaces=SchemaLxmlTreeMap,
                typename=stBaseType)
            # Lxml Xpath does not seem to handle alternative (X|Y)
            # expressions.  If we need to search for xs:union,
            # we search again and append.
            #
            # We do not know how to handle xs:union at this level.
            # A union that has base types that has unions etc is too
            # complicated.
            #
            #if not items:
            #    items += SchemaLxmlTree.xpath(
            #        './/xs:simpleType[@name=$typename]/xs:union',
            #        namespaces=SchemaLxmlTreeMap,
            #        typename=stBaseType)
            if items:
                item = items[0]
                stBaseType = item.get('base')
            else:
                stBaseType = None
    else:
        elementName = "<unknown>"
        if element:
            elementName = element.getName()
        err_msg("*** warning.  Loop limit exceeded.  Cannot find base "
                "simple type for element: {}\n".format(elementName))
        stBaseType = None
    return stBaseType


def determinePythonType(stBaseType):
    pyType = None
    pyTypeStr = None
    if stBaseType is not None:
        if XsdNameSpace and ":" not in stBaseType:
            stBaseType = "{}:{}".format(XsdNameSpace, stBaseType)
        if not stBaseType:
            pass
        elif (stBaseType in StringType or
                stBaseType == TokenType):
            pyType = str
            pyTypeStr = 'str'
        elif stBaseType == DateTimeType:
            pyTypeStr = 'datetime_.datetime'
        elif stBaseType == DateType:
            pyTypeStr = 'datetime_.date'
        elif stBaseType == TimeType:
            pyTypeStr = 'datetime_.time'
        elif (stBaseType in IntegerType or
                stBaseType == PositiveIntegerType or
                stBaseType == NonPositiveIntegerType or
                stBaseType == NegativeIntegerType or
                stBaseType == NonNegativeIntegerType):
            pyType = int
            pyTypeStr = 'int'
        elif stBaseType == FloatType or stBaseType == DoubleType:
            pyType = float
            pyTypeStr = 'float'
        elif stBaseType == DecimalType:
            pyType = decimal_.Decimal
            pyTypeStr = 'decimal_.Decimal'
    return pyType, pyTypeStr


def generateTypeValidationForSimpleType(base, element):
    str1 = ''
    stBaseType = find_simple_type_base(base, element)
    _, pyTypeStr = determinePythonType(stBaseType)
    if pyTypeStr:
        str1 += "            if not isinstance(value, %s):\n" % (pyTypeStr, )
        str1 += "                lineno = self.gds_get_node_lineno_()\n"
        str1 += ("                self.gds_collector_."
                 "add_message('Value \"%%(value)s\"%%(lineno)s is "
                 "not of the correct base simple type (%s)' %% "
                 "{\"value\": value, \"lineno\": lineno, })\n" % (pyTypeStr, ))
        str1 += "                return False\n"
    return str1


# Generate validator method bodies.
def getValidatorBody(stName, base, element, child):
    s1 = None
    patterns1 = ''
    if not UseOldSimpleTypeValidators and SchemaLxmlTree is not None:
        # generate validator bodies directly from the XML schema.
        ns = {'xs': 'http://www.w3.org/2001/XMLSchema'}
        tree = SchemaLxmlTree
        # on determine l elemnt ou le type est definit
        st = find_simple_type_def(tree, stName, element, child, ns, base)
        if st is not None:
            restrictions = st.xpath(
                "./xs:restriction",
                namespaces=ns, n=stName, b=base)
            # une liste qui contient les restrictions deja traitees
            if restrictions:
                s1 = ('        if value is not None and '
                      'Validate_simpletypes_ and '
                      'self.gds_collector_ is not None:\n')
                s1 += generateTypeValidationForSimpleType(base, element)
                initial_len = len(s1)
                patterns1 = []
                s1 = processValidatorBodyRestrictions(
                    tree, s1, restrictions, st, ns, stName, base,
                    patterns1)
                if len(s1) == initial_len and not patterns1:
                    s1 += '            pass\n'
        if s1 is None:
            s1 = '        pass\n'
        return s1, patterns1
    #
    # if UseOldSimpleTypeValidators
    else:
        # Generate validator bodies from user code.
        retrieved = 0
        if ValidatorBodiesBasePath:
            found = 0
            path = '%s%s%s.py' % (ValidatorBodiesBasePath, os.sep, stName, )
            if os.path.exists(path):
                found = 1
            else:
                path = '%s%s%s' % (ValidatorBodiesBasePath, os.sep, stName, )
                if os.path.exists(path):
                    found = 1
            if found:
                infile = open(path, 'r')
                lines = infile.readlines()
                infile.close()
                lines1 = []
                for line in lines:
                    if not line.startswith('##'):
                        lines1.append(line)
                s1 = ''.join(lines1)
                retrieved = 1
        if not retrieved:
            s1 = '        pass\n'
        return s1, None
# end getValidatorBody


NsGetterSetterBodies = """\
    def get_ns_prefix_(self):
        return self.ns_prefix_
    def set_ns_prefix_(self, ns_prefix):
        self.ns_prefix_ = ns_prefix
"""


# Generate get/set/add/insert member functions.
def generateGettersAndSetters(wrt, element):
    if not XmlDisabled:
        wrt(NsGetterSetterBodies)
    for child in element.getChildren():
        if child.getType() == AnyTypeIdentifier:
            wrt('    def get_anytypeobjs_(self): return self.anytypeobjs_\n')
            wrt('    def set_anytypeobjs_('
                'self, anytypeobjs_): self.anytypeobjs_ = anytypeobjs_\n')
            if child.getMaxOccurs() > 1:
                wrt('    def add_anytypeobjs_(self, value): '
                    'self.anytypeobjs_.append(value)\n')
                wrt('    def insert_anytypeobjs_(self, index, value): '
                    'self._anytypeobjs_[index] = value\n')
        else:
            name = cleanupName(child.getCleanName())
            unmappedName = cleanupName(child.getName())
            capName = make_gs_name(unmappedName)
            wrt('    def get%s(self):\n'
                #'        pass\n'    # add custom code here for getter
                '        return self.%s\n' % (capName, name))
            wrt('    def set%s(self, %s):\n'
                #'        pass\n'    # add custom code here for setter
                '        self.%s = %s\n' % (
                    capName, name, name, name))
            childType = child.getType()
            type_obj = ElementDict.get(childType)
            if (type_obj is not None and
                    type_obj.getExtended() and
                    type_obj.isAbstract()):
                suffix = make_gs_name('with_type')
                originalTagname = child.getName()
                extensionType = 'value.__class__.__name__'
                wrt("    def set%s%s(self, value):\n"
                    "        self.%s = value\n"
                    "        value.original_tagname_ = '%s'\n"
                    "        value.extensiontype_ = %s\n" % (
                        capName, suffix, name,
                        originalTagname, extensionType))
            if child.getMaxOccurs() > 1:
                wrt('    def add%s(self, value):\n'
                    '        self.%s.append(value)\n' % (
                        capName, name))
                if (type_obj is not None and
                        type_obj.getExtended() and
                        type_obj.isAbstract()):
                    suffix = make_gs_name('with_type')
                    originalTagname = child.getName()
                    extensionType = 'value.__class__.__name__'
                    wrt("    def add%s%s(self, value):\n"
                        "        self.%s.append(value)\n"
                        "        value.original_tagname_ = '%s'\n"
                        "        value.extensiontype_ = %s\n" % (
                            capName, suffix, name,
                            originalTagname, extensionType))
                suffix = make_gs_name('at')
                wrt('    def insert%s%s(self, index, value):\n'
                    '        self.%s.insert(index, value)\n' %
                    (capName, suffix, name))
                wrt('    def replace%s%s(self, index, value):\n'
                    '        self.%s[index] = value\n' %
                    (capName, suffix, name))
            if GenerateProperties:
                wrt('    %sProp = property(get%s, set%s)\n' %
                    (unmappedName, capName, capName))
    attrDefs = element.getAttributeDefs()
    for key in element.getAttributeDefsList():
        attrDef = attrDefs[key]
        name = cleanupName(attrDef.getName().replace(':', '_'))
        mappedName = mapName(name)
        wrt('    def get%s(self):\n'
            #'        pass\n'    # add custom code here for getter
            '        return self.%s\n' %
            (make_gs_name(name), mappedName))
        gsName = make_gs_name(name)
        wrt('    def set%s(self, %s):\n'
            #'        pass\n'    # add custom code here for setter
            '        self.%s = %s\n' % (
                gsName, mappedName, mappedName, mappedName))
        if GenerateProperties:
            wrt('    %sProp = property(get%s, set%s)\n' %
                (name, gsName, gsName))
    if element.getSimpleContent() or element.isMixed():
        wrt('    def get%s_(self): return self.valueOf_\n' % (
            make_gs_name('valueOf'), ))
        wrt('    def set%s_(self, valueOf_): self.valueOf_ = valueOf_\n' % (
            make_gs_name('valueOf'), ))
    if element.getAnyAttribute():
        wrt('    def get%s_(self): return self.anyAttributes_\n' % (
            make_gs_name('anyAttributes'), ))
        wrt('    def set%s_(self, anyAttributes_): '
            'self.anyAttributes_ = anyAttributes_\n' %
            (make_gs_name('anyAttributes'), ))
    if element.getExtended():
        wrt('    def get%s_(self): return self.extensiontype_\n' % (
            make_gs_name('extensiontype'), ))
        wrt('    def set%s_(self, extensiontype_): '
            'self.extensiontype_ = extensiontype_\n' %
            (make_gs_name('extensiontype'), ))
# end generateGettersAndSetters


# Generate validator methods.
def generateValidatorDefs(wrt, element):
    generatedSimpleTypes = []
    for child in element.getChildren():
        #
        # If this child is defined in a simpleType, then generate
        #   a validator method.
        typeName = child.getSimpleType()
        if (typeName and
                typeName in SimpleTypeDict and
                typeName not in generatedSimpleTypes):
            cleanTypeName = cleanupName(typeName)
            generatedSimpleTypes.append(typeName)
            wrt('    def validate_%s(self, value):\n' % (
                cleanupName(typeName), ))
            wrt('        result = True\n')
            if typeName in SimpleTypeDict:
                stObj = SimpleTypeDict[typeName]
                wrt('        # Validate type %s, a restriction '
                    'on %s.\n' %
                    (typeName, stObj.getBase(), ))
            else:
                wrt('        # validate type %s\n' % (typeName, ))
            body, patterns = getValidatorBody(
                typeName, stObj.getBase(), element, child)
            wrt(body)
            if patterns:
                if stObj.getBase() in Date_Time_DateTime_Type:
                    wrt("            value = str(value)\n")
                wrt('            if not self.gds_validate_simple_patterns(\n')
                wrt('                    self.validate_%s_patterns_, '
                    'value):\n' % (cleanTypeName,))
                s1 = ("                self.gds_collector_."
                      "add_message('Value \"%%s\" "
                      "does not match xsd pattern restrictions: %%s' "
                      "%% (encode_str_2_3(value), "
                      "self.validate_%s_patterns_, ))\n" % (cleanTypeName,)
                      )
                wrt(s1)
                wrt('                result = False\n')
            wrt('        return result\n')
            if patterns:
                wrt('    validate_%s_patterns_ = %s\n' % (
                    cleanTypeName, patterns,))
    if not len(element.getChildren()):
        # Does it have simple content?
        simpleBase = element.getSimpleBase()
        if len(simpleBase) > 0:
            typeName = simpleBase[0]
            if (typeName in SimpleTypeDict and
                    typeName not in generatedSimpleTypes):
                stObj = SimpleTypeDict.get(typeName)
                wrt('    def validate_%s(self, value):\n' % (
                    cleanupName(typeName),))
                wrt('        result = True\n')
                if typeName in SimpleTypeDict:
                    stObj = SimpleTypeDict[typeName]
                    if stObj and stObj.getBase() != Base64Type:
                        wrt('        # Validate type %s, a restriction '
                            'on %s.\n' %
                            (typeName, stObj.getBase(),))
                else:
                    wrt('        # validate type %s\n' % (typeName,))
                body, patterns = getValidatorBody(
                    typeName, stObj.getBase(), element, None)
                if body:
                    if stObj and stObj.getBase() != Base64Type:
                        wrt(body)
                if patterns:
                    if stObj.getBase() in Date_Time_DateTime_Type:
                        wrt("            value = str(value)\n")
                    wrt('            if not self.'
                        'gds_validate_simple_patterns(\n')
                    wrt('                    self.validate_%s_patterns_, '
                        'value):\n' % (cleanupName(typeName),))
                    s1 = ("                self.gds_collector_."
                          "add_message('Value \"%%s\" "
                          "does not match xsd pattern restrictions: %%s' "
                          "%% (encode_str_2_3(value), "
                          "self.validate_%s_patterns_, ))\n" % (
                              cleanupName(typeName),)
                          )
                    wrt(s1)
                    wrt('                result = False\n')
                if body or patterns:
                    wrt('        return result\n')
                if patterns:
                    wrt('    validate_%s_patterns_ = %s\n' % (
                        cleanupName(typeName), patterns,))
    attrDefs = element.getAttributeDefs()
    for key in element.getAttributeDefsList():
        attrDef = attrDefs[key]
        typeName = attrDef.getType()
        orig_typeName = typeName
        typeName1 = typeName.split(':')
        if len(typeName1) == 2:
            typeName = typeName1[1]
#        typeName = lookup_prefix_and_name(typeName)
        if (typeName and
                typeName in SimpleTypeDict and
                typeName not in generatedSimpleTypes):
            cleanTypeName = cleanupName(typeName)
            generatedSimpleTypes.append(typeName)
            wrt('    def validate_%s(self, value):\n' % (
                cleanupName(typeName), ))
            if typeName in SimpleTypeDict:
                stObj = SimpleTypeDict[typeName]
                wrt('        # Validate type %s, a restriction on %s.\n' % (
                    orig_typeName, stObj.getBase(), ))
            else:
                wrt('        # validate type %s\n' % (typeName, ))
            body, patterns = getValidatorBody(
                typeName, stObj.getBase(), None, None)
            wrt(body)
            if patterns:
                if stObj.getBase() in Date_Time_DateTime_Type:
                    wrt("            value = str(value)\n")
                wrt('            if not self.gds_validate_simple_patterns(\n')
                wrt('                    self.validate_%s_patterns_, '
                    'value):\n' % (cleanTypeName, ))
                s1 = ("                self.gds_collector_."
                      "add_message('Value \"%%s\" "
                      "does not match xsd pattern restrictions: %%s' "
                      "%% (encode_str_2_3(value), "
                      "self.validate_%s_patterns_, ))\n" % (cleanTypeName, )
                      )
                wrt(s1)
                wrt('    validate_%s_patterns_ = %s\n' % (
                    cleanTypeName, patterns, ))
# end generateValidatorDefs


#
# Generate a class variable whose value is a list of tuples, one
#   tuple for each member data item of the class.
#   Each tuple has 5 or 6 elements: (1) member name, (2) member data type,
#   (3) container/list or not (maxoccurs > 1), (4) optional,
#   (5) attributes dictionary, (6) choice group.
def generateMemberSpec(wrt, element):
    generateDict = MemberSpecs and MemberSpecs == 'dict'
    if generateDict:
        content = ['    member_data_items_ = {']
    else:
        content = ['    member_data_items_ = [']
    add = content.append
    attrDefs = element.getAttributeDefs()
    for attrName in element.getAttributeDefsList():
        attrDef = attrDefs[attrName]
        item0 = mapName(attrName)
        item1 = cleanupName(item0)
        item2 = attrDef.getType()
        item3 = 0
        item4 = 1 if attrDef.getUse() == 'optional' else 0

        # Renders attr def as a dict without 'u' prefix
        if sys.version_info.major >= 3:
            attrDefStr = "{'use': " + repr(attrDef.getUse()) + ", 'name': '" + item0 + "'}"
        else:
            attrDefStr = ("{'use': " +
                          repr(unicode(attrDef.getUse()).encode('utf8')) +
                          ", 'name': '" + item0 + "'}")
        if generateDict:
            item = "        '%s': MemberSpec_('%s', '%s', %d, %d, %s)," % (
                item1, item1, item2, item3, item4, attrDefStr)
        else:
            item = "        MemberSpec_('%s', '%s', %d, %d, %s)," % (
                item1, item2, item3, item4, attrDefStr)
        add(item)
    for child in element.getChildren():
        name = cleanupName(child.getCleanName())
        if not name and child.type == AnyTypeIdentifier:
            item1 = AnyTypeIdentifier
        else:
            item1 = name
        simplebase = child.getSimpleBase()
        if item1 == AnyTypeIdentifier:
            item2 = "'%s'" % AnyTypeIdentifier
        elif simplebase:
            if len(simplebase) == 1:
                item2 = "'%s'" % (simplebase[0], )
            else:
                item2 = simplebase
        else:
            element1 = ElementDict.get(name)
            if element1:
                item2 = "'%s'" % element1.getType()
            else:
                item2 = "'%s'" % (child.getType(), )
        if child.getMaxOccurs() > 1:
            item3 = 1
        else:
            item3 = 0
        item4 = 1 if child.getOptional() else 0

        # Renders child attrs as a sorted dict without 'u' prefix
        if sys.version_info.major == 2:
            child_attrs = [
                repr(k.encode('utf8')) + ": " + repr(v.encode('utf8'))
                for k, v in child.getAttrs().items()]
        else:
            child_attrs = [
                repr(k) + ": " + repr(v)
                for k, v in child.getAttrs().items()]
        child_attrs = sorted(child_attrs)
        child_attrs = "{" + ', '.join(child_attrs) + '}'

        if generateDict:
            item = "        '%s': MemberSpec_('%s', %s, %d, %d, %s, %s)," % (
                item1, item1, item2, item3, item4, child_attrs,
                child.choice.getChoiceGroup() if child.choice else None)
        else:
            item = "        MemberSpec_('%s', %s, %d, %d, %s, %s)," % (
                item1, item2, item3, item4, child_attrs,
                child.choice.getChoiceGroup() if child.choice else None)
        add(item)
    simplebase = element.getSimpleBase()
    if element.getSimpleContent() or element.isMixed():
        if len(simplebase) == 1:
            simplebase = "'%s'" % (simplebase[0], )
        if generateDict:
            item = "        'valueOf_': MemberSpec_('valueOf_', %s, 0)," % (
                simplebase, )
        else:
            item = "        MemberSpec_('valueOf_', %s, 0)," % (
                simplebase, )
        add(item)
    elif element.isMixed():
        if generateDict:
            item = "        'valueOf_': MemberSpec_('valueOf_', '%s', 0)," % (
                'xs:string', )
        else:
            item = "        MemberSpec_('valueOf_', '%s', 0)," % (
                'xs:string', )
        add(item)
    if generateDict:
        add('    }')
    else:
        add('    ]')
    wrt('\n'.join(content))
    wrt('\n')
# end generateMemberSpec


#
# Generate a class variable for holding the slots
def generateSlots(wrt, element):
    additional_members = set()
    eltype = element.getType()
    if (element.getSimpleContent() or
            element.isMixed() or
            eltype in SimpleTypeDict or
            CurrentNamespacePrefix + eltype in OtherSimpleTypes):
        additional_members.add("valueOf_")
    if element.getAnyAttribute():
        additional_members.add("anyAttributes_")
    if element.getExtended():
        additional_members.add("extensiontype_")
    if element.isMixed():
        additional_members.update(("mixedclass_", "content_", "valueOf_"))
    content = "    __slots__ = GeneratedsSuper.gds_subclass_slots(" \
        "member_data_items_)"
    if len(additional_members) > 0:
        content += " + ['%s']" % "', '".join(sorted(additional_members))
    wrt(content)
    wrt('\n')
# end generateSlots


def generateUserMethods(wrt, element):
    if not UserMethodsModule:
        return
    specs = UserMethodsModule.METHOD_SPECS
    name = cleanupName(element.getCleanName())
    values_dict = {'class_name': name, }
    for spec in specs:
        if spec.match_name(name):
            source = spec.get_interpolated_source(values_dict)
            wrt(source)


def generateHascontentMethod(wrt, prefix, element):
    wrt('    def _hasContent(self):\n')
    wrt('        if (\n')
    firstTime = True
    for child in element.getChildren():
        if child.getType() == AnyTypeIdentifier:
            name = 'anytypeobjs_'
        else:
            name = child.getCleanName()
        if not firstTime:
            wrt(' or\n')
        firstTime = False
        if child.getMaxOccurs() > 1:
            wrt('            self.%s' % (name, ))
        else:
            default = child.getDefault()
            if default is None:
                wrt('            self.%s is not None' % (name, ))
            else:
                child_type = child.getType()
                target_base_type = None
                if child_type in ElementDict:
                    target_type = ElementDict.get(child_type)
                    target_base_type = target_type.getSimpleBase()
                if target_base_type:
                    # Perhaps it has xs:simpleContent.
                    wrt('            self.%s is not None' % (name, ))
                elif (child_type in StringType or
                        child_type == TokenType or
                        child_type in DateTimeGroupType):
                    wrt('            self.%s != "%s"' % (name, default, ))
                elif child_type == BooleanType:
                    if default == 'true':
                        wrt('            not self.%s' % (name, ))
                    elif default == 'false':
                        wrt('            self.%s' % (name, ))
                    else:
                        wrt('            self.%s is not None' % (name, ))
                else:
                    wrt('            self.%s != %s' % (name, default, ))
    if element.getSimpleContent() or element.isMixed():
        if not firstTime:
            wrt(' or\n')
        firstTime = False
        wrt('            (1 if type(self.valueOf_) '
            'in [int,float] else self.valueOf_)')
        if element.isMixed():
            wrt(' or\n')
            wrt('            self.content_')
    parentName, parent = getParentName(element)
    if parentName:
        elName = element.getCleanName()
        if not firstTime:
            wrt(' or\n')
        firstTime = False
        wrt('            super(%s%s, self)._hasContent()' % (prefix, elName, ))
    wrt('\n        ):\n')
    wrt('            return True\n')
    wrt('        else:\n')
    wrt('            return False\n')


FactoryMethodTemplate = """\
    def factory(*args_, **kwargs_):
        if CurrentSubclassModule_ is not None:
            subclass = getSubclassFromModule_(
                CurrentSubclassModule_, {prefix}{name})
            if subclass is not None:
                return subclass(*args_, **kwargs_)
        if {prefix}{name}.subclass:
            return {prefix}{name}.subclass(*args_, **kwargs_)
        else:
            return {prefix}{name}(*args_, **kwargs_)
"""


def generateDocString(element):
    if not element.documentation:
        return None
    docStr = element.documentation
    items = docStr.split("x<>x")
    items2 = []
    for item in items:
        if item.strip():
            items2.append(item.rstrip())
    for idx, item in enumerate(items2):
        if item.startswith('y<>y'):
            items2[idx] = '* ' + items2[idx][4:]
        elif item.startswith('z<>z'):
            items2[idx] = '  ' + items2[idx][4:].strip()
    items3 = []
    for idx, item in enumerate(items2):
        if item.strip():
            items3.append(item)
        elif (idx < (len(items2) - 1) and
              items2[idx + 1].startswith('* ')):
            items3.append(item)
    for idx, line in enumerate(items3):
        if not line.strip():
            break
        items3[idx] = line[2:]
    items4 = []
    for idx, line in enumerate(items3):
        if idx == 0:
            items4.append('    """%s' % line)
        else:
            items4.append('    %s' % line)
    items4.append('    ')
    items4.append('    """\n')
    docStr1 = '\n'.join(items4)
    return docStr1


def generateClasses(wrt, prefix, element, delayed, nameSpacesDef=''):
    _log.debug(
        'ENTER, prefix: "%s", element: "%s", delayed: "%s", NS Def: "%s"',
        prefix, element, delayed, nameSpacesDef)
    mappedName = element.getFullyQualifiedName()
    parentName, base = getParentName(element)
    _log.debug("Element base: %s", base)
    if not element.isExplicitDefine():
        _log.debug("Not an explicit define, returning.")
        if element.isComplex() and element.getName() != element.getType():
            MappingTypes[element.getName()] = element.getType()
        return
    # If this element is an extension (has a base) and the base has
    #   not been generated, then postpone it.
    if parentName:
        parentFQN = base.getFullyQualifiedName()
        if parentFQN not in AlreadyGenerated:
            PostponedExtensions.append(element)
            _log.debug("Postponing the class %s since its parent "
                       "has not been generated", mappedName)
            return
    if mappedName in AlreadyGenerated:
        _log.debug("The class for %s has already been generated", mappedName)
        return
    AlreadyGenerated.add(mappedName)
    if element.getMixedExtensionError():
        err_msg('*** Element %s extension chain contains mixed and '
                'non-mixed content.  Not generated.\n' %
                (element.getName(), ))
        return
    ElementsForSubclasses.append(element)
    name = element.getCleanName()
    if parentName:
        s1 = 'class %s%s(%s%s):\n' % (
            prefix, name, prefix, mapName(cleanupName(base.getType())),)
    else:
        s1 = 'class %s%s(GeneratedsSuper):\n' % (prefix, name)
    wrt(s1)
    # If this element has documentation, generate a doc-string.
    s2 = generateDocString(element)
    if s2:
        wrt(s2)
    # copy __hash__ method from the superclass
    wrt("    __hash__ = GeneratedsSuper.__hash__\n")
    if UserMethodsModule or MemberSpecs:
        generateMemberSpec(wrt, element)
    if UseSlots:
        generateSlots(wrt, element)
    wrt('    subclass = None\n')
    parentName, parent = getParentName(element)
    superclass_name = 'None'
    if parentName and parent.getFullyQualifiedName() in AlreadyGenerated:
        superclass_name = prefix + parentName
    wrt('    superclass = %s\n' % (superclass_name, ))

    # create reverse dict of known namespace mappings
    r_nsdict = {}
    if len(nameSpacesDef) > 0:
        for nsdesc in nameSpacesDef.split():
            ns, uri = nsdesc.split('=')
            ns, uri = ns[6:], uri.replace('"', '')
            r_nsdict[uri] = ns

    generateCtor(wrt, prefix, element, r_nsdict)
    wrt(FactoryMethodTemplate.format(prefix=prefix, name=name))
    wrt('    factory = staticmethod(factory)\n')
    if UseGetterSetter != 'none':
        generateGettersAndSetters(wrt, element)
    generateValidatorDefs(wrt, element)
    if element.namespace:
        namespace = element.namespace
    elif element.targetNamespace in NamespacesDict:
        namespace = NamespacesDict[element.targetNamespace]
    elif Targetnamespace in NamespacesDict:
        namespace = NamespacesDict[Targetnamespace]
    else:
        namespace = ''
    generateHascontentMethod(wrt, prefix, element)
    if not XmlDisabled:
        if ExportWrite:
            generateExportFn(wrt, prefix, element, namespace, nameSpacesDef)
        if ExportEtree:
            generateToEtree(wrt, element, Targetnamespace)
        if ExportLiteral:
            generateExportLiteralFn(wrt, prefix, element)
        if ExportDjango:
            generateExportDjangoFn(wrt, element)
        if ExportSQLAlchemy:
            generateExportSQLAlchemyFn(wrt, element)
    if GenerateValidatorMethods:
        generateValidatorMethods(wrt, element)
    if GenerateRecursiveGenerator:
        generateRecursiveGenerator(wrt, element)
    if not XmlDisabled:
        generateBuildFn(wrt, prefix, element, delayed)
    generateUserMethods(wrt, element)
    wrt('# end class %s%s\n' % (prefix, name, ))
    wrt('\n\n')
    _log.debug("Finished generating the class %s", name)
    AllGeneratedClassNames.add(name)
# end generateClasses


TEMPLATE_HEADER = """\
#xmldisable##!/usr/bin/env python
# -*- coding: utf-8 -*-

#
# Generated {tstamp} by generateDS.py{version}.
# Python {pyversion}
#
# Command line options:
{options1}
#
# Command line arguments:
#   {args1}
#
# Command line:
#   {command_line}
#
# Current working directory (os.getcwd()):
#   {current_working_directory}
#

import sys
try:
    ModulenotfoundExp_ = ModuleNotFoundError
except NameError:
    ModulenotfoundExp_ = ImportError
{itertools_import}
import os
import re as re_
import base64
{db_orm_import}import datetime as datetime_
import decimal as decimal_
#xmldisable#from lxml import etree as etree_

{custom_imports}
Validate_simpletypes_ = True
SaveElementTreeNode = True
TagNamePrefix = "{prefix}"
if sys.version_info.major == 2:
    BaseStrType_ = basestring
else:
    BaseStrType_ = str


#xmldisable#def parsexml_(infile, parser=None, **kwargs):
#xmldisable#    if parser is None:
#xmldisable#        # Use the lxml ElementTree compatible parser so that, e.g.,
#xmldisable#        #   we ignore comments.
#xmldisable#        try:
#xmldisable#            parser = etree_.ETCompatXMLParser()
#xmldisable#        except AttributeError:
#xmldisable#            # fallback to xml.etree
#xmldisable#            parser = etree_.XMLParser()
#xmldisable#    try:
#xmldisable#        if isinstance(infile, os.PathLike):
#xmldisable#            infile = os.path.join(infile)
#xmldisable#    except AttributeError:
#xmldisable#        pass
#xmldisable#    doc = etree_.parse(infile, parser=parser, **kwargs)
#xmldisable#    return doc

#xmldisable#def parsexmlstring_(instring, parser=None, **kwargs):
#xmldisable#    if parser is None:
#xmldisable#        # Use the lxml ElementTree compatible parser so that, e.g.,
#xmldisable#        #   we ignore comments.
#xmldisable#        try:
#xmldisable#            parser = etree_.ETCompatXMLParser()
#xmldisable#        except AttributeError:
#xmldisable#            # fallback to xml.etree
#xmldisable#            parser = etree_.XMLParser()
#xmldisable#    element = etree_.fromstring(instring, parser=parser, **kwargs)
#xmldisable#    return element

#
# Namespace prefix definition table (and other attributes, too)
#
# The module generatedsnamespaces, if it is importable, must contain
# a dictionary named GeneratedsNamespaceDefs.  This Python dictionary
# should map element type names (strings) to XML schema namespace prefix
# definitions.  The export method for any class for which there is
# a namespace prefix definition, will export that definition in the
# XML representation of that element.  See the export method of
# any generated element type class for an example of the use of this
# table.
# A sample table is:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceDefs = {{
#         "ElementtypeA": "http://www.xxx.com/namespaceA",
#         "ElementtypeB": "http://www.xxx.com/namespaceB",
#     }}
#
# Additionally, the generatedsnamespaces module can contain a python
# dictionary named GenerateDSNamespaceTypePrefixes that associates element
# types with the namespace prefixes that are to be added to the
# "xsi:type" attribute value.  See the _exportAttributes method of
# any generated element type and the generation of "xsi:type" for an
# example of the use of this table.
# An example table:
#
#     # File: generatedsnamespaces.py
#
#     GenerateDSNamespaceTypePrefixes = {{
#         "ElementtypeC": "aaa:",
#         "ElementtypeD": "bbb:",
#     }}
#

try:
    from {gds_import_path}generatedsnamespaces import GenerateDSNamespaceDefs \
as GenerateDSNamespaceDefs_
except ModulenotfoundExp_ :
    GenerateDSNamespaceDefs_ = {{}}
try:
    from {gds_import_path}generatedsnamespaces import GenerateDSNamespaceTypePrefixes \
as GenerateDSNamespaceTypePrefixes_
except ModulenotfoundExp_ :
    GenerateDSNamespaceTypePrefixes_ = {{}}

#
# You can replace the following class definition by defining an
# importable module named "generatedscollector" containing a class
# named "GdsCollector".  See the default class definition below for
# clues about the possible content of that class.
#
try:
    from {gds_import_path}generatedscollector import GdsCollector as GdsCollector_
except ModulenotfoundExp_ :

    class GdsCollector_(object):

        def __init__(self, messages=None):
            if messages is None:
                self.messages = []
            else:
                self.messages = messages

        def add_message(self, msg):
            self.messages.append(msg)

        def get_messages(self):
            return self.messages

        def clear_messages(self):
            self.messages = []

        def print_messages(self):
            for msg in self.messages:
                print("Warning: {{}}".format(msg))

        def write_messages(self, outstream):
            for msg in self.messages:
                outstream.write("Warning: {{}}\\n".format(msg))


#
# The super-class for enum types
#

try:
    from enum import Enum
except ModulenotfoundExp_ :
    Enum = object

#
# The root super-class for element type classes
#
# Calls to the methods in these classes are generated by generateDS.py.
# You can replace these methods by re-implementing the following class
#   in a module named generatedssuper.py.

{generatedssuper_import}

#
# If you have installed IPython you can uncomment and use the following.
# IPython is available from http://ipython.scipy.org/.
#

## from IPython.Shell import IPShellEmbed
## args = ''
## ipshell = IPShellEmbed(args,
##     banner = 'Dropping into IPython',
##     exit_msg = 'Leaving Interpreter, back to program.')

# Then use the following line where and when you want to drop into the
# IPython shell:
#    ipshell('<some message> -- Entering ipshell.\\nHit Ctrl-D to exit')

#
# Globals
#

ExternalEncoding = '{ExternalEncoding}'
# Set this to false in order to deactivate during export, the use of
# name space prefixes captured from the input document.
UseCapturedNS_ = True
CapturedNsmap_ = {{}}
Tag_pattern_ = re_.compile(r'({{.*}})?(.*)')
String_cleanup_pat_ = re_.compile(r"[\\n\\r\\s]+")
Namespace_extract_pat_ = re_.compile(r'{{(.*)}}(.*)')
CDATA_pattern_ = re_.compile(r"<!\\[CDATA\\[.*?\\]\\]>", re_.DOTALL)

# Change this to redirect the generated superclass module to use a
# specific subclass module.
CurrentSubclassModule_ = None
{preserve_cdata_tags_pat}
#
# Support/utility functions.
#


def showIndent(outfile, level, pretty_print=True):
    if pretty_print:
        for idx in range(level):
            outfile.write('    ')


def quote_xml(inStr):
    "Escape markup chars, but do not modify CDATA sections."
    if not inStr:
        return ''
    {quote_xml_text}
    s2 = ''
    pos = 0
    matchobjects = CDATA_pattern_.finditer(s1)
    for mo in matchobjects:
        s3 = s1[pos:mo.start()]
        s2 += quote_xml_aux(s3)
        s2 += s1[mo.start():mo.end()]
        pos = mo.end()
    s3 = s1[pos:]
    s2 += quote_xml_aux(s3)
    return s2


def quote_xml_aux(inStr):
    s1 = inStr.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    return s1


def quote_attrib(inStr):
    {quote_attrib_text}
    s1 = s1.replace('&', '&amp;')
    s1 = s1.replace('<', '&lt;')
    s1 = s1.replace('>', '&gt;')
    if '"' in s1:
        if "'" in s1:
            s1 = '"%s"' % s1.replace('"', "&quot;")
        else:
            s1 = "'%s'" % s1
    else:
        s1 = '"%s"' % s1
    return s1


def quote_python(inStr):
    s1 = inStr
    if s1.find("'") == -1:
        if s1.find('\\n') == -1:
            return "'%s'" % s1
        else:
            return "'''%s'''" % s1
    else:
        if s1.find('"') != -1:
            s1 = s1.replace('"', '\\\\"')
        if s1.find('\\n') == -1:
            return '"%s"' % s1
        else:
            return '\"\"\"%s\"\"\"' % s1


{preserve_cdata_get_text}

def find_attr_value_(attr_name, node):
    attrs = node.attrib
    attr_parts = attr_name.split(':')
    value = None
    if len(attr_parts) == 1:
        value = attrs.get(attr_name)
    elif len(attr_parts) == 2:
        prefix, name = attr_parts
        if prefix == 'xml':
            namespace = 'http://www.w3.org/XML/1998/namespace'
        else:
            namespace = node.nsmap.get(prefix)
        if namespace is not None:
            value = attrs.get('{{%s}}%s' % (namespace, name, ))
    return value


def encode_str_2_3(instr):
    return instr


class GDSParseError(Exception):
    pass


def raise_parse_error(node, msg):
    if node is not None:
        msg = '%s (element %s/line %d)' % (msg, node.tag, node.sourceline, )
    raise GDSParseError(msg)


class MixedContainer:
    # Constants for category:
    CategoryNone = 0
    CategoryText = 1
    CategorySimple = 2
    CategoryComplex = 3
    # Constants for content_type:
    TypeNone = 0
    TypeText = 1
    TypeString = 2
    TypeInteger = 3
    TypeFloat = 4
    TypeDecimal = 5
    TypeDouble = 6
    TypeBoolean = 7
    TypeBase64 = 8
    def __init__(self, category, content_type, name, value):
        self.category = category
        self.content_type = content_type
        self.name = name
        self.value = value
    def getCategory(self):
        return self.category
    def getContenttype(self, content_type):
        return self.content_type
    def getValue(self):
        return self.value
    def getName(self):
        return self.name
#xmldisable#    def export(self, outfile, level, name, namespace,
#xmldisable#               pretty_print=True):
#xmldisable#        if self.category == MixedContainer.CategoryText:
#xmldisable#            # Prevent exporting empty content as empty lines.
#xmldisable#            if self.value.strip():
#xmldisable#                outfile.write(self.value)
#xmldisable#        elif self.category == MixedContainer.CategorySimple:
#xmldisable#            self.exportSimple(outfile, level, name)
#xmldisable#        else:    # category == MixedContainer.CategoryComplex
#xmldisable#            self.value.export(
#xmldisable#                outfile, level, namespace, name_=name,
#xmldisable#                pretty_print=pretty_print)
#xmldisable#    def exportSimple(self, outfile, level, name):
#xmldisable#        if self.content_type == MixedContainer.TypeString:
#xmldisable#            outfile.write('<%s>%s</%s>' % (
#xmldisable#                self.name, self.value, self.name))
#xmldisable#        elif self.content_type == MixedContainer.TypeInteger or \\
#xmldisable#                self.content_type == MixedContainer.TypeBoolean:
#xmldisable#            outfile.write('<%s>%d</%s>' % (
#xmldisable#                self.name, self.value, self.name))
#xmldisable#        elif self.content_type == MixedContainer.TypeFloat or \\
#xmldisable#                self.content_type == MixedContainer.TypeDecimal:
#xmldisable#            outfile.write('<%s>%f</%s>' % (
#xmldisable#                self.name, self.value, self.name))
#xmldisable#        elif self.content_type == MixedContainer.TypeDouble:
#xmldisable#            outfile.write('<%s>%g</%s>' % (
#xmldisable#                self.name, self.value, self.name))
#xmldisable#        elif self.content_type == MixedContainer.TypeBase64:
#xmldisable#            outfile.write('<%s>%s</%s>' % (
#xmldisable#                self.name,
#xmldisable#                base64.b64encode(self.value),
#xmldisable#                self.name))
#xmldisable#    def to_etree(self, element, mapping_=None, reverse_mapping_=None, nsmap_=None):
#xmldisable#        if self.category == MixedContainer.CategoryText:
#xmldisable#            # Prevent exporting empty content as empty lines.
#xmldisable#            if self.value.strip():
#xmldisable#                if len(element) > 0:
#xmldisable#                    if element[-1].tail is None:
#xmldisable#                        element[-1].tail = self.value
#xmldisable#                    else:
#xmldisable#                        element[-1].tail += self.value
#xmldisable#                else:
#xmldisable#                    if element.text is None:
#xmldisable#                        element.text = self.value
#xmldisable#                    else:
#xmldisable#                        element.text += self.value
#xmldisable#        elif self.category == MixedContainer.CategorySimple:
#xmldisable#            subelement = etree_.SubElement(
#xmldisable#                element, '%s' % self.name)
#xmldisable#            subelement.text = self.to_etree_simple()
#xmldisable#        else:    # category == MixedContainer.CategoryComplex
#xmldisable#            self.value.to_etree(element)
#xmldisable#    def to_etree_simple(self, mapping_=None, reverse_mapping_=None, nsmap_=None):
#xmldisable#        if self.content_type == MixedContainer.TypeString:
#xmldisable#            text = self.value
#xmldisable#        elif (self.content_type == MixedContainer.TypeInteger or
#xmldisable#                self.content_type == MixedContainer.TypeBoolean):
#xmldisable#            text = '%d' % self.value
#xmldisable#        elif (self.content_type == MixedContainer.TypeFloat or
#xmldisable#                self.content_type == MixedContainer.TypeDecimal):
#xmldisable#            text = '%f' % self.value
#xmldisable#        elif self.content_type == MixedContainer.TypeDouble:
#xmldisable#            text = '%g' % self.value
#xmldisable#        elif self.content_type == MixedContainer.TypeBase64:
#xmldisable#            text = '%s' % base64.b64encode(self.value)
#xmldisable#        return text
#xmldisable#    def exportLiteral(self, outfile, level, name):
#xmldisable#        if self.category == MixedContainer.CategoryText:
#xmldisable#            showIndent(outfile, level)
#xmldisable#            outfile.write(
#xmldisable#                'model_.MixedContainer(%d, %d, "%s", "%s"),\\n' % (
#xmldisable#                    self.category, self.content_type,
#xmldisable#                    self.name, self.value))
#xmldisable#        elif self.category == MixedContainer.CategorySimple:
#xmldisable#            showIndent(outfile, level)
#xmldisable#            outfile.write(
#xmldisable#                'model_.MixedContainer(%d, %d, "%s", "%s"),\\n' % (
#xmldisable#                    self.category, self.content_type,
#xmldisable#                    self.name, self.value))
#xmldisable#        else:    # category == MixedContainer.CategoryComplex
#xmldisable#            showIndent(outfile, level)
#xmldisable#            outfile.write(
#xmldisable#                'model_.MixedContainer(%d, %d, "%s",\\n' % (
#xmldisable#                    self.category, self.content_type, self.name,))
#xmldisable#            self.value.exportLiteral(outfile, level + 1)
#xmldisable#            showIndent(outfile, level)
#xmldisable#            outfile.write(')\\n')


class MemberSpec_(object):
    def __init__(self, name='', data_type='', container=0,
            optional=0, child_attrs=None, choice=None):
        self.name = name
        self.data_type = data_type
        self.container = container
        self.child_attrs = child_attrs
        self.choice = choice
        self.optional = optional
    def set_name(self, name): self.name = name
    def get_name(self): return self.name
    def set_data_type(self, data_type): self.data_type = data_type
    def get_data_type_chain(self): return self.data_type
    def get_data_type(self):
        if isinstance(self.data_type, list):
            if len(self.data_type) > 0:
                return self.data_type[-1]
            else:
                return 'xs:string'
        else:
            return self.data_type
    def set_container(self, container): self.container = container
    def get_container(self): return self.container
    def set_child_attrs(self, child_attrs): self.child_attrs = child_attrs
    def get_child_attrs(self): return self.child_attrs
    def set_choice(self, choice): self.choice = choice
    def get_choice(self): return self.choice
    def set_optional(self, optional): self.optional = optional
    def get_optional(self): return self.optional


def _cast(typ, value):
    if typ is None or value is None:
        return value
    return typ(value)

#
# Data representation classes.
#

"""


TEMPLATE_GENERATEDS_SUPER = """\

class GeneratedsSuper({supersuper_repl}):
    {gds_slots}__hash__ = object.__hash__
    tzoff_pattern = re_.compile(r'(\+|-)((0\d|1[0-3]):[0-5]\d|14:00)$')
    class _FixedOffsetTZ(datetime_.tzinfo):
        def __init__(self, offset, name):
            self.__offset = datetime_.timedelta(minutes=offset)
            self.__name = name
        def utcoffset(self, dt):
            return self.__offset
        def tzname(self, dt):
            return self.__name
        def dst(self, dt):
            return None{gds_subclass_slots}
#xmldisable#    def __str__(self):
#xmldisable#        settings = {{
#xmldisable#            'str_pretty_print': True,
#xmldisable#            'str_indent_level': 0,
#xmldisable#            'str_namespaceprefix': '',
#xmldisable#            'str_name': self.__class__.__name__,
#xmldisable#            'str_namespacedefs': '',
#xmldisable#        }}
#xmldisable#        for n in settings:
#xmldisable#            if hasattr(self, n):
#xmldisable#                settings[n] = getattr(self, n)
#xmldisable#        if sys.version_info.major == 2:
#xmldisable#            from StringIO import StringIO
#xmldisable#        else:
#xmldisable#            from io import StringIO
#xmldisable#        output = StringIO()
#xmldisable#        self.export(
#xmldisable#            output,
#xmldisable#            settings['str_indent_level'],
#xmldisable#            pretty_print=settings['str_pretty_print'],
#xmldisable#            namespaceprefix_=settings['str_namespaceprefix'],
#xmldisable#            name_=settings['str_name'],
#xmldisable#            namespacedef_=settings['str_namespacedefs']
#xmldisable#        )
#xmldisable#        strval = output.getvalue()
#xmldisable#        output.close()
#xmldisable#        return strval
    def gds_format_string(self, input_data, input_name=''):
        return input_data
    def gds_parse_string(self, input_data, node=None, input_name=''):
        return input_data
    def gds_validate_string(self, input_data, node=None, input_name=''):
        if not input_data:
            return ''
        else:
            return input_data
    def gds_format_base64(self, input_data, input_name=''):
        return base64.b64encode(input_data).decode('ascii')
    def gds_validate_base64(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_integer(self, input_data, input_name=''):
        return '%d' % int(input_data)
    def gds_parse_integer(self, input_data, node=None, input_name=''):
        try:
            ival = int(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, 'Requires integer value: %s' % exp)
        return ival
    def gds_validate_integer(self, input_data, node=None, input_name=''):
        try:
            value = int(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires integer value')
        return value
    def gds_format_integer_list(self, input_data, input_name=''):
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
            input_data = [str(s) for s in input_data]
        return '%s' % ' '.join(input_data)
    def gds_validate_integer_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                int(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of integer values')
        return values
    def gds_format_float(self, input_data, input_name=''):
        return ('%.15f' % float(input_data)).rstrip('0')
    def gds_parse_float(self, input_data, node=None, input_name=''):
        try:
            fval_ = float(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, 'Requires float or double value: %s' % exp)
        return fval_
    def gds_validate_float(self, input_data, node=None, input_name=''):
        try:
            value = float(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires float value')
        return value
    def gds_format_float_list(self, input_data, input_name=''):
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
            input_data = [str(s) for s in input_data]
        return '%s' % ' '.join(input_data)
    def gds_validate_float_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of float values')
        return values
    def gds_format_decimal(self, input_data, input_name=''):
        return_value = '%s' % input_data
        if '.' in return_value:
            return_value = return_value.rstrip('0')
            if return_value.endswith('.'):
                return_value = return_value.rstrip('.')
        return return_value
    def gds_parse_decimal(self, input_data, node=None, input_name=''):
        try:
            decimal_value = decimal_.Decimal(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires decimal value')
        return decimal_value
    def gds_validate_decimal(self, input_data, node=None, input_name=''):
        try:
            value = decimal_.Decimal(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires decimal value')
        return value
    def gds_format_decimal_list(self, input_data, input_name=''):
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
            input_data = [str(s) for s in input_data]
        return ' '.join([self.gds_format_decimal(item) for item in input_data])
    def gds_validate_decimal_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                decimal_.Decimal(value)
            except (TypeError, ValueError):
                raise_parse_error(node, 'Requires sequence of decimal values')
        return values
    def gds_format_double(self, input_data, input_name=''):
        return '%s' % input_data
    def gds_parse_double(self, input_data, node=None, input_name=''):
        try:
            fval_ = float(input_data)
        except (TypeError, ValueError) as exp:
            raise_parse_error(node, 'Requires double or float value: %s' % exp)
        return fval_
    def gds_validate_double(self, input_data, node=None, input_name=''):
        try:
            value = float(input_data)
        except (TypeError, ValueError):
            raise_parse_error(node, 'Requires double or float value')
        return value
    def gds_format_double_list(self, input_data, input_name=''):
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
            input_data = [str(s) for s in input_data]
        return '%s' % ' '.join(input_data)
    def gds_validate_double_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            try:
                float(value)
            except (TypeError, ValueError):
                raise_parse_error(
                    node, 'Requires sequence of double or float values')
        return values
    def gds_format_boolean(self, input_data, input_name=''):
        return ('%s' % input_data).lower()
    def gds_parse_boolean(self, input_data, node=None, input_name=''):
        if input_data in ('true', '1'):
            bval = True
        elif input_data in ('false', '0'):
            bval = False
        else:
            raise_parse_error(node, 'Requires boolean value')
        return bval
    def gds_validate_boolean(self, input_data, node=None, input_name=''):
        if input_data not in (True, 1, False, 0, ):
            raise_parse_error(
                node,
                'Requires boolean value '
                '(one of True, 1, False, 0)')
        return input_data
    def gds_format_boolean_list(self, input_data, input_name=''):
        if len(input_data) > 0 and not isinstance(input_data[0], BaseStrType_):
            input_data = [str(s) for s in input_data]
        return '%s' % ' '.join(input_data)
    def gds_validate_boolean_list(
            self, input_data, node=None, input_name=''):
        values = input_data.split()
        for value in values:
            value = self.gds_parse_boolean(value, node, input_name)
            if value not in (True, 1, False, 0, ):
                raise_parse_error(
                    node,
                    'Requires sequence of boolean values '
                    '(one of True, 1, False, 0)')
        return values
    def gds_validate_datetime(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_datetime(self, input_data, input_name=''):
        if input_data.microsecond == 0:
            _svalue = '%04d-%02d-%02dT%02d:%02d:%02d' % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = '%04d-%02d-%02dT%02d:%02d:%02d.%s' % (
                input_data.year,
                input_data.month,
                input_data.day,
                input_data.hour,
                input_data.minute,
                input_data.second,
                ('%f' % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{{0:02d}}:{{1:02d}}'.format(hours, minutes)
        return _svalue
    @classmethod
    def gds_parse_datetime(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        time_parts = input_data.split('.')
        if len(time_parts) > 1:
            micro_seconds = int(float('0.' + time_parts[1]) * 1000000)
            input_data = '%s.%s' % (
                time_parts[0], "{{}}".format(micro_seconds).rjust(6, "0"), )
            dt = datetime_.datetime.strptime(
                input_data, '%Y-%m-%dT%H:%M:%S.%f')
        else:
            dt = datetime_.datetime.strptime(
                input_data, '%Y-%m-%dT%H:%M:%S')
        dt = dt.replace(tzinfo=tz)
        return dt
    def gds_validate_date(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_date(self, input_data, input_name=''):
        _svalue = '%04d-%02d-%02d' % (
            input_data.year,
            input_data.month,
            input_data.day,
        )
        try:
            if input_data.tzinfo is not None:
                tzoff = input_data.tzinfo.utcoffset(input_data)
                if tzoff is not None:
                    total_seconds = tzoff.seconds + (86400 * tzoff.days)
                    if total_seconds == 0:
                        _svalue += 'Z'
                    else:
                        if total_seconds < 0:
                            _svalue += '-'
                            total_seconds *= -1
                        else:
                            _svalue += '+'
                        hours = total_seconds // 3600
                        minutes = (total_seconds - (hours * 3600)) // 60
                        _svalue += '{{0:02d}}:{{1:02d}}'.format(
                            hours, minutes)
        except AttributeError:
            pass
        return _svalue
    @classmethod
    def gds_parse_date(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        dt = datetime_.datetime.strptime(input_data, '%Y-%m-%d')
        dt = dt.replace(tzinfo=tz)
        return dt.date()
    def gds_validate_time(self, input_data, node=None, input_name=''):
        return input_data
    def gds_format_time(self, input_data, input_name=''):
        if input_data.microsecond == 0:
            _svalue = '%02d:%02d:%02d' % (
                input_data.hour,
                input_data.minute,
                input_data.second,
            )
        else:
            _svalue = '%02d:%02d:%02d.%s' % (
                input_data.hour,
                input_data.minute,
                input_data.second,
                ('%f' % (float(input_data.microsecond) / 1000000))[2:],
            )
        if input_data.tzinfo is not None:
            tzoff = input_data.tzinfo.utcoffset(input_data)
            if tzoff is not None:
                total_seconds = tzoff.seconds + (86400 * tzoff.days)
                if total_seconds == 0:
                    _svalue += 'Z'
                else:
                    if total_seconds < 0:
                        _svalue += '-'
                        total_seconds *= -1
                    else:
                        _svalue += '+'
                    hours = total_seconds // 3600
                    minutes = (total_seconds - (hours * 3600)) // 60
                    _svalue += '{{0:02d}}:{{1:02d}}'.format(hours, minutes)
        return _svalue
    def gds_validate_simple_patterns(self, patterns, target):
        # pat is a list of lists of strings/patterns.
        # The target value must match at least one of the patterns
        # in order for the test to succeed.
        found1 = True
        for patterns1 in patterns:
            found2 = False
            for patterns2 in patterns1:
                mo = re_.search(patterns2, target)
                if mo is not None and len(mo.group(0)) == len(target):
                    found2 = True
                    break
            if not found2:
                found1 = False
                break
        return found1
    @classmethod
    def gds_parse_time(cls, input_data):
        tz = None
        if input_data[-1] == 'Z':
            tz = GeneratedsSuper._FixedOffsetTZ(0, 'UTC')
            input_data = input_data[:-1]
        else:
            results = GeneratedsSuper.tzoff_pattern.search(input_data)
            if results is not None:
                tzoff_parts = results.group(2).split(':')
                tzoff = int(tzoff_parts[0]) * 60 + int(tzoff_parts[1])
                if results.group(1) == '-':
                    tzoff *= -1
                tz = GeneratedsSuper._FixedOffsetTZ(
                    tzoff, results.group(0))
                input_data = input_data[:-6]
        if len(input_data.split('.')) > 1:
            dt = datetime_.datetime.strptime(input_data, '%H:%M:%S.%f')
        else:
            dt = datetime_.datetime.strptime(input_data, '%H:%M:%S')
        dt = dt.replace(tzinfo=tz)
        return dt.time()
    def gds_check_cardinality_(
            self, value, input_name,
            min_occurs=0, max_occurs=1, required=None):
        if value is None:
            length = 0
        elif isinstance(value, list):
            length = len(value)
        else:
            length = 1
        if required is not None :
            if required and length < 1:
                self.gds_collector_.add_message(
                    "Required value {{}}{{}} is missing".format(
                        input_name, self.gds_get_node_lineno_()))
        if length < min_occurs:
            self.gds_collector_.add_message(
                "Number of values for {{}}{{}} is below "
                "the minimum allowed, "
                "expected at least {{}}, found {{}}".format(
                    input_name, self.gds_get_node_lineno_(),
                    min_occurs, length))
        elif length > max_occurs:
            self.gds_collector_.add_message(
                "Number of values for {{}}{{}} is above "
                "the maximum allowed, "
                "expected at most {{}}, found {{}}".format(
                    input_name, self.gds_get_node_lineno_(),
                    max_occurs, length))
    def gds_validate_builtin_ST_(
            self, validator, value, input_name,
            min_occurs=None, max_occurs=None, required=None):
        if value is not None:
            try:
                validator(value, input_name=input_name)
            except GDSParseError as parse_error:
                self.gds_collector_.add_message(str(parse_error))
    def gds_validate_defined_ST_(
            self, validator, value, input_name,
            min_occurs=None, max_occurs=None, required=None):
        if value is not None:
            try:
                validator(value)
            except GDSParseError as parse_error:
                self.gds_collector_.add_message(str(parse_error))
    def gds_str_lower(self, instring):
        return instring.lower()
    def get_path_(self, node):
        path_list = []
        self.get_path_list_(node, path_list)
        path_list.reverse()
        path = '/'.join(path_list)
        return path
    Tag_strip_pattern_ = re_.compile(r'\{{.*\}}')
    def get_path_list_(self, node, path_list):
        if node is None:
            return
        tag = GeneratedsSuper.Tag_strip_pattern_.sub('', node.tag)
        if tag:
            path_list.append(tag)
        self.get_path_list_(node.getparent(), path_list)
    def get_class_obj_(self, node, default_class=None):
        class_obj1 = default_class
        if 'xsi' in node.nsmap:
            classname = node.get('{{%s}}type' % node.nsmap['xsi'])
            if classname is not None:
                names = classname.split(':')
                if len(names) == 2:
                    classname = names[1]
                class_obj2 = globals().get(classname)
                if class_obj2 is not None:
                    class_obj1 = class_obj2
        return class_obj1
    def gds_build_any(self, node, type_name=None):
        # provide default value in case option --disable-xml is used.
        content = ""
#xmldisable#        content = etree_.tostring(node, encoding="unicode")
        return content
    @classmethod
    def gds_reverse_node_mapping(cls, mapping):
        {gds_reverse_node_mapping_text}
    @staticmethod
    def gds_encode(instring):
        if sys.version_info.major == 2:
            if ExternalEncoding:
                encoding = ExternalEncoding
            else:
                encoding = 'utf-8'
            return instring.encode(encoding)
        else:
            return instring
    @staticmethod
    def convert_unicode(instring):
        if isinstance(instring, str):
            result = quote_xml(instring)
        elif sys.version_info.major == 2 and isinstance(instring, unicode):
            result = quote_xml(instring).encode('utf8')
        else:
            result = GeneratedsSuper.gds_encode(str(instring))
        return result{gds_equals}
    def __ne__(self, other):
        return not self.__eq__(other)
    # Django ETL transform hooks.
    def gds_djo_etl_transform(self):
        pass
    def gds_djo_etl_transform_db_obj(self, dbobj):
        pass
    # SQLAlchemy ETL transform hooks.
    def gds_sqa_etl_transform(self):
        return 0, None
    def gds_sqa_etl_transform_db_obj(self, dbobj):
        pass
    def gds_get_node_lineno_(self):
        if (hasattr(self, "gds_elementtree_node_") and
                self.gds_elementtree_node_ is not None):
            return ' near line {{}}'.format(
                self.gds_elementtree_node_.sourceline)
        else:
            return ""


def getSubclassFromModule_(module, class_):
    '''Get the subclass of a class from a specific module.'''
    name = class_.__name__ + '{SubclassSuffix}'
    if hasattr(module, name):
        return getattr(module, name)
    else:
        return None
"""

TEMPLATE_GENERATEDS_SUPER_EQUALS_WITH_SLOTS = """
    def __eq__(self, other):
        if type(self) != type(other):
            return False
        mro = self.__class__.__mro__
        return all(
            getattr(self, attribute) == getattr(other, attribute)
            for cls in islice(mro, 0, len(mro) - 2)
            for attribute in cls.member_data_items_)"""

TEMPLATE_GENERATEDS_SUPER_EQUALS_WITHOUT_SLOTS = """
    def __eq__(self, other):
        def excl_select_objs_(obj):
            return (obj[0] != 'parent_object_' and
                    obj[0] != 'gds_collector_')
        if type(self) != type(other):
            return False
        return all(x == y for x, y in zip_longest(
            filter(excl_select_objs_, self.__dict__.items()),
            filter(excl_select_objs_, other.__dict__.items())))"""

TEMPLATE_GENERATEDS_SUPER_SUBCLASS_SLOTS_WITH_XML = """
    @staticmethod
    def gds_subclass_slots(member_data_items):
        slots = []
        for member in member_data_items:
            slots.append(member)
            slots.append("%s_nsprefix_" % member)
        return slots"""

TEMPLATE_GENERATEDS_SUPER_SUBCLASS_SLOTS_WITHOUT_XML = """
    @staticmethod
    def gds_subclass_slots(member_data_items):
        return list(member_data_items.keys())"""

# Fool (and straighten out) the syntax highlighting.
# DUMMY = """


def format_options_args(options, args):
    options1 = '\n'.join(['#   %s' % (item, ) for item in options])
    args1 = '\n'.join(['#   %s' % (item, ) for item in args])
    program = sys.argv[0]
    options2 = ''
    for name, value in options:
        if value:
            if name.startswith('--'):
                options2 += ' %s="%s"' % (name, value, )
            else:
                options2 += ' %s "%s"' % (name, value, )
        else:
            options2 += ' %s' % name
    args1 = ' '.join(args)
    command_line = '%s%s %s' % (program, options2, args1, )
    return options1, args1, command_line


Preserve_cdata_get_all_text1 = """\
PRESERVE_CDATA_TAGS_PAT1 = re_.compile(
    r'^<.+?>(.*?)</?[a-zA-Z0-9\-]+>(?!.*</?[a-zA-Z0-9\-]+>)')
PRESERVE_CDATA_TAGS_PAT2 = re_.compile(r'^<.+?>.*?</.+?>(.*)$')


def get_all_text_(node):
    if node.text is not None:
        mo_ = PRESERVE_CDATA_TAGS_PAT1.search(etree_.tostring(node).strip())
        if mo_ is not None:
            text = mo_.group(1)
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            mo_ = PRESERVE_CDATA_TAGS_PAT2.search(
                etree_.tostring(child).strip())
            if mo_ is not None:
                text += mo_.group(1)
    return text
"""

Preserve_cdata_get_all_text2 = """\
def get_all_text_(node):
    if node.text is not None:
        text = node.text
    else:
        text = ''
    for child in node:
        if child.tail is not None:
            text += child.tail
    return text
"""


def generateHeader(wrt, prefix, options, args, externalImports, customImports):
    global TEMPLATE_HEADER
    tstamp = (not NoDates and time.ctime()) or ''
    if NoVersion:
        version = ''
    else:
        version = ' version %s' % VERSION
    options1, args1, command_line = format_options_args(options, args)
    current_working_directory = os.path.split(os.getcwd())[1]
    if PreserveCdataTags and not XmlDisabled:
        preserve_cdata_tags_pat = (
            "PRESERVE_CDATA_TAGS_PAT = "
            "re_.compile(r'^<.+?>(.*)<.+>$', re_.DOTALL)\n\n")
        preserve_cdata_get_text = Preserve_cdata_get_all_text1
    else:
        preserve_cdata_tags_pat = ""
        preserve_cdata_get_text = Preserve_cdata_get_all_text2
    gds_reverse_node_mapping_text = \
        "return dict(((v, k) for k, v in mapping.items()))"
    quote_xml_text = \
        "s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)"
    quote_attrib_text = \
        "s1 = (isinstance(inStr, BaseStrType_) and inStr or '%s' % inStr)"

    gds_slots = ""
    if UseSlots:
        slots = ["gds_collector_"]
        if not XmlDisabled:
            slots.extend([
                "gds_elementtree_node_", "original_tagname_", "parent_object_",
                "ns_prefix_"])
        gds_slots = "__slots__ = ['%s']\n    " % "', '".join(slots)
    gds_equals = TEMPLATE_GENERATEDS_SUPER_EQUALS_WITH_SLOTS if UseSlots \
        else TEMPLATE_GENERATEDS_SUPER_EQUALS_WITHOUT_SLOTS
    gds_subclass_slots = ((
        TEMPLATE_GENERATEDS_SUPER_SUBCLASS_SLOTS_WITHOUT_XML if XmlDisabled
        else TEMPLATE_GENERATEDS_SUPER_SUBCLASS_SLOTS_WITH_XML) if UseSlots
        else "")
    if UseGeneratedssuperLookup:
        supersuper_repl = 'GeneratedsSuperSuper'
    else:
        supersuper_repl = 'object'
    import_string = TEMPLATE_GENERATEDS_SUPER.format(
        gds_equals=gds_equals,
        gds_reverse_node_mapping_text=gds_reverse_node_mapping_text,
        gds_slots=gds_slots,
        gds_subclass_slots=gds_subclass_slots,
        SubclassSuffix=SubclassSuffix,
        gds_import_path=GDSImportPath,
        supersuper_repl=supersuper_repl,
    )
    if UseGeneratedssuperLookup:
        s0 = """try:
    from {gds_import_path}generatedssuper import GeneratedsSuper
except ModulenotfoundExp_ as exp:
    try:
        from {gds_import_path}generatedssupersuper import GeneratedsSuperSuper
    except ModulenotfoundExp_ as exp:
        class GeneratedsSuperSuper(object):
            pass
""".format(gds_import_path=GDSImportPath)
        if sys.version_info.major == 2:
            outfile = StringIO.StringIO
        else:
            outfile = io.StringIO
        for line in outfile(import_string).readlines():
            s0 += "    " + line
        import_string = s0
    db_orm_import = ''
    if ExportDjango or ExportSQLAlchemy:
        db_orm_import = '# imports for django and/or sqlalchemy\n'
        db_orm_import += 'import json as json_\n'
    if ExportDjango:
        db_orm_import += """try:
    import models as models_
except ModulenotfoundExp_ :
    models_ = None
"""
    if ExportSQLAlchemy:
        db_orm_import += """try:
    import models_sqa as models_sqa_
except ModulenotfoundExp_ :
    models_sqa_ = None
"""

    itertools_import = "from itertools import islice" if UseSlots \
        else "from six.moves import zip_longest"
    custom_imports = ''
    if customImports:
        custom_imports = '\n'.join(
            customImports if isinstance(
                customImports, list) else [customImports])
    s1 = TEMPLATE_HEADER.format(
        tstamp=tstamp,
        version=version,
        pyversion=sys.version.replace('\n', ' '),
        options1=options1,
        args1=args1,
        command_line=command_line,
        current_working_directory=current_working_directory,
        ExternalEncoding=ExternalEncoding,
        preserve_cdata_tags_pat=preserve_cdata_tags_pat,
        preserve_cdata_get_text=preserve_cdata_get_text,
        generatedssuper_import=import_string,
        quote_xml_text=quote_xml_text,
        quote_attrib_text=quote_attrib_text,
        db_orm_import=db_orm_import,
        itertools_import=itertools_import,
        gds_import_path=GDSImportPath,
        custom_imports=custom_imports,
        prefix=prefix,
    )
    wrt(s1)
    # Ensure that imports are generated in the same, predictable order.
    externalImports = sorted(externalImports)
    for externalImport in externalImports:
        wrt(externalImport + "\n")
    wrt("\n")


TEMPLATE_MAIN = """\
USAGE_TEXT = \"\"\"
Usage: python <%(prefix)sParser>.py [ -s ] <in_xml_file>
\"\"\"


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def get_root_tag(node):
    tag = Tag_pattern_.match(node.tag).groups()[-1]
    prefix_tag = TagNamePrefix + tag
    rootClass = GDSClassesMapping.get(prefix_tag)
    if rootClass is None:
        rootClass = globals().get(prefix_tag)
    return tag, rootClass


def get_required_ns_prefix_defs(rootNode):
    '''Get all name space prefix definitions required in this XML doc.
    Return a dictionary of definitions and a char string of definitions.
    '''
    nsmap = {
        prefix: uri
        for node in rootNode.iter()
        for (prefix, uri) in node.nsmap.items()
        if prefix is not None
    }
    namespacedefs = ' '.join([
        'xmlns:{}="{}"'.format(prefix, uri)
        for prefix, uri in nsmap.items()
    ])
    return nsmap, namespacedefs


def parse(inFileName, silence=False, print_warnings=True):
    global CapturedNsmap_
    gds_collector = GdsCollector_()
%(preserve_cdata_tags)s    doc = parsexml_(inFileName, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = '%(rootElement)s'
        rootClass = %(prefix)s%(rootClass)s
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    CapturedNsmap_, namespacedefs = get_required_ns_prefix_defs(rootNode)
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
#silence#    if not silence:
#silence#        sys.stdout.write('<?xml version="1.0" ?>\\n')
#silence#        rootObj.export(
#silence#            sys.stdout, 0, name_=rootTag,
#silence#            namespacedef_=namespacedefs,
#silence#            pretty_print=True)
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseEtree(inFileName, silence=False, print_warnings=True,
               mapping=None, reverse_mapping=None, nsmap=None):
%(preserve_cdata_tags)s    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = '%(rootElement)s'
        rootClass = %(prefix)s%(rootClass)s
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if mapping is None:
        mapping = {}
    if reverse_mapping is None:
        reverse_mapping = {}
    rootElement = rootObj.to_etree(
        None, name_=rootTag, mapping_=mapping,
        reverse_mapping_=reverse_mapping, nsmap_=nsmap)
    reverse_node_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
#silence#    if not silence:
#silence#        content = etree_.tostring(
#silence#            rootElement, pretty_print=True,
#silence#            xml_declaration=True, encoding="utf-8")
#silence#        sys.stdout.write(str(content))
#silence#        sys.stdout.write('\\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj, rootElement, mapping, reverse_node_mapping


def parseString(inString, silence=False, print_warnings=True):
    '''Parse a string, create the object tree, and export it.

    Arguments:
    - inString -- A string.  This XML fragment should not start
      with an XML declaration containing an encoding.
    - silence -- A boolean.  If False, export the object.
    Returns -- The root object in the tree.
    '''
%(preserve_cdata_tags)s    rootNode= parsexmlstring_(inString, parser)
    gds_collector = GdsCollector_()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = '%(rootElement)s'
        rootClass = %(prefix)s%(rootClass)s
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    if not SaveElementTreeNode:
        rootNode = None
#silence#    if not silence:
#silence#        sys.stdout.write('<?xml version="1.0" ?>\\n')
#silence#        rootObj.export(
#silence#            sys.stdout, 0, name_=rootTag,
#silence#            namespacedef_='%(namespacedef)s')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def parseLiteral(inFileName, silence=False, print_warnings=True):
%(preserve_cdata_tags)s    doc = parsexml_(inFileName, parser)
    gds_collector = GdsCollector_()
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = '%(rootElement)s'
        rootClass = %(prefix)s%(rootClass)s
    rootObj = rootClass.factory()
    rootObj.build(rootNode, gds_collector_=gds_collector)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
#silence#    if not silence:
#silence#        sys.stdout.write('#from %(module_name)s import *\\n\\n')
#silence#        sys.stdout.write('import %(module_name)s as model_\\n\\n')
#silence#        sys.stdout.write('rootObj = model_.rootClass(\\n')
#silence#        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
#silence#        sys.stdout.write(')\\n')
    if print_warnings and len(gds_collector.get_messages()) > 0:
        separator = ('-' * 50) + '\\n'
        sys.stderr.write(separator)
        sys.stderr.write('----- Warnings -- count: {} -----\\n'.format(
            len(gds_collector.get_messages()), ))
        gds_collector.write_messages(sys.stderr)
        sys.stderr.write(separator)
    return rootObj


def main():
    args = sys.argv[1:]
    if len(args) == 1:
        parse(args[0])
    else:
        usage()


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()

"""


# Fool (and straighten out) the syntax highlighting.
# DUMMY = '''


def generateMain(outfile, prefix, root, generatedClasses):
    lines = []
    nsmap = SchemaLxmlTree.nsmap.copy()
    if None in nsmap:
        ns_prefix = nsmap.get(None)
        del nsmap[None]
        if 'xs' not in nsmap:
            nsmap['xs'] = ns_prefix
    if 'xs' not in nsmap and 'xsd' in nsmap:
        nsmap['xs'] = nsmap['xsd']
    top_lvl_elements = SchemaLxmlTree.xpath(
        './xs:element', namespaces=nsmap)
    for element in top_lvl_elements:
        if 'ref' in element.attrib:
            classType = element.attrib.get('ref')
            name = classType
        else:
            classType = element.attrib.get('type')
            name = element.attrib.get('name')
        if classType is not None and name is not None:
            _, classType = get_prefix_and_value(classType)
            _, name = get_prefix_and_value(name)
            mappedClassType = mapName(cleanupName(classType))
            mappedName = mapName(name)
            if (mappedClassType and mappedName and
                    mappedClassType in generatedClasses):
                lines.append("    '%s': %s%s,\n" % (
                    mappedName, prefix, mappedClassType, ))
    lines.sort()
    exportDictLine = "GDSClassesMapping = {{\n{}}}\n\n\n".format(
        ''.join(lines))
    outfile.write(exportDictLine)
    if XmlDisabled:
        return
    children = root.getChildren()
    rootClass = None
    if children:
        name = RootElement or children[0].getName()
        elType = cleanupName(children[0].getType())
        if RootElement:
            roots = RootElement.split('|')
            if len(roots) > 1:
                rootElement = roots[0]
                rootClass = roots[1]
            else:
                rootElement = roots[0]
        else:
            rootElement = elType
    else:
        name = ''
        if RootElement:
            roots = RootElement.split('|')
            if len(roots) > 1:
                rootElement = roots[0]
                rootClass = roots[1]
            else:
                rootElement = roots[0]
        else:
            rootElement = ''
    if rootClass is None:
        rootClass = rootElement
    if not rootClass:
        rootClass = 'None'
    if Namespacedef:
        namespace = Namespacedef
    elif Targetnamespace:
        if Targetnamespace in NamespacesDict:
            namespace = 'xmlns:%s="%s"' % (
                NamespacesDict[Targetnamespace].rstrip(':'), Targetnamespace, )
        else:
            namespace = ''
    else:
        namespace = ''
    params = {
        'prefix': prefix,
        'cap_name': cleanupName(make_gs_name(name)),
        'name': name,
        'cleanname': cleanupName(name),
        'module_name': os.path.splitext(os.path.basename(outfile.name))[0],
        'rootElement': rootElement,
        'rootClass': rootClass,
        'namespacedef': namespace,
    }
    if PreserveCdataTags:
        params['preserve_cdata_tags'] = \
            "    parser = etree_.ETCompatXMLParser(strip_cdata=False)\n"
    else:
        params['preserve_cdata_tags'] = "    parser = None\n"
        params['preserve_cdata_tags_pat'] = ""
    s1 = TEMPLATE_MAIN % params
    outfile.write(s1)


def buildCtorParams(element, parent, childCount):
    content = []
    addedArgs = {}
    add = content.append
    buildCtorParams_aux(addedArgs, add, parent)
    if element.getSimpleContent() or element.isMixed():
        add("valueOf_, ")
    if element.isMixed():
        add('mixedclass_, ')
        add('content_, ')
    if element.getExtended():
        add('extensiontype_, ')
    return content


def buildCtorParams_aux(addedArgs, add, element):
    parentName, parentObj = getParentName(element)
    if parentName:
        buildCtorParams_aux(addedArgs, add, parentObj)
    attrDefs = element.getAttributeDefs()
    for key in element.getAttributeDefsList():
        attrDef = attrDefs[key]
        name = attrDef.getName()
        name = cleanupName(mapName(name))
        if name == element.getCleanName():
            name += '_member'
        if name not in addedArgs:
            addedArgs[name] = 1
            add('%s, ' % name)
    for child in element.getChildren():
        if child.getType() == AnyTypeIdentifier:
            add('anytypeobjs_, ')
        else:
            name = child.getCleanName()
            if name == element.getCleanName():
                name += '_member'
            if name not in addedArgs:
                addedArgs[name] = 1
                add('%s, ' % name)


def get_class_behavior_args(classBehavior):
    argList = []
    args = classBehavior.getArgs()
    args = args.getArg()
    for arg in args:
        argList.append(arg.getName())
    argString = ', '.join(argList)
    return argString


#
# Retrieve the implementation body via an HTTP request to a
#   URL formed from the concatenation of the baseImplUrl and the
#   implUrl.
# An alternative implementation of get_impl_body() that also
#   looks in the local file system is commented out below.
#
def get_impl_body(classBehavior, baseImplUrl, implUrl):
    impl = '        pass\n'
    if implUrl:
        if baseImplUrl:
            implUrl = '%s%s' % (baseImplUrl, implUrl)
        try:
            impl = requests.get(implUrl).content
        except requests.exceptions.HTTPError:
            err_msg('*** Implementation at %s not found.\n' % implUrl)
        except requests.exceptions.RequestException:
            err_msg('*** Connection refused for URL: %s\n' % implUrl)
    return impl

###
### This alternative implementation of get_impl_body() tries the URL
###   via http first, then, if that fails, looks in a directory on
###   the local file system (baseImplUrl) for a file (implUrl)
###   containing the implementation body.
###
##import requests
##
##def get_impl_body(classBehavior, baseImplUrl, implUrl):
##    impl = '        pass\n'
##    if implUrl:
##        trylocal = 0
##        if baseImplUrl:
##            implUrl = '%s%s' % (baseImplUrl, implUrl)
##        try:
##            impl = requests.get(implUrl).content
##        except:
##            trylocal = 1
##        if trylocal:
##            try:
##                implFile = file(implUrl)
##                impl = implFile.read()
##                implFile.close()
##            except:
##                print '*** Implementation at %s not found.' % implUrl
##    return impl


def generateClassBehaviors(wrt, classBehaviors, baseImplUrl):
    for classBehavior in classBehaviors:
        behaviorName = classBehavior.getName()
        #
        # Generate the core behavior.
        argString = get_class_behavior_args(classBehavior)
        if argString:
            wrt('    def %s(self, %s, *args):\n' % (behaviorName, argString))
        else:
            wrt('    def %s(self, *args):\n' % (behaviorName, ))
        implUrl = classBehavior.getImpl_url()
        impl = get_impl_body(classBehavior, baseImplUrl, implUrl)
        wrt(impl)
        wrt('\n')
        #
        # Generate the ancillaries for this behavior.
        ancillaries = classBehavior.getAncillaries()
        if ancillaries:
            ancillaries = ancillaries.getAncillary()
        if ancillaries:
            for ancillary in ancillaries:
                argString = get_class_behavior_args(ancillary)
                if argString:
                    wrt('    def %s(self, %s, *args):\n' %
                        (ancillary.getName(), argString))
                else:
                    wrt('    def %s(self, *args):\n' % (ancillary.getName(), ))
                implUrl = ancillary.getImpl_url()
                impl = get_impl_body(classBehavior, baseImplUrl, implUrl)
                wrt(impl)
                wrt('\n')
        #
        # Generate the wrapper method that calls the ancillaries and
        #   the core behavior.
        argString = get_class_behavior_args(classBehavior)
        if argString:
            wrt('    def %s_wrapper(self, %s, *args):\n' %
                (behaviorName, argString))
        else:
            wrt('    def %s_wrapper(self, *args):\n' % (behaviorName, ))
        if ancillaries:
            for ancillary in ancillaries:
                role = ancillary.getRole()
                if role == 'DBC-precondition':
                    wrt('        if not self.%s(*args)\n' %
                        (ancillary.getName(), ))
                    wrt('            return False\n')
        if argString:
            wrt('        result = self.%s(%s, *args)\n' %
                (behaviorName, argString))
        else:
            wrt('        result = self.%s(*args)\n' % (behaviorName, ))
        if ancillaries:
            for ancillary in ancillaries:
                role = ancillary.getRole()
                if role == 'DBC-postcondition':
                    wrt('        if not self.%s(*args)\n' %
                        (ancillary.getName(), ))
                    wrt('            return False\n')
        wrt('        return result\n')
        wrt('\n')


def generateSubclass(wrt, element, prefix, xmlbehavior, behaviors, baseUrl):
    if not element.isComplex():
        return
    mappedName = element.getCleanName()
    if mappedName in AlreadyGenerated_subclass:
        return
    AlreadyGenerated_subclass.add(mappedName)
    name = element.getCleanName()
    wrt('class %s%s%s(supermod.%s%s):\n' % (
        prefix, name, SubclassSuffix, prefix, name))
    childCount = countChildren(element, 0)
    s1 = buildCtorArgs_multilevel(element, childCount)
    wrt('    def __init__(self%s, **kwargs_):\n' % s1)
    args = buildCtorParams(element, element, childCount)
    s1 = ''.join(args)
    if len(args) > 254:
        wrt('        arglist_ = (%s)\n' % (s1, ))
        wrt('        super(%s%s%s, self).__init__(*arglist_, **kwargs_)\n' %
            (prefix, name, SubclassSuffix, ))
    else:
        #wrt('        supermod.%s%s.__init__(%s)\n' % (prefix, name, s1))
        wrt('        super(%s%s%s, self).__init__(%s **kwargs_)\n' % (
            prefix, name, SubclassSuffix, s1, ))
    if xmlbehavior and behaviors:
        wrt('\n')
        wrt('    #\n')
        wrt('    # XMLBehaviors\n')
        wrt('    #\n')
        # Get a list of behaviors for this class/subclass.
        classDictionary = behaviors.get_class_dictionary()
        if name in classDictionary:
            classBehaviors = classDictionary[name]
        else:
            classBehaviors = None
        if classBehaviors:
            generateClassBehaviors(wrt, classBehaviors, baseUrl)
    wrt('supermod.%s%s.subclass = %s%s%s\n' % (
        prefix, name, prefix, name, SubclassSuffix))
    wrt('# end class %s%s%s\n' % (prefix, name, SubclassSuffix))
    wrt('\n\n')


TEMPLATE_SUBCLASS_HEADER = """\
#!/usr/bin/env python

#
# Generated %s by generateDS.py%s.
# Python %s
#
# Command line options:
%s
#
# Command line arguments:
#   %s
#
# Command line:
#   %s
#
# Current working directory (os.getcwd()):
#   %s
#

import os
import sys
#xmldisable#from lxml import etree as etree_

%s

#xmldisable#def parsexml_(infile, parser=None, **kwargs):
#xmldisable#    if parser is None:
#xmldisable#        # Use the lxml ElementTree compatible parser so that, e.g.,
#xmldisable#        #   we ignore comments.
#xmldisable#        parser = etree_.ETCompatXMLParser()
#xmldisable#    try:
#xmldisable#        if isinstance(infile, os.PathLike):
#xmldisable#            infile = os.path.join(infile)
#xmldisable#    except AttributeError:
#xmldisable#        pass
#xmldisable#    doc = etree_.parse(infile, parser=parser, **kwargs)
#xmldisable#    return doc

#xmldisable#def parsexmlstring_(instring, parser=None, **kwargs):
#xmldisable#    if parser is None:
#xmldisable#        # Use the lxml ElementTree compatible parser so that, e.g.,
#xmldisable#        #   we ignore comments.
#xmldisable#        try:
#xmldisable#            parser = etree_.ETCompatXMLParser()
#xmldisable#        except AttributeError:
#xmldisable#            # fallback to xml.etree
#xmldisable#            parser = etree_.XMLParser()
#xmldisable#    element = etree_.fromstring(instring, parser=parser, **kwargs)
#xmldisable#    return element

#
# Globals
#

ExternalEncoding = '%s'
SaveElementTreeNode = True

#
# Data representation classes
#


"""

TEMPLATE_SUBCLASS_FOOTER = """\
def get_root_tag(node):
    tag = supermod.Tag_pattern_.match(node.tag).groups()[-1]
    rootClass = None
    rootClass = supermod.GDSClassesMapping.get(tag)
    if rootClass is None and hasattr(supermod, tag):
        rootClass = getattr(supermod, tag)
    return tag, rootClass


def parse(inFilename, silence=False):
%(preserve_cdata_tags)s    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = '%(rootElement)s'
        rootClass = supermod.%(prefix)s%(rootClass)s
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
#silence#    if not silence:
#silence#        sys.stdout.write('<?xml version="1.0" ?>\\n')
#silence#        rootObj.export(
#silence#            sys.stdout, 0, name_=rootTag,
#silence#            namespacedef_='%(namespacedef)s',
#silence#            pretty_print=True)
    return rootObj


def parseEtree(inFilename, silence=False):
%(preserve_cdata_tags)s    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = '%(rootElement)s'
        rootClass = supermod.%(prefix)s%(rootClass)s
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    mapping = {}
    rootElement = rootObj.to_etree(None, name_=rootTag, mapping_=mapping)
    reverse_mapping = rootObj.gds_reverse_node_mapping(mapping)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
#silence#    if not silence:
#silence#        content = etree_.tostring(
#silence#            rootElement, pretty_print=True,
#silence#            xml_declaration=True, encoding="utf-8")
#silence#        sys.stdout.write(content)
#silence#        sys.stdout.write('\\n')
    return rootObj, rootElement, mapping, reverse_mapping


def parseString(inString, silence=False):
    if sys.version_info.major == 2:
        from StringIO import StringIO
    else:
        from io import BytesIO as StringIO
%(preserve_cdata_tags)s    rootNode= parsexmlstring_(inString, parser)
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = '%(rootElement)s'
        rootClass = supermod.%(prefix)s%(rootClass)s
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        rootNode = None
#silence#    if not silence:
#silence#        sys.stdout.write('<?xml version="1.0" ?>\\n')
#silence#        rootObj.export(
#silence#            sys.stdout, 0, name_=rootTag,
#silence#            namespacedef_='%(namespacedef)s')
    return rootObj


def parseLiteral(inFilename, silence=False):
%(preserve_cdata_tags)s    doc = parsexml_(inFilename, parser)
    rootNode = doc.getroot()
    rootTag, rootClass = get_root_tag(rootNode)
    if rootClass is None:
        rootTag = '%(rootElement)s'
        rootClass = supermod.%(prefix)s%(rootClass)s
    rootObj = rootClass.factory()
    rootObj.build(rootNode)
    # Enable Python to collect the space used by the DOM.
    if not SaveElementTreeNode:
        doc = None
        rootNode = None
#silence#    if not silence:
#silence#        sys.stdout.write('#from %(super)s import *\\n\\n')
#silence#        sys.stdout.write('import %(super)s as model_\\n\\n')
#silence#        sys.stdout.write('rootObj = model_.rootClass(\\n')
#silence#        rootObj.exportLiteral(sys.stdout, 0, name_=rootTag)
#silence#        sys.stdout.write(')\\n')
    return rootObj


USAGE_TEXT = \"\"\"
Usage: python ???.py <infilename>
\"\"\"


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    args = sys.argv[1:]
    if len(args) != 1:
        usage()
    infilename = args[0]
    parse(infilename)


if __name__ == '__main__':
    #import pdb; pdb.set_trace()
    main()
"""

TEMPLATE_ABSTRACT_CLASS = """\
class %(clsname)s(object):
    subclass = None
    superclass = None
# fix valueof
    def __init__(self, valueOf_=''):
        raise NotImplementedError(
            'Cannot instantiate abstract class %(clsname)s (__init__)')
    def factory(*args_, **kwargs_):
        raise NotImplementedError(
            'Cannot instantiate abstract class %(clsname)s (factory)')
    factory = staticmethod(factory)
    def build(self, node_):
        raise NotImplementedError(
            'Cannot build abstract class %(clsname)s')
        attrs = node_.attributes
        # fix_abstract
        type_name = attrs.getNamedItemNS(
            'http://www.w3.org/2001/XMLSchema-instance', 'type')
        if type_name is not None:
            self.type_ = globals()[type_name.value]()
            self.type_.build(node_)
        else:
            raise NotImplementedError(
                'Class %%s not implemented (build)' %% type_name.value)
# end class %(clsname)s


"""

TEMPLATE_ABSTRACT_CHILD = """\
            type_name_ = child_.attrib.get(
                '{http://www.w3.org/2001/XMLSchema-instance}type')
            if type_name_ is None:
                type_name_ = child_.attrib.get('type')
            if type_name_ is not None:
                type_names_ = type_name_.split(':')
                if len(type_names_) == 1:
                    type_name_ = type_names_[0]
                else:
                    type_name_ = type_names_[1]
                class_ = globals()["%s" + type_name_]
                obj_ = class_.factory()
                obj_.build(child_, gds_collector_=gds_collector_)
            else:
                raise NotImplementedError(
                    'Class not implemented for <%s> element')
"""


def getNamespace(element):
    namespace = ''
    if element.targetNamespace in NamespacesDict:
        namespace = 'xmlns:%s="%s"' % (
            NamespacesDict[element.targetNamespace].rstrip(':'),
            element.targetNamespace, )
    elif Namespacedef:
        namespace = Namespacedef
    elif Targetnamespace in NamespacesDict:
        namespace = 'xmlns:%s="%s"' % (
            NamespacesDict[Targetnamespace].rstrip(':'),
            Targetnamespace, )
    return namespace


def generateSubclasses(root, subclassFilename, behaviorFilename,
                       prefix, options, args, superModule='xxx'):
    subclassFile = makeFile(subclassFilename)
    wrt = subclassFile.write
    if subclassFile:
        # Read in the XMLBehavior file.
        xmlbehavior = None
        behaviors = None
        baseUrl = None
        if behaviorFilename:
            try:
                # Add the currect working directory to the path so that
                #   we use the user/developers local copy.
                sys.path.insert(0, '.')
                import xmlbehavior_sub as xmlbehavior
            except ModulenotfoundExp_:
                err_msg('*** You have requested generation of '
                        'extended methods.\n')
                err_msg('*** But, no xmlbehavior module is available.\n')
                err_msg('*** Generation of extended behavior '
                        'methods is omitted.\n')
            if xmlbehavior:
                behaviors = xmlbehavior.parse(behaviorFilename)
                behaviors.make_class_dictionary(cleanupName)
                baseUrl = behaviors.getBase_impl_url()
        wrt = subclassFile.write
        tstamp = (not NoDates and time.ctime()) or ''
        if NoVersion:
            version = ''
        else:
            version = ' version %s' % VERSION
        options1, args1, command_line = format_options_args(options, args)
        current_working_directory = os.path.split(os.getcwd())[1]
        super_import_statement = 'import {} as supermod'.format(
            superModule)
        wrt(TEMPLATE_SUBCLASS_HEADER % (tstamp, version,
            sys.version.replace('\n', ' '),
            options1, args1,
            command_line, current_working_directory,
            super_import_statement, ExternalEncoding, ))
        for element in ElementsForSubclasses:
            generateSubclass(
                wrt, element, prefix, xmlbehavior, behaviors, baseUrl)
        if XmlDisabled:
            return
        children = root.getChildren()
        rootClass = None
        if children:
            name = children[0].getName()
            elType = cleanupName(children[0].getType())
            if RootElement:
                roots = RootElement.split('|')
                if len(roots) > 1:
                    rootElement = roots[0]
                    rootClass = roots[1]
                else:
                    rootElement = roots[0]
            else:
                rootElement = elType
        else:
            name = ''
            if RootElement:
                roots = RootElement.split('|')
                if len(roots) > 1:
                    rootElement = roots[0]
                    rootClass = roots[1]
                else:
                    rootElement = roots[0]
            else:
                rootElement = ''
        if rootClass is None:
            rootClass = rootElement
        if Namespacedef:
            namespace = Namespacedef
        elif Targetnamespace:
            if Targetnamespace in NamespacesDict:
                namespace = 'xmlns:%s="%s"' % (
                    NamespacesDict[Targetnamespace].rstrip(':'),
                    Targetnamespace, )
            else:
                namespace = ''
        else:
            namespace = ''
        params = {
            'cap_name': make_gs_name(cleanupName(name)),
            'name': name,
            'prefix': prefix,
            'cleanname': cleanupName(name),
            'module_name': os.path.splitext(
                os.path.basename(subclassFilename))[0],
            'root': root,
            'rootElement': rootElement,
            'rootClass': rootClass,
            'namespacedef': namespace,
            'super': superModule,
        }
        if PreserveCdataTags:
            params['preserve_cdata_tags'] = \
                "    parser = etree_.ETCompatXMLParser(strip_cdata=False)\n"
        else:
            params['preserve_cdata_tags'] = \
                "    parser = None\n"
        wrt(TEMPLATE_SUBCLASS_FOOTER % params)
        subclassFile.close()


def getUsedNamespacesDefs(element):
    processedPrefixes = []
    nameSpacesDef = getNamespace(element)
    for child in element.getChildren():
        if child.prefix not in processedPrefixes and \
           child.prefix in prefixToNamespaceMap:
            spaceDef = 'xmlns:%s="%s" ' % (
                child.prefix, prefixToNamespaceMap[child.prefix])
            if spaceDef.strip() not in nameSpacesDef:
                nameSpacesDef += ' ' + spaceDef
            processedPrefixes.append(child.prefix)
    return nameSpacesDef


def generateFromTree(wrt, prefix, elements, processed, already_seen):
    for element in elements:
        if NoNameSpaceDefs:
            nameSpacesDef = ""
        else:
            nameSpacesDef = getUsedNamespacesDefs(element)
        name = element.getCleanName()
        if element not in already_seen:
            already_seen.add(element)
            processed.append(name)
            generateClasses(wrt, prefix, element, 0, nameSpacesDef)
            children = element.getChildren()
            if children:
                generateFromTree(
                    wrt, prefix, children, processed, already_seen)


def generateSimpleTypes(wrt, prefix, simpleTypeDict, root):
    global SingleFileOutput, UppercaseEnums

    def validateIdentifier(name):
        # validation function Py2
        isId = lambda x: PythonIdentifierRegex.match(x)  # noqa: E731
        # ... Py3
        if sys.version_info.major == 3:
            isId = lambda x: x.isidentifier()  # noqa: E731

        # This will turn a string 'fooBar123' to 'foo_Bar_123'
        for regex in NameSeparationRegexList:
            name = regex.sub(r"\1_\2", name)

        if UppercaseEnums:
            name = name.upper()

        name = NonAlphaNumRegex.sub("", name)

        if not isId(name):
            # it may start with a digit
            escapedName = '_%s' % name
            if isId(escapedName):
                return NameTable.get(escapedName, escapedName)
            else:
                raise ValueError

        return NameTable.get(name, name)

    def make_unique_label(value, enum_labels):
        """Make sure that the label is unique."""
        unique_value = value
        count = 0
        while unique_value in enum_labels:
            count += 1
            unique_value = '{}_{}'.format(value, count)
        enum_labels.add(unique_value)
        return unique_value

    def writeEnumClass(simpleType):
        enumValues = simpleType.getEnumValues()
        simpleTypeName = cleanupName(simpleType.getName())
        enum_labels = set()
        if enumValues:
            output = ""
            try:
                validateIdentifier(simpleTypeName)
            except ValueError:
                err_msg(
                    '*** The Simple Type name "%s" is not a valid '
                    'Python identifier\n' % simpleTypeName)
                return
            output += 'class %s(str, Enum):\n' % simpleTypeName
            docstring = generateDocString(simpleType)
            output += docstring if docstring else ''
            for enumValue in enumValues:
                try:
                    validatedEnumValue = validateIdentifier(enumValue)
                except ValueError:
                    err_msg(
                        '*** The enumeration value "%s" is not a valid Python '
                        'identifier\n' % enumValue)
                    return
                validatedEnumValue = make_unique_label(
                    validatedEnumValue, enum_labels)
                valdoc = simpleType.getEnumValueDocumentation(enumValue)
                cleanEnumValue = enumValue.replace("'", "\\'")
                output += ('    ' + validatedEnumValue + '=\'' +
                           cleanEnumValue + '\'')
                if valdoc:
                    # Use DocEnum and pass this as argument when python3 only
                    output += (' # ' + valdoc)
                output += '\n'
            output = version_py2_encode(output)
            wrt(output)
            wrt('\n\n')

    for simpletypeName in sorted(simpleTypeDict.keys()):
        if ':' not in simpletypeName or (
                not SingleFileOutput and
                root.targetNamespace and
                root.targetNamespace !=
                get_prefix_and_value(simpletypeName)[0]):
            continue
        simpleType = simpleTypeDict[simpletypeName]
        writeEnumClass(simpleType)
# end generateSimpleTypes


def getImportsForExternalXsds(root):
    '''
    If we are creating a file per xsd, then
    we need to import any external classes we use
    '''
    externalImports = set()
    if not SingleFileOutput:
        childStack = list(root.getChildren())
        while len(childStack) > 0:
            child = childStack.pop()
            if child.namespace and child.namespace != root.targetNamespace:
                fqn = child.getFullyQualifiedType()
                if fqn in fqnToModuleNameMap and fqn in fqnToElementDict:
                    schemaElement = fqnToElementDict[fqn]
                    moduleName = fqnToModuleNameMap[fqn]
                    elementType = schemaElement.getType()
                    if elementType == CurrentNamespacePrefix + "string":
                        elementType = schemaElement.getName()
                    if child.namespace in NamespaceToCustomImportPath:
                        externalImports.add(
                            "from %s import %s" % (
                                NamespaceToCustomImportPath[child.namespace],
                                elementType))
                    else:
                        externalImports.add(
                            "from .%s%s import %s" % (
                                moduleName, ModuleSuffix, elementType))
            if child.getBase():
                _, parentObj = getParentName(child)
                if parentObj is not None:
                    fqnChild = child.getFullyQualifiedName()
                    fqnParent = parentObj.getFullyQualifiedName()
                    moduleNameChild = fqnToModuleNameMap.get(fqnChild)
                    moduleNameParent = fqnToModuleNameMap.get(fqnParent)
                    if (moduleNameParent is not None and
                            moduleNameChild is not None and
                            moduleNameParent != moduleNameChild):
                        parentType = parentObj.getType()
                        if parentType == CurrentNamespacePrefix + "string":
                            parentType = parentObj.getName()
                        externalImports.add("from .%s%s import %s" % (
                            moduleNameParent, ModuleSuffix, parentType))
            for subChild in child.getChildren():
                childStack.append(subChild)
    return externalImports
# end getImportsForExternalXsds


def isNewState():
    state = reduce(
        operator.concat,
        (str(id(item)) for item in PostponedExtensions))
    if sys.version_info.major == 2:
        sum = hashlib.sha1(str(state)).hexdigest()
    else:
        sum = hashlib.sha1(str(state).encode()).hexdigest()
    if sum in LoopcheckOneperChecksums:
        return False
    LoopcheckOneperChecksums.add(sum)
    return True


def generate(outfileName, subclassFilename, behaviorFilename,
             prefix, root, options, args, superModule, customImports):
    global DelayedElements, DelayedElements_subclass, AlreadyGenerated
    # Create an output file.
    # Note that even if the user does not request an output file,
    #   we still need to go through the process of generating classes
    #   because it produces data structures needed during generation of
    #   subclasses.
    MappingTypes.clear()
    generatedClasses = set()
    outfile = None
    outfile = makeFile(outfileName)
    wrt = outfile.write
    processed = []
    externalImports = getImportsForExternalXsds(root)
    generateHeader(wrt, prefix, options, args, externalImports, customImports)
    generateSimpleTypes(wrt, prefix, SimpleTypeDict, root)
    DelayedElements = set()
    DelayedElements_subclass = set()
    elements = root.getChildren()
    already_seen = set()
    generateFromTree(wrt, prefix, elements, processed, already_seen)
    for element in elements:
        if element.getFullyQualifiedName() in AlreadyGenerated:
            generatedClasses.add(element.getCleanName())
    while 1:
        if len(DelayedElements) <= 0:
            break
        element = DelayedElements.pop()
        name = element.getCleanName()
        if name not in processed:
            processed.append(name)
            if NoNameSpaceDefs:
                nameSpacesDef = ""
            else:
                nameSpacesDef = getUsedNamespacesDefs(element)
            generateClasses(wrt, prefix, element, 1, nameSpacesDef)
            if element.getFullyQualifiedName() in AlreadyGenerated:
                generatedClasses.add(element.getCleanName())
    #
    # Generate the elements that were postponed because we had not
    #   yet generated their base class.
    while len(PostponedExtensions) > 0:
        if not isNewState():
            sys.stderr.write('\n*** maxLoops exceeded.  Something is '
                             'wrong.\n\n')
            sys.stderr.write(
                '*** Failed to process the following element '
                'definitions:\n    %s\n' % (PostponedExtensions))
            break
        element = PostponedExtensions.pop()
        parentName, parent = getParentName(element)
        if parentName:
            if (parent.getFullyQualifiedName() in AlreadyGenerated or
                    parentName in SimpleTypeDict):
                if NoNameSpaceDefs:
                    nameSpacesDef = ""
                else:
                    nameSpacesDef = getUsedNamespacesDefs(element)
                generateClasses(wrt, prefix, element, 1, nameSpacesDef)
                generatedClasses.add(element.getCleanName())
            else:
                PostponedExtensions.insert(0, element)

    #
    # Disable the generation of SAX handler/parser.
    # It failed when we stopped putting simple types into ElementDict.
    # When there are duplicate names, the SAX parser probably does
    #   not work anyway.
    generateMain(outfile, prefix, root, generatedClasses)
    outfile.close()
    if subclassFilename:
        generateSubclasses(
            root, subclassFilename, behaviorFilename,
            prefix, options, args, superModule)
    return generatedClasses
# end generate


def makeFile(outFileName):
    outFile = None
    if (not Force) and os.path.exists(outFileName):
        if NoQuestions:
            sys.stderr.write(
                'File %s exists.  Change output file or use -f (force).\n' %
                outFileName)
            sys.exit('Exiting.  No output file.')
        else:
            reply = input(
                'File %s exists.  Overwrite? (y/n): ' % outFileName)
            if reply == 'y':
                if sys.version_info.major == 2:
                    outFile = open(outFileName, 'w')
                else:
                    outFile = open(outFileName, 'w', encoding='utf-8')
            else:
                sys.exit('Exiting.  No output file.')
    else:
        if sys.version_info.major == 2:
            outFile = open(outFileName, 'w')
        else:
            outFile = open(outFileName, 'w', encoding='utf-8')
    return outFile


def version_py2_encode(s1):
    if s1 and sys.version_info.major == 2:
        s1 = s1.encode('utf-8')
    return s1


def get_parser_validator(item_type):
    if item_type == FloatType:
        parser_name = 'gds_parse_float'
        validator_name = 'gds_validate_float'
    elif item_type == DoubleType:
        parser_name = 'gds_parse_double'
        validator_name = 'gds_validate_double'
    elif item_type == DecimalType:
        parser_name = 'gds_parse_decimal'
        validator_name = 'gds_validate_decimal'
    else:
        parser_name = None
        validator_name = None
    return parser_name, validator_name


def mapName(oldName):
    newName = oldName
    if oldName in NameTable:
        newName = NameTable[oldName]
    return newName


def cleanupName(oldName):
    newName = oldName
    for pattern, repl in CleanupNameList:
        newName = re.sub(pattern, repl, newName)
    return newName


def make_gs_name(oldName):
    if UseGetterSetter == 'old':
        newName = oldName.capitalize()
    elif UseGetterSetter == 'new':
        newName = '_%s' % oldName
    else:
        newName = ''
    return newName


def fixDjangoName(name):
    if name == 'id':
        name += '_x'
    elif name.endswith('_') and not name == AnyTypeIdentifier:
        name += 'x'
    return name


fixSQLAlchemyName = fixDjangoName


def strip_namespace(val):
    return val.split(':')[-1]


def get_prefix_and_value(val):
    if ':' in val:
        return val.split(':')
    return None, val


def escape_string(instring):
    s1 = instring
    s1 = s1.replace('\\', '\\\\')
    s1 = s1.replace("'", "\\'")
    return s1


def is_builtin_simple_type(type_val):
    if (type_val in StringType or
            type_val == TokenType or
            type_val in DateTimeGroupType or
            type_val in IntegerType or
            type_val == DecimalType or
            type_val == PositiveIntegerType or
            type_val == NonPositiveIntegerType or
            type_val == NegativeIntegerType or
            type_val == NonNegativeIntegerType or
            type_val == BooleanType or
            type_val == FloatType or
            type_val == DoubleType or
            type_val in OtherSimpleTypes):
        return True
    else:
        return False


#
# Copy namespace map.
# If "xsd" is in namespace map, replace with "xs".
# Remove None.
def fix_lxml_nsmap(nsmap):
    nsmap = nsmap.copy()
    if 'xsd' in nsmap:
        nsmap['xs'] = nsmap.get('xsd')
        nsmap.pop('xsd')
    elif None in nsmap and 'xs' not in nsmap:
        nsmap['xs'] = nsmap.pop(None)
    if None in nsmap:
        nsmap.pop(None)
    return nsmap


def parseAndGenerate(
        outfileName,
        subclassFilename,
        prefix,
        xschemaFileName,
        behaviorFilename,
        catalogFilename,
        processIncludes,
        options,
        noCollectIncludes,
        noRedefineGroups,
        args,
        superModule='???',
        customImports=None):
    global DelayedElements, DelayedElements_subclass, \
        AlreadyGenerated, SaxDelayedElements, \
        AlreadyGenerated_subclass, UserMethodsPath, UserMethodsModule, \
        SchemaLxmlTree, SchemaLxmlTreeMap, SchemaRenameMap, \
        ModuleSuffix, UseSourceFileAsModuleName, \
        SchemaNamespaceDict
    DelayedElements = set()
    DelayedElements_subclass = set()
    AlreadyGenerated = set()
    AlreadyGenerated_subclass = set()
    if UserMethodsPath:
        # UserMethodsModule = __import__(UserMethodsPath)
        if sys.version_info.major == 2:
            path_list = UserMethodsPath.split('/')
            mod_name = path_list[-1]
            mod_name = mod_name.split('.')[0]
            mod_path = path_list[:-1]
            mod_path = '/'.join(mod_path)
            module_spec = imp.find_module(mod_name, [mod_path, ])
            UserMethodsModule = imp.load_module(mod_name, *module_spec)
        else:
            path_list = UserMethodsPath.split('/')
            mod_name = path_list[-1]
            mod_path = UserMethodsPath
            module_spec = importlib.util.spec_from_file_location(
                mod_name, mod_path)
            UserMethodsModule = importlib.util.module_from_spec(module_spec)
            module_spec.loader.exec_module(UserMethodsModule)
##    parser = saxexts.make_parser("xml.sax.drivers2.drv_pyexpat")
    if xschemaFileName == '-':
        infile = sys.stdin
    else:
        infile = open(xschemaFileName, 'rb')
    if SingleFileOutput:
        parser = make_parser()
        dh = XschemaHandler()
        parser.setContentHandler(dh)
        if processIncludes:
            import process_includes
            if sys.version_info.major == 2:
                outfile = StringIO.StringIO()
            else:
                outfile = io.StringIO()
            result = process_includes.process_include_files(
                infile, outfile,
                inpath=xschemaFileName,
                catalogpath=catalogFilename,
                fixtypenames=FixTypeNames,
                no_collect_includes=noCollectIncludes,
                no_redefine_groups=noRedefineGroups,
            )
            doc, SchemaNamespaceDict, schema_ns_dict, rename_data = result
            SchemaRenameMap = rename_data.name_mappings
            prefixToNamespaceMap.update(schema_ns_dict)
            outfile.seek(0)
            infile = outfile
            SchemaLxmlTree = doc.getroot()
            SchemaLxmlTreeMap = fix_lxml_nsmap(SchemaLxmlTree.nsmap)
        else:
            print('xschemaFileName: {}'.format(xschemaFileName))
            from lxml import etree
            doc = etree.parse(xschemaFileName)
            SchemaLxmlTree = doc.getroot()
            SchemaLxmlTreeMap = fix_lxml_nsmap(SchemaLxmlTree.nsmap)
            rename_data = None
        parser.parse(infile)
        root = dh.getRoot()
        root.annotate()
        #generatedClasses = generate(
        generate(
            outfileName, subclassFilename, behaviorFilename,
            prefix, root, options, args, superModule, customImports)

        if outfileName:
            outfile = open(outfileName, "a")
            # Generate a dictionary showing any renaming that was
            # done because of duplicate (unqualified) names in
            # different namespaces.
            # This dictionary maps namespace+unqualified-name to
            # the new unique names.
            if rename_data is not None:
                renaming_lines = [
                    '    "{}": "{}",\n'.format(item[0], item[1])
                    for item in rename_data.name_mappings.items()]
                renaming_lines.sort()
                renaming_lines = ''.join(renaming_lines)
                rename_content = 'RenameMappings_ = {{\n{}}}\n'.format(
                    renaming_lines)
                outfile.write(rename_content)
            # Generate a mapping from name spaces to the definitions
            # in each namespace.
            if xschemaFileName != '-':
                infile = open(xschemaFileName, 'rb')
                rootPaths = process_includes.get_all_root_file_paths(
                    infile, inpath=xschemaFileName,
                    catalogpath=catalogFilename)
                opts = argparse.Namespace(
                    schema_file_names=rootPaths,
                    force=False,
                    no_out=True,
                    outfile='',
                    silence=False,
                    verbose=False
                )
                import gds_collect_namespace_mappings as cnm
                namespace_mappings = cnm.create_mapping(opts, globals())
                formatted_mappings = pprint.pformat(namespace_mappings)
                wrt = outfile.write
                wrt('\n#\n')
                wrt('# Mapping of namespaces to types defined in them\n')
                wrt('# and the file in which each is defined.\n')
                wrt('# simpleTypes are marked "ST" and complexTypes "CT".\n')
                wrt('NamespaceToDefMappings_ = {}\n'.format(
                    formatted_mappings))
            # Generate __all__, which, when the generated file
            # is used as a module, is useful to isolate
            # important classes from internal ones. This way one
            # can do a reasonably safe "from parser import *"
            exportableClassList = [
                '"%s%s"' % (prefix, name, )
                for name in AllGeneratedClassNames]
            exportableClassList.sort()
            exportableClassNames = ',\n    '.join(exportableClassList)
            exportLine = "\n__all__ = [\n    %s\n]\n" % exportableClassNames
            outfile.write(exportLine)
            outfile.close()
    else:    # not SingleFileOutput
        import process_includes
        if processIncludes:
            if sys.version_info.major == 2:
                outfile = StringIO.StringIO()
            else:
                outfile = io.StringIO()
            result = process_includes.process_include_files(
                infile, outfile,
                inpath=xschemaFileName,
                catalogpath=catalogFilename,
                fixtypenames=FixTypeNames)
            doc, SchemaNamespaceDict, schema_ns_dict, rename_data = result
            SchemaRenameMap = rename_data.name_mappings
            prefixToNamespaceMap.update(schema_ns_dict)
            outfile.close()
            outfile = None
            SchemaLxmlTree = doc.getroot()
            SchemaLxmlTreeMap = fix_lxml_nsmap(SchemaLxmlTree.nsmap)
        infile.seek(0)
        rootPaths = process_includes.get_all_root_file_paths(
            infile, inpath=xschemaFileName,
            catalogpath=catalogFilename)
        roots = []
        rootInfos = []
        for path in rootPaths:
            if (path.startswith('https:') or
                    path.startswith('http:') or
                    path.startswith('ftp:')):
                try:
                    headers = {
                        'User-Agent':
                            "Mozilla/5.0 (X11; 'Linux x86_64) "
                            "AppleWebKit/537.36 (KHTML, like Gecko) ",
                    }
                    content = requests.get(path, headers=headers).content
                    if sys.version_info.major == 2:
                        rootFile = StringIO.StringIO()
                    else:
                        rootFile = io.StringIO()
                        content = content.decode()
                    rootFile.write(content)
                    rootFile.seek(0)
                except requests.exceptions.HTTPError:
                    msg = "Can't find file %s." % (path, )
                    raise IOError(msg)
            else:
                rootFile = open(path, 'r')
            parser = make_parser()
            dh = XschemaHandler()
            parser.setContentHandler(dh)
            parser.parse(rootFile)
            root = dh.getRoot()
            roots.append(root)
            rootFile.close()
        for root, rootPath in zip(roots, rootPaths):
            root.annotate()
            moduleName = os.path.splitext(os.path.basename(rootPath))[0]
            modulePath = None
            # register fully qualified names for all types defined in this XSD
            for child in root.getChildren():
                typeName = child.getType()
                if typeName.startswith(CurrentNamespacePrefix):
                    # no need to create a module for
                    # xs: types
                    continue
                fqnToModuleNameMap[child.getFullyQualifiedType()] = \
                    moduleName
                fqnToModuleNameMap[child.getFullyQualifiedName()] = \
                    moduleName
            if UseSourceFileAsModuleName:
                # use the root file name as module name
                modulePath = os.path.join(
                    OutputDirectory,
                    moduleName + ModuleSuffix + ".py")
            else:
                # use the first root element to set
                # up the module name and path
                for child in root.getChildren():
                    if child.isRootElement():
                        typeName = child.getType()
                        if typeName.startswith(CurrentNamespacePrefix):
                            # no need to create a module for
                            # xs: types
                            continue
                        # convert to lower camel case if needed.
                        if "-" in typeName:
                            tokens = typeName.split("-")
                            typeName = ''.join([t.title() for t in tokens])
                        moduleName = typeName[0].lower() + typeName[1:]
                        modulePath = (
                            OutputDirectory +
                            os.sep + moduleName +
                            ModuleSuffix + ".py")
            rootInfos.append((root, modulePath))
        generatedModules = set()
        for root, modulePath in rootInfos:
            if modulePath and modulePath not in generatedModules:
                generatedModules.add(modulePath)
                # Do not generate the file for the root that is imported from 
                # a custom location
                if root.targetNamespace in NamespaceToCustomImportPath:
                    modulePath = os.path.join(
                        os.path.dirname(modulePath), "__generateDS_remove.py")
                    try:
                        generate(modulePath,subclassFilename, behaviorFilename,
                            prefix, root, options, args, superModule, 
                            customImports)
                    finally:
                        if os.path.exists(modulePath):
                            os.remove(modulePath)
                    continue
                #generatedClasses = generate(
                generate(
                    modulePath, subclassFilename, behaviorFilename,
                    prefix, root, options, args, superModule, customImports)
                # Generate a dictionary showing any renaming that was
                # done because of duplicate (unqualified) names in
                # different namespaces.
                # This dictionary maps namespace+unqualified-name to
                # the new unique names.
                outfile = open(modulePath, "a")
                renaming_lines = [
                    '    "{}": "{}",\n'.format(item[0], item[1])
                    for item in rename_data.name_mappings.items()]
                renaming_lines.sort()
                renaming_lines = ''.join(renaming_lines)
                rename_content = 'RenameMappings_ = {{\n{}\n}}'.format(
                    renaming_lines)
                outfile.write(rename_content)
                # Generate __all__.  When using the parser as a module
                # it is useful
                # to isolate important classes from internal ones. This way one
                # can do a reasonably safe "from parser import *"
                exportableClassList = [
                    '"%s%s"' % (prefix, name, )
                    for name in AllGeneratedClassNames]
                exportableClassList.sort()
                exportableClassNames = ',\n    '.join(exportableClassList)
                exportLine = "\n__all__ = [\n    %s\n]\n" % (
                    exportableClassNames, )
                outfile.write(exportLine)
                outfile.close()
# end parseAndGenerate


# Function that gets called recursively in order to expand nested references
# to element groups
def _expandGR(grp, visited):
    # visited is used for loop detection
    children = []
    changed = False
    for child in grp.children:
        groupRef = child.getElementGroup()
        if not groupRef:
            children.append(child)
            continue
        ref = groupRef.ref
        referencedGroup = ElementGroups.get(ref, None)
        if referencedGroup is None:
            ref = strip_namespace(ref)
            referencedGroup = ElementGroups.get(ref, None)
        if referencedGroup is None:
            err_msg('*** Reference to unknown group %s\n' % groupRef.ref)
            continue
        visited.add(id(grp))
        if id(referencedGroup) in visited:
            #err_msg('*** Circular reference for %s' % groupRef.attrs['ref'])
            err_msg('*** Circular reference for %s\n' % groupRef.ref)
            continue
        changed = True
        _expandGR(referencedGroup, visited)
        children.extend(referencedGroup.children)
    if changed:
        # Avoid replacing the list with a copy of the list
        grp.children = children


def expandGroupReferences(grp):
    visited = set()
    _expandGR(grp, visited)


def load_config():
    try:
        #print('1. updating NameTable')
        import generateds_config
        NameTable.update(generateds_config.NameTable)
        #print('2. updating NameTable', generateds_config.NameTable)
        #print('3. NameTable:', NameTable)
    except ModulenotfoundExp_:
        pass


def fixSilence(txt, silent):
    if silent:
        txt = txt.replace('#silence#', '## ')
    else:
        txt = txt.replace('#silence#', '')
    return txt


def fixXmlDisable(txt, disabled):
    if disabled:
        txt = txt.replace('#xmldisable#', '## ')
    else:
        txt = txt.replace('#xmldisable#', '')
    return txt


def capture_cleanup_name_list(option):
    cleanupNameList = []
    if not option:
        return cleanupNameList
    # remove extra whitespace
    cleanup_str = option.strip()
    # remove extra quotes
    while cleanup_str[0] == cleanup_str[-1] and cleanup_str[0] in '"\'':
        cleanup_str = cleanup_str[1:-1]
    from ast import literal_eval
    try:
        cleanup_list = literal_eval(cleanup_str)
    except ValueError:
        raise RuntimeError(
            'Unable to parse option --cleanup-name-list.')
    if type(cleanup_list) not in (list, tuple):
        raise RuntimeError(
            'Option --cleanup-name-list must be a list or a tuple.')
    for cleanup_pair in cleanup_list:
        if sys.version_info.major == 2:
            if (type(cleanup_pair) not in (list, tuple) or
                    len(cleanup_pair) != 2 or
                    not isinstance(cleanup_pair[0], BaseStrTypes) or
                    not isinstance(cleanup_pair[1], BaseStrTypes)):
                raise RuntimeError(
                    'Option --cleanup-name-list contains '
                    'invalid element.')
        else:
            if (type(cleanup_pair) not in (list, tuple) or
                    len(cleanup_pair) != 2 or
                    not isinstance(cleanup_pair[0], str) or
                    not isinstance(cleanup_pair[1], str)):
                raise RuntimeError(
                    'Option --cleanup-name-list contains '
                    'invalid element.')
        try:
            if sys.version_info.major == 2:
                target = cleanup_pair[0].decode('utf-8')
            else:
                target = cleanup_pair[0]
            cleanupNameList.append(
                (re.compile(target), cleanup_pair[1]))
        except Exception:
            raise RuntimeError(
                'Option --cleanup-name-list contains invalid '
                'pattern "%s".'
                % cleanup_pair[0])
    return cleanupNameList


def capture_fq_attr_name(name):
    fully_qualified_name = None
    split_name = name.split(':')
    if (len(split_name) == 2 and
            (split_name[0] == 'xml' or
                split_name[0] == 'xlink')):
        fully_qualified_name = name
    return fully_qualified_name


def err_msg(msg):
    if not NoWarnings:
        sys.stderr.write(msg)


USAGE_TEXT = __doc__


def usage():
    print(USAGE_TEXT)
    sys.exit(1)


def main():
    global Force, GenerateProperties, SubclassSuffix, RootElement, \
        ValidatorBodiesBasePath, UseGetterSetter, \
        UserMethodsPath, XsdNameSpace, \
        Namespacedef, NoNameSpaceDefs, NoDates, NoVersion, TEMPLATE_HEADER, \
        TEMPLATE_GENERATEDS_SUPER, \
        TEMPLATE_MAIN, TEMPLATE_SUBCLASS_FOOTER, TEMPLATE_SUBCLASS_HEADER,\
        Dirpath, ExternalEncoding, MemberSpecs, NoQuestions, \
        ExportWrite, ExportEtree, ExportLiteral, ExportDjango, \
        ExportSQLAlchemy, GenerateValidatorMethods, \
        GenerateRecursiveGenerator, XmlDisabled, UseSlots, \
        FixTypeNames, SingleFileOutput, OutputDirectory, \
        ModuleSuffix, UseOldSimpleTypeValidators, \
        UseGeneratedssuperLookup, UseSourceFileAsModuleName, \
        PreserveCdataTags, CleanupNameList, \
        NoWarnings, AlwaysExportDefault, \
        UppercaseEnums, CreateMandatoryChildren, \
        GDSImportPath, NamespaceToCustomImportPath
    outputText = True
    args = sys.argv[1:]
    try:
        options, args = getopt.getopt(
            args, 'hfyo:s:p:a:b:c:mu:q',
            [
                'help', 'subclass-suffix=',
                'root-element=', 'super=',
                'validator-bodies=', 'use-getter-setter=',
                'user-methods=', 'no-process-includes', 'silence',
                'namespacedef=', 'no-namespace-defs', 'external-encoding=',
                'member-specs=', 'no-dates', 'no-versions',
                'no-questions', 'session=', 'fix-type-names=',
                'version', 'export=', 'disable-xml', 'enable-slots',
                'one-file-per-xsd', 'output-directory=',
                'module-suffix=', 'use-old-simpletype-validators',
                'preserve-cdata-tags', 'cleanup-name-list=',
                'disable-generatedssuper-lookup',
                'use-source-file-as-module-name',
                'no-warnings',
                'no-collect-includes', 'no-redefine-groups',
                'always-export-default', 'mixed-case-enums',
                'create-mandatory-children', 'import-path=',
                'custom-imports-template=', 'namespace-to-import-path-configuration-file='
            ])
    except getopt.GetoptError:
        usage()
    prefix = ''
    outFilename = None
    subclassFilename = None
    behaviorFilename = None
    nameSpace = 'xs:'
    superModule = '???'
    processIncludes = 1
    namespacedef = ''
    NoNameSpaceDefs = False
    ExternalEncoding = ''
    NoDates = False
    NoVersion = False
    NoQuestions = False
    AlwaysExportDefault = False
    showVersion = False
    xschemaFileName = None
    catalogFilename = None
    noCollectIncludes = False
    noRedefineGroups = False
    UppercaseEnums = True
    CreateMandatoryChildren = False
    GDSImportPath = ''
    customImports = None
    for option in options:
        if option[0] == '--session':
            sessionFilename = option[1]
            from libgenerateDS.gui import generateds_gui_session
            from lxml import etree
            doc = etree.parse(sessionFilename)
            rootNode = doc.getroot()
            sessionObj = generateds_gui_session.sessionType()
            sessionObj.build(rootNode)
            if sessionObj.get_input_schema():
                xschemaFileName = sessionObj.get_input_schema()
            if sessionObj.get_output_superclass():
                outFilename = sessionObj.get_output_superclass()
            if sessionObj.get_output_subclass():
                subclassFilename = sessionObj.get_output_subclass()
            if sessionObj.get_force():
                Force = True
            if sessionObj.get_prefix():
                prefix = sessionObj.get_prefix()
            if sessionObj.get_empty_namespace_prefix():
                nameSpace = ''
            elif sessionObj.get_namespace_prefix():
                nameSpace = sessionObj.get_namespace_prefix()
            if sessionObj.get_behavior_filename():
                behaviorFilename = sessionObj.get_behavior_filename()
            if sessionObj.get_properties():
                GenerateProperties = True
            if sessionObj.get_subclass_suffix():
                SubclassSuffix = sessionObj.get_subclass_suffix()
            if sessionObj.get_root_element():
                RootElement = sessionObj.get_root_element()
            if sessionObj.get_superclass_module():
                superModule = sessionObj.get_superclass_module()
            if sessionObj.get_old_getters_setters():
                UseGetterSetter = option[1]
            if sessionObj.get_validator_bodies():
                ValidatorBodiesBasePath = sessionObj.get_validator_bodies()
                if not os.path.isdir(ValidatorBodiesBasePath):
                    err_msg('*** Option validator-bodies must specify '
                            'an existing path.\n')
                    sys.exit(1)
            if sessionObj.get_user_methods():
                UserMethodsPath = sessionObj.get_user_methods()
            if sessionObj.get_no_dates():
                NoDates = True
            if sessionObj.get_no_versions():
                NoVersion = True
            if sessionObj.get_no_process_includes():
                processIncludes = 0
            if sessionObj.get_silence():
                outputText = False
            if sessionObj.get_namespace_defs():
                namespacedef = sessionObj.get_namespace_defs()
            if sessionObj.get_external_encoding():
                ExternalEncoding = sessionObj.get_external_encoding()
            if sessionObj.get_member_specs() in ('list', 'dict'):
                MemberSpecs = sessionObj.get_member_specs()
            exports = sessionObj.get_export_spec()
            if exports:
                ExportWrite = False
                ExportEtree = False
                ExportLiteral = False
                ExportDjango = False
                ExportSQLAlchemy = False
                GenerateValidatorMethods = False
                GenerateRecursiveGenerator = False
                exports = exports.split()
                if 'write' in exports:
                    ExportWrite = True
                if 'etree' in exports:
                    ExportEtree = True
                if 'literal' in exports:
                    ExportLiteral = True
                if 'django' in exports:
                    ExportDjango = True
                if 'sqlalchemy' in exports:
                    ExportSQLAlchemy = True
                if 'validate' in exports:
                    GenerateValidatorMethods = True
                if 'generator' in exports:
                    GenerateRecursiveGenerator = True
            if sessionObj.get_one_file_per_xsd():
                SingleFileOutput = False
            if sessionObj.get_output_directory():
                OutputDirectory = sessionObj.get_output_directory()
            if sessionObj.get_module_suffix():
                ModuleSuffix = sessionObj.get_module_suffix()
            if sessionObj.get_preserve_cdata_tags():
                PreserveCdataTags = True
            CleanupNameList = capture_cleanup_name_list(
                sessionObj.get_cleanup_name_list())
            break
    for option in options:
        if option[0] == '-h' or option[0] == '--help':
            usage()
        elif option[0] == '-p':
            prefix = option[1]
        elif option[0] == '-o':
            outFilename = option[1]
        elif option[0] == '-s':
            subclassFilename = option[1]
        elif option[0] == '-f':
            Force = 1
        elif option[0] == '-a':
            nameSpace = option[1]
        elif option[0] == '-b':
            behaviorFilename = option[1]
        elif option[0] == '-c':
            catalogFilename = option[1]
        elif option[0] == '-m':
            GenerateProperties = 1
        elif option[0] == '--no-dates':
            NoDates = True
        elif option[0] == '--no-versions':
            NoVersion = True
        elif option[0] == '--subclass-suffix':
            SubclassSuffix = option[1]
        elif option[0] == '--root-element':
            RootElement = option[1]
        elif option[0] == '--super':
            superModule = option[1]
        elif option[0] == '--validator-bodies':
            ValidatorBodiesBasePath = option[1]
            if not os.path.isdir(ValidatorBodiesBasePath):
                err_msg('*** Option validator-bodies must specify an '
                        'existing path.\n')
                sys.exit(1)
        elif option[0] == '--use-getter-setter':
            if option[1] in ('old', 'new', 'none'):
                UseGetterSetter = option[1]
            else:
                err_msg('*** Option use-getter-setter must '
                        '"old" or "new" or "none".\n')
                sys.exit(1)
        elif option[0] == '--use-old-simpletype-validators':
            UseOldSimpleTypeValidators = True
        elif option[0] in ('-u', '--user-methods'):
            UserMethodsPath = option[1]
        elif option[0] == '--no-process-includes':
            processIncludes = 0
        elif option[0] == "--silence":
            outputText = False
        elif option[0] == "--namespacedef":
            namespacedef = option[1]
        elif option[0] == "--no-namespace-defs":
            NoNameSpaceDefs = True
        elif option[0] == '--external-encoding':
            ExternalEncoding = option[1]
        elif option[0] in ('-q', '--no-questions'):
            NoQuestions = True
        elif option[0] == "--fix-type-names":
            FixTypeNames = option[1]
        elif option[0] == '--version':
            showVersion = True
        elif option[0] == '--member-specs':
            MemberSpecs = option[1]
            if MemberSpecs not in ('list', 'dict', ):
                raise RuntimeError(
                    'Option --member-specs must be "list" or "dict".')
        elif option[0] == '--export':
            ExportWrite = False
            ExportEtree = False
            ExportLiteral = False
            ExportDjango = False
            ExportSQLAlchemy = False
            GenerateValidatorMethods = False
            GenerateRecursiveGenerator = False
            tmpoptions = option[1].split()
            if 'write' in tmpoptions:
                ExportWrite = True
            if 'etree' in tmpoptions:
                ExportEtree = True
            if 'literal' in tmpoptions:
                ExportLiteral = True
            if 'django' in tmpoptions:
                ExportDjango = True
            if 'sqlalchemy' in tmpoptions:
                ExportSQLAlchemy = True
            if 'validate' in tmpoptions:
                GenerateValidatorMethods = True
            if 'generator' in tmpoptions:
                GenerateRecursiveGenerator = True
        elif option[0] == '--disable-xml':
            XmlDisabled = True
        elif option[0] == '--enable-slots':
            UseSlots = True
        elif option[0] == '--disable-generatedssuper-lookup':
            UseGeneratedssuperLookup = False
        elif option[0] == '--use-source-file-as-module-name':
            UseSourceFileAsModuleName = True
        elif option[0] == '--one-file-per-xsd':
            SingleFileOutput = False
        elif option[0] == "--output-directory":
            OutputDirectory = option[1]
        elif option[0] == "--module-suffix":
            ModuleSuffix = option[1]
        elif option[0] == "--preserve-cdata-tags":
            PreserveCdataTags = True
        elif option[0] == '--cleanup-name-list':
            CleanupNameList = capture_cleanup_name_list(option[1])
        elif option[0] == '--no-warnings':
            NoWarnings = True
        elif option[0] == '--no-collect-includes':
            noCollectIncludes = True
        elif option[0] == '--no-redefine-groups':
            noRedefineGroups = True
        elif option[0] == '--always-export-default':
            AlwaysExportDefault = True
        elif option[0] == '--mixed-case-enums':
            UppercaseEnums = False
        elif option[0] == '--create-mandatory-children':
            CreateMandatoryChildren = True
        elif option[0] == '--import-path':
            GDSImportPath = option[1]
        elif option[0] == '--custom-imports-template':
            if not os.path.isfile(option[1]):
                err_msg('*** Custom imports template must be a valid file.\n')
                sys.exit(1)
            cit = open(option[1])
            customImports = cit.readlines()
            cit.close()
        elif option[0] == '--namespace-to-import-path-configuration-file':
            with open(option[1]) as namespaceToImportFile:
                NamespaceToCustomImportPath = json.load(namespaceToImportFile)
    if UseSlots and MemberSpecs != 'dict':
        raise RuntimeError(
            'Option --enable--slots must be used with --member-specs=dict.')
    if showVersion:
        print('generateDS.py version %s' % VERSION)
        sys.exit(0)
    XsdNameSpace = nameSpace
    Namespacedef = namespacedef
    set_type_constants(nameSpace)
    if behaviorFilename and not subclassFilename:
        err_msg(USAGE_TEXT)
        err_msg('\n*** Error.  Option -b requires -s\n')
    if xschemaFileName is None:
        if len(args) != 1:
            usage()
        else:
            xschemaFileName = args[0]
            XsdFileName.append(xschemaFileName)
    silent = not outputText
    TEMPLATE_HEADER = fixXmlDisable(TEMPLATE_HEADER, XmlDisabled)
    TEMPLATE_GENERATEDS_SUPER = fixXmlDisable(
        TEMPLATE_GENERATEDS_SUPER, XmlDisabled)
    TEMPLATE_MAIN = fixSilence(TEMPLATE_MAIN, silent)
    TEMPLATE_SUBCLASS_HEADER = fixXmlDisable(
        TEMPLATE_SUBCLASS_HEADER, XmlDisabled)
    TEMPLATE_SUBCLASS_FOOTER = fixSilence(TEMPLATE_SUBCLASS_FOOTER, silent)

    load_config()
    if outFilename is None and SingleFileOutput:
        sys.exit('\nMissing required option "-o" (output module name)\n')
    parseAndGenerate(
        outFilename,
        subclassFilename,
        prefix,
        xschemaFileName,
        behaviorFilename,
        catalogFilename,
        processIncludes,
        options,
        noCollectIncludes,
        noRedefineGroups,
        args,
        superModule=superModule,
        customImports=customImports)


if __name__ == '__main__':
    # Default logger configuration
    logging.basicConfig(
        level=logging.WARNING,
        #format='%(asctime)s %(levelname)s %(message)s',
        # log file and function names
        format="%(levelname)s - %(pathname)s - %(funcName)s - %(message)s",
        #stream=sys.stdout,
        #filemode='w',      # Can uncomment this line or change to append ('a')
        #filename='generateDS.log'  # uncomment to send messages to file
    )
    #import pdb; pdb.set_trace()
    #import ipdb; ipdb.set_trace()
    # use the following to debug after an exception (post mortem debbing).
    #try:
    #    main()
    #except:
    #    import pdb; pdb.post_mortem()
    main()
# vim: tabstop=8 expandtab shiftwidth=4 softtabstop=4
