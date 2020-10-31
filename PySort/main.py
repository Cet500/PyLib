# программа сортировки файлов по папкам по их типу или расширению

import os

from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

from conf import conf_ext


print( ' PythonSorter by SI ver 0.5' )
print( '-----------------------------------------------------------' )
print( ' Здравствуйте, ' + os.getlogin() + '!' )
print( ' Вас приветствует программа сортировки ваших файлов' )
print( '-----------------------------------------------------------' )
print( ' Давайте начнём с выбора задачи: ' )
print( '-----------------------------------------------------------' )
print( ' 1 | сортировка файлов по папкам' )
print( ' 2 | просмотр конфигурации типов' )
print( '-----------------------------------------------------------' )


task = int( input( ' ' ) )


if not ((task == 1) or (task == 2)):
	print( '-----------------------------------------------------------' )
	print( ' Ошибка: нет такой задачи, вы вероятно ошиблись, бывает' )
	print( ' Совет:  перезапустите программу и попробуйте снова' )
	print( '-----------------------------------------------------------' )
	exit()


if task == 1:
	print( '-----------------------------------------------------------' )
	print( ' Перед началом работы давайте всё настроим как вам нужно' )
	print( '-----------------------------------------------------------' )
	print( ' Выберите режим сортировки:' )
	print( '-----------------------------------------------------------' )
	print( ' 1 | по типу' )
	print( ' 2 | по расширению' )
	print( '-----------------------------------------------------------' )
	
	regime = int( input( ' ' ) )
	
	if not ((regime == 1) or (regime == 2)):
		print( '-----------------------------------------------------------' )
		print( ' Ошибка: нет такого режима, вы вероятно ошиблись, бывает' )
		print( ' Совет:  перезапустите программу и попробуйте снова' )
		print( '-----------------------------------------------------------' )
		exit()
	
	print( '-----------------------------------------------------------' )
	print( ' Введите путь к папке в таком формате:' )
	print( ' C:/example/path/to/files/' )
	print( '-----------------------------------------------------------' )
	
	folder = str( input( ' ' ) )
	
	print( '-----------------------------------------------------------' )
	print( ' Настройки сохранены, всё уже работает' )
	print( ' Для выхода введите что угодно или закройте консоль' )
	print( '-----------------------------------------------------------' )
	print( ' Ход работы:' )
	

	class Handler( FileSystemEventHandler ):
		
		def on_modified( self, event ):
			global count
			count = 0
			
			for filename in os.listdir( folder ):
				extension = filename.split( "." )
				
				if len( extension ) > 1:
					if regime == 1:
						count += 1
						
						for i in range( 0, len( conf_ext ) ):
							if extension[ -1 ].lower() in conf_ext[ i ][ 1 ]:
								print( ' ' + str( count ) + ' | ' + conf_ext[ i ][ 0 ][ 0 ] + ' | ' + filename )
								
								try:
									os.chdir( folder + conf_ext[ i ][ 0 ][ 0 ] + '/' )
								except:
									try:
										os.makedirs( folder + conf_ext[ i ][ 0 ][ 0 ] + '/' )
									except:
										pass
								
								file = folder + filename
								file_new = folder + conf_ext[ i ][ 0 ][ 0 ] + '/' + filename
								try:
									os.rename( file, file_new )
								except:
									file_new = folder + conf_ext[ i ][ 0 ][ 0 ] + '/' + str( count ) + filename
									try:
										os.rename( file, file_new )
									except:
										pass
					
					if regime == 2:
						count += 1
						print( ' ' + str( count ) + ' | ' + extension[ -1 ].lower() + ' | ' + filename )
						
						try:
							os.chdir( folder + extension[ -1 ].lower() + '/' )
						except:
							try:
								os.makedirs( folder + extension[ -1 ].lower() + '/' )
							except:
								pass
						
						file = folder + filename
						file_new = folder + extension[ -1 ].lower() + '/' + filename
						try:
							os.rename( file, file_new )
						except:
							file_new = folder + extension[ -1 ].lower() + '/' + str( count ) + filename
							try:
								os.rename( file, file_new )
							except:
								pass
	
	
	handle = Handler()
	observer = Observer()
	observer.schedule( handle, folder, recursive = False )
	observer.start()
	
	if input():
		observer.stop()
	
	observer.join()


if task == 2:
	print( '-----------------------------------------------------------' )
	print( ' Запускаю вывод всех соотношений типов и расширений...' )
	print( '-----------------------------------------------------------' )
	
	conf_ext.sort()
	
	for i in range(0, len(conf_ext)):
		print( f' тип {conf_ext[i][0][0]}:' )
		conf_ext[i][1].sort()
		
		for j in range(0, len(conf_ext[i][1])):
			print( f'     - {conf_ext[i][1][j]}' )
		
		print('')

# M:/FilesDump/
