import jmake

jmake.setupenv()

workspace = jmake.Workspace('openxlsx')
workspace.lang = 'cpp17'

openxlsx = jmake.Project('openxlsx', target=jmake.Target.STATIC_LIBRARY)

cpp_files = jmake.glob('OpenXLSX', '**/*.cpp')
hpp_files = jmake.glob('OpenXLSX', '**/*.hpp')

openxlsx.add(cpp_files)
openxlsx.add(hpp_files)

external = 'OpenXLSX/external'
openxlsx.include(jmake.fullpath([ f"{external}/nowide", f"{external}/zippy", f"{external}/pugixml", "OpenXLSX/headers",
                                 "OpenXLSX/sources", "OpenXLSX", ]))

# note that this is msvc specific, enable alternative token support
openxlsx.compile('/Za')
openxlsx.export(includes=jmake.fullpath('OpenXLSX'))

debug = openxlsx.filter('debug')
debug['debug'] = True

test = jmake.Project('test', target=jmake.Target.EXECUTABLE)
test.add(jmake.fullpath(['Examples/Demo1.cpp']))
test.depend(openxlsx)

test['debug'] = True

workspace.add(openxlsx)
workspace.add(test)

jmake.generate(workspace)
