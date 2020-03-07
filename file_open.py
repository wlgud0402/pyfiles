#파일처리
#파일열기 open() 열면 닫아주는게 좋음 파일객체.close()

#사용법
#파일객체 = open(문자열:파일경로, 문자열:읽기모드)

#모드의 종류:
# w(write모드:새로씀) 
# a(append모드: 뒤에 이어서 씀)
# r(read모드:읽기모드)

file = open("file_open_made.txt", "w")

file.write("HELLO WORLD")

file.close()
