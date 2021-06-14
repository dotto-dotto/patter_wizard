from download import download
import os

dir = r'C:\instaladores'

office = r'D:\office\OFFICE-2013\setup.exe'
crack = r'D:\crack\re-loader_by_r@in\Re-LoaderByR@1n'

os.mkdir(dir)

url_java = 'https://javadl.oracle.com/webapps/download/AutoDL?BundleId=244554_d7fc238d0cbf4b0dac67be84580cfb4b' 
file_path_java = r'C:\instaladores\java.exe'

url_winrar = 'https://www.win-rar.com/fileadmin/winrar-versions/winrar/winrar-x64-601.exe'
file_path_winrar = r'C:\instaladores\winrar.exe'

url_anydesk = 'https://download.anydesk.com/AnyDesk.exe?_ga=2.45708196.1693756804.1623423712-927459799.1623423712'
file_path_anydesk = r'C:\instaladores\anydesk.exe'

url_chrome = 'https://dl.google.com/tag/s/appguid%3D%7B8A69D345-D564-463C-AFF1-A69D9E530F96%7D%26iid%3D%7B3CCDFA4A-E5E3-6C64-01A4-360ED983EF11%7D%26lang%3Dpt-BR%26browser%3D3%26usagestats%3D1%26appname%3DGoogle%2520Chrome%26needsadmin%3Dprefers%26ap%3Dx64-stable-statsdef_1%26installdataindex%3Dempty/update2/installers/ChromeSetup.exe'
file_path_chrome = r'C:\instaladores\chrome.exe'

url_acrobat = 'https://admdownload.adobe.com/bin/live/readerdc_br_xa_crd_install.exe'
file_path_acrobat = r'C:\instaladores\acrobat-reader.exe'

url_teamviewer = 'https://customdesign.teamviewer.com/download/version_15x/tqgwqfz_windows/TeamViewer_Host_Setup.exe'
file_path_teamviewer = r'C:\instaladores\teamviewer.exe'

path = { download(url_java, file_path_java, progressbar=True, kind="file", replace=True),
	download(url_winrar, file_path_winrar, progressbar=True, kind="file", replace=True),
	download(url_anydesk, file_path_anydesk, progressbar=True, kind="file", replace=True),
	download(url_chrome, file_path_chrome, progressbar=True, kind="file", replace=True),
	download(url_acrobat, file_path_acrobat, progressbar=True, kind="file", replace=True),
	download(url_teamviewer, file_path_teamviewer, progressbar=True, kind="file", replace=True)
}

os.system(file_path_winrar)
os.system(file_path_java)
os.system(file_path_chrome)
os.system(file_path_acrobat)
os.system(file_path_teamviewer)
os.system(office)
os.system(crack)
