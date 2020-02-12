# >>> from bible import *
# >>> base(12, 595)
# [4, 1, 7]
# >>> base
# <function base at 0xb6590150>
# >>> import itertools
# >>> dir(itertools)
# ['__doc__', '__loader__', '__name__', '__package__', '__spec__', '_grouper', '_tee', '_tee_dataobject', 'accumulate', 'chain', 'combinations', 'combinations_with_replacement', 'compress', 'count', 'cycle', 'dropwhile', 'filterfalse', 'groupby', 'islice', 'permutations', 'product', 'repeat', 'starmap', 'takewhile', 'tee', 'zip_longest']
# >>> list(itertools.islice(fbase(23,math.pi),23))
# [3, 3, 5, 20, 17, 9, 20, 8, 1, 3, 19, 20, 7, 0, 15, 19, 19, 19, 21, 1, 5, 0, 18]
# >>> from table import *
# >>> Row[_]
# Row([3, 3, 5, 20, 17, 9, 20, 8, 1, 3, 19, 20, 7, 0, 15, 19, 19, 19, 21, 1, 5, 0, 18])
# >>> tod='0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.__getitem__
# >>> ''.join(_@tod)
# '335kh9k813jk70fjjjl150i'
# >>> 
# >>> list(itertools.islice(fbase(64,math.pi),23))
# [3, 9, 3, 61, 42, 34, 8, 22, 35, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# >>> chr(59),chr(0x59)
# (';', 'Y')
# >>> 
# >>> 
# >>> 
# >>> 
# >>> tell(ssum,osum,lsum,'cube cubes')
# cube cubes
# 310 + 410 =720
#  31 +  50 = 81
#  4  +  5  = 9
# >>> 31**(1/3)
# 3.1413806523913927
# >>> tell(ssum,osum,lsum,'guide')
# g  u  i d e
# 7+300+9+4+5=325
# 7+ 21+9+4+5= 46
# 1+ 1 +1+1+1= 5
# >>> tell(ssum,osum,lsum,'guides')
# g  u  i d e  s
# 7+300+9+4+5+100=425
# 7+ 21+9+4+5+ 19= 65
# 1+ 1 +1+1+1+ 1 = 6
# >>> b/'guide'
# Exodus 15:13;2 Chronicles 32:22;Job 31:18;38:32;Psalms 25:9;31:3;32:8;48:14;55:13;73:24;78:52,72;112:5;Proverbs 2:17;6:7;11:3;23:19;Isaiah 49:10;51:18;58:11;Jeremiah 3:4;Micah 7:5;Matthew 23:16,24;Luke 1:79;John 16:13;Acts 1:16;8:31;Romans 2:19;1 Timothy 5:14 (30 verses)
# >>> base(1189,31102)
# [26, 188]
# >>> base(33,1189)
# [1, 3, 1]
# >>> base(33,3088286401)
# [2, 12, 30, 4, 4, 0, 13]
# >>> int('2cu440d',33)
# 3088286401
# >>> bases(3088286401)
# 2 [1, 0, 1, 1, 1, 0, 0, 0, 0, 0, 0, 1, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 0, 1, 1, 0, 0, 0, 0, 0, 1]
# 3 [2, 1, 2, 2, 2, 0, 2, 0, 0, 1, 1, 0, 1, 2, 1, 1, 1, 2, 1, 1]
# 4 [2, 3, 2, 0, 0, 1, 0, 3, 2, 0, 0, 2, 3, 0, 0, 1]
# 5 [2, 2, 3, 1, 1, 1, 0, 0, 1, 3, 1, 1, 0, 1]
# 6 [1, 2, 3, 0, 2, 4, 0, 4, 1, 0, 1, 2, 1]
# 7 [1, 3, 6, 3, 5, 0, 0, 0, 0, 3, 0, 4]
# 8 [2, 7, 0, 0, 4, 7, 0, 1, 3, 0, 1]
# 9 [7, 8, 6, 6, 1, 3, 5, 4, 5, 4]
# 10 [3, 0, 8, 8, 2, 8, 6, 4, 0, 1]
# 11 [1, 3, 4, 5, 2, 9, 1, 3, 1, 2]
# 12 [7, 2, 2, 3, 1, 6, 9, 4, 1]
# 13 [3, 10, 2, 10, 8, 6, 5, 0, 5]
# 14 [2, 1, 4, 2, 2, 8, 11, 3, 11]
# 15 [1, 3, 1, 1, 13, 2, 12, 5, 1]
# 16 [11, 8, 1, 3, 8, 2, 12, 1]
# 17 [7, 8, 16, 1, 2, 14, 1, 16]
# 18 [5, 0, 14, 6, 17, 10, 2, 13]
# 19 [3, 8, 12, 4, 10, 2, 18, 10]
# 20 [2, 8, 5, 1, 15, 16, 0, 1]
# 21 [1, 15, 0, 3, 13, 5, 0, 4]
# 22 [1, 5, 5, 5, 8, 9, 0, 13]
# 23 [20, 19, 18, 19, 18, 11, 18]
# 24 [16, 3, 20, 8, 8, 8, 1]
# 25 [12, 16, 6, 0, 8, 6, 1]
# 26 [9, 25, 24, 2, 11, 0, 5]
# 27 [7, 26, 6, 4, 5, 13, 22]
# 28 [6, 11, 12, 11, 16, 22, 25]
# 29 [5, 5, 16, 12, 5, 23, 15]
# 30 [4, 7, 2, 20, 29, 10, 1]
# 31 [3, 14, 27, 1, 2, 14, 30]
# 32 [2, 28, 1, 7, 0, 22, 1]
# 33 [2, 12, 30, 4, 4, 0, 13]
# 34 [1, 33, 33, 0, 12, 0, 33]
# 35 [1, 23, 28, 0, 0, 4, 11]
# 36 [1, 15, 2, 24, 25, 1, 13]
# 37 [1, 7, 19, 30, 17, 10, 1]
# 38 [1, 0, 37, 3, 24, 18, 29]
# 39 [34, 8, 36, 13, 21, 31]
# 40 [30, 6, 14, 19, 0, 1]
# >>> dir(inspect)
# ['ArgInfo', 'ArgSpec', 'Arguments', 'Attribute', 'BlockFinder', 'BoundArguments', 'CORO_CLOSED', 'CORO_CREATED', 'CORO_RUNNING', 'CORO_SUSPENDED', 'CO_ASYNC_GENERATOR', 'CO_COROUTINE', 'CO_GENERATOR', 'CO_ITERABLE_COROUTINE', 'CO_NESTED', 'CO_NEWLOCALS', 'CO_NOFREE', 'CO_OPTIMIZED', 'CO_VARARGS', 'CO_VARKEYWORDS', 'ClosureVars', 'EndOfBlock', 'FrameInfo', 'FullArgSpec', 'GEN_CLOSED', 'GEN_CREATED', 'GEN_RUNNING', 'GEN_SUSPENDED', 'OrderedDict', 'Parameter', 'Signature', 'TPFLAGS_IS_ABSTRACT', 'Traceback', '_ClassMethodWrapper', '_KEYWORD_ONLY', '_MethodWrapper', '_NonUserDefinedCallables', '_PARAM_NAME_MAPPING', '_POSITIONAL_ONLY', '_POSITIONAL_OR_KEYWORD', '_ParameterKind', '_VAR_KEYWORD', '_VAR_POSITIONAL', '_WrapperDescriptor', '__author__', '__builtins__', '__cached__', '__doc__', '__file__', '__loader__', '__name__', '__package__', '__spec__', '_check_class', '_check_instance', '_empty', '_filesbymodname', '_findclass', '_finddoc', '_get_paramkind_descr', '_getfullargs', '_is_type', '_main', '_missing_arguments', '_sentinel', '_shadowed_dict', '_signature_bound_method', '_signature_from_builtin', '_signature_from_callable', '_signature_from_function', '_signature_fromstr', '_signature_get_bound_param', '_signature_get_partial', '_signature_get_user_defined_method', '_signature_is_builtin', '_signature_is_functionlike', '_signature_strip_non_python_syntax', '_static_getmro', '_too_many', '_void', 'abc', 'attrgetter', 'builtins', 'classify_class_attrs', 'cleandoc', 'collections', 'currentframe', 'dis', 'enum', 'findsource', 'formatannotation', 'formatannotationrelativeto', 'formatargspec', 'formatargvalues', 'functools', 'getabsfile', 'getargs', 'getargspec', 'getargvalues', 'getattr_static', 'getblock', 'getcallargs', 'getclasstree', 'getclosurevars', 'getcomments', 'getcoroutinelocals', 'getcoroutinestate', 'getdoc', 'getfile', 'getframeinfo', 'getfullargspec', 'getgeneratorlocals', 'getgeneratorstate', 'getinnerframes', 'getlineno', 'getmembers', 'getmodule', 'getmodulename', 'getmro', 'getouterframes', 'getsource', 'getsourcefile', 'getsourcelines', 'importlib', 'indentsize', 'isabstract', 'isasyncgen', 'isasyncgenfunction', 'isawaitable', 'isbuiltin', 'isclass', 'iscode', 'iscoroutine', 'iscoroutinefunction', 'isdatadescriptor', 'isframe', 'isfunction', 'isgenerator', 'isgeneratorfunction', 'isgetsetdescriptor', 'ismemberdescriptor', 'ismethod', 'ismethoddescriptor', 'ismodule', 'isroutine', 'istraceback', 'itertools', 'k', 'linecache', 'mod_dict', 'modulesbyfile', 'namedtuple', 'os', 're', 'signature', 'stack', 'sys', 'token', 'tokenize', 'trace', 'types', 'unwrap', 'v', 'walktree', 'warnings']
# >>> inspect.getfile(base)
# '/home/pi/python/parle/primes.py'
# >>> 
# >>> 
