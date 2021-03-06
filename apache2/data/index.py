#!/home/woongsup/anaconda3/bin/python
import sys
import io
import cgi
import urllib.request
import urllib.parse
from bs4 import BeautifulSoup

sys.stdout = io.TextIOWrapper(sys.stdout.detach(), encoding='utf-8')
sys.stderr = io.TextIOWrapper(sys.stderr.detach(), encoding='utf-8')
print("content-type: text/html; charset=utf-8\n")

import json

parsed_data = ""
save_dir = ""
crawler_name = ""
var_name = ""


def crawling():
    url = 'https://www.medifonews.com/news/article_list_all.html?sec_no=0'
    html = urllib.request.urlopen(url).read()
    soup = BeautifulSoup(html, 'html.parser')
    title = soup.select('ul.art_list_all > li')

    parsed_data = [{"href": i.a['href'], "text": i.h2.text} for i in title]
    parsed_data = parsed_data[0:6]
    save_dir = './crawlingData.js'
    crawler_name = "crawling.py"
    var_name = "NewsData"
    return parsed_data, save_dir, crawler_name, var_name


def write_data(parsed_data, save_dir, crawler_name, var_name):
    with open(save_dir, "w", encoding="utf-8") as make_file:
        json.dump(parsed_data, make_file, ensure_ascii=False, indent=2)

    data = ""
    with open(save_dir, "r", encoding="UTF-8-sig") as f:
        line = f.readline()
        while line:
            data += line
            line = f.readline()

    final_data = f"//Auto-generated by {crawler_name}\nvar {var_name} = {data};"

    with open(save_dir, "w", encoding="UTF-8-sig") as f_write:
        f_write.write(final_data)


parsed_data, save_dir, crawler_name, var_name = crawling()
write_data(parsed_data, save_dir, crawler_name, var_name)
# form = cgi.FieldStorage()
# if 'id' in form:
# 	pageId = form["id"].value
# 	description = open('data/' + pageId, 'r').read() #data/html
# else:
# 	pageId = 'Welcome'
# description = 'Hello, web'

print('''
<!DOCTYPE html>
<html lang="en">

<head>

  <meta charset="utf-8">
  <meta http-equiv="X-UA-Compatible" content="IE=edge">
  <meta name="viewport" content="width=device-width, initial-scale=1, shrink-to-fit=no">
  <meta name="description" content="">
  <meta name="author" content="">

  <title>어의가 없네</title>

  <!-- Custom fonts for this template-->
  <link href="vendor/fontawesome-free/css/all.min.css" rel="stylesheet" type="text/css">
  <link href="https://fonts.googleapis.com/css?family=Nunito:200,200i,300,300i,400,400i,600,600i,700,700i,800,800i,900,900i" rel="stylesheet">

  <!-- Custom styles for this template-->
  <link href="css/sb-admin-2.min.css" rel="stylesheet">
  <link rel="stylesheet" href="https://stackpath.bootstrapcdn.com/bootstrap/4.5.2/css/bootstrap.min.css" integrity="sha384-JcKb8q3iqJ61gNV9KGb8thSsNjpSL0n8PARn9HuZOnIxN0hoP+VmmDGMN5t9UJ0Z" crossorigin="anonymous">
  <style>
	   #symptoms_input {
	  	 padding-bottom: 110px;
	  	 width: 601.979166px;
	  }

	  #symptoms_input2 {
	  	margin-left: 20px; 
	  	 width: 631.979166px;
	  }

	  #sidebox { 
	  	margin-left: -200px; 
	  	width: 631.979166px;
	  }

  </style>
</head>

<body id="page-top">

  <!-- Page Wrapper -->
  <div id="wrapper">

    <!-- Sidebar -->
    <ul class="navbar-nav bg-gradient-primary sidebar sidebar-dark accordion" id="accordionSidebar">

      <!-- Sidebar - Brand -->
      <a class="sidebar-brand d-flex align-items-center justify-content-center" href="index.py">
        <div class="sidebar-brand-icon rotate-n-15">
          <i class="fas fa-laugh-wink"></i>
        </div>
        <div class="sidebar-brand-text mx-3">어의가 없네</div>
      </a>

      <!-- Divider -->
      <hr class="sidebar-divider my-0">

      <!-- Heading -->
      <div class="sidebar-heading">
        Symptoms
      </div>

      <!-- Nav Item - Dashboard -->
      <li class="nav-item active">
        <a class="nav-link" href="index.py">
          <i class="fas fa-fw fa-tachometer-alt"></i>
          <span>증상 입력</span></a>
      </li>

      <!-- Nav Item - Charts -->
      <li class="nav-item">
        <a class="nav-link" href="chart.py">
          <i class="fas fa-fw fa-chart-area"></i>
          <span>증상 예측</span></a>
      </li>

      <!-- Nav Item - Pages Collapse Menu -->
      <li class="nav-item">
        <a class="nav-link collapsed" href="banner.py">
          <i class="fas fa-fw fa-cog"></i>
          <span>증상 세부 설명</span></a>
      </li>

      <!-- Divider -->
      <hr class="sidebar-divider">

      <!-- Heading -->
      <div class="sidebar-heading">
        Data analysis
      </div>


      <li class="nav-item">
        <a class="nav-link collapsed" href="usage.py">
          <i class="fas fa-fw fa-cog"></i>
          <span>사용자 이용 현황</span></a>
      </li>

      <li class="nav-item">
        <a class="nav-link collapsed" href="visual.py">
          <i class="fas fa-fw fa-cog"></i>
          <span>의료 데이터 시각화</span></a>
      </li>

      <li class="nav-item">
        <a class="nav-link collapsed" href="map.py">
          <i class="fas fa-fw fa-cog"></i>
          <span>근처 병원 안내</span></a>
      </li>

      <!-- Divider -->
      <hr class="sidebar-divider d-none d-md-block">

      <!-- Sidebar Toggler (Sidebar) -->
      <div class="text-center d-none d-md-inline">
        <button class="rounded-circle border-0" id="sidebarToggle"></button>
      </div>

    </ul>
    <!-- End of Sidebar -->

    <!-- Content Wrapper -->
    <div id="content-wrapper" class="d-flex flex-column">

      <!-- Main Content -->
      <div id="content">

        <!-- Begin Page Content -->
        <div class="container-fluid">

          <!-- Page Heading -->
          <div class="d-sm-flex align-items-center justify-content-between mb-4">
            <h1 class="h3 mb-0 text-gray-800">  </h1>

          </div>



          <!-- Content Row -->

          <div class="row">

            <!-- Area Chart -->
            <div class="col-xl-8 col-lg-7">
              <div class="card shadow mb-4" id="symptoms_input2">
                <!-- Card Header - Dropdown -->
                <div class="card-header py-3 d-flex flex-row align-items-center justify-content-between">
                  <h6 class="m-0 font-weight-bold text-primary">다음 항목을 모두 입력해주세요</h6>

                </div>
                <!-- Card Body -->
                <div class="card-body" id="symptoms_input">
                  <div class="chart-area">

                        <form action="chart.py" method="post">
                        
                        	


                        	<div class="form-group">
                              <label for="exampleFormControlSelect1"><br>연령대를 선택해주세요</label>
                              <select class="form-control" id="exampleFormControlSelect1">
                                <option>10세미만</option>
                                <option>10세 이상 ~20세 미만</option>
                                <option>20세 이상 ~30세 미만</option>
                                <option>30세 이상 ~40세 미만</option>
                                <option>40세 이상 ~50세 미만</option>
                                <option>50세 이상 ~60세 미만</option>
                                <option>60세 이상</option>
                              </select>
                            </div>

                     		    <div class="form-group">
                     			    <label for="exampleFormControlSelect2">진료과를 선택해주세요</label>
                              	<select class="form-control" name="department" id="exampleFormControlSelect2">
                                <option value="없음">없음</option>
                                <option value="내과">내과</option>
                                <option value="피부과">피부과</option>
                                <option value="외과">외과</option>
                                <option value="신경과">신경과</option>
                                <option value="안과">안과</option>
                                <option value="이비인후과">이비인후과</option>
                                <option value="신경과">신경과</option>
                                <option value="가정의학과">가정의학과</option>
                              </select>
                              <br>
             				          <label for="exampleFormControlTextarea1">증상을 자세히 입력해주세요</label>
                              <textarea class="form-control" name="symptoms" id="exampleFormControlTextarea1" rows="4"></textarea>
                            </div>

                     		  <input class="btn btn-primary" type="submit" id="submit_button">
                        </form>
                  </div>
                </div>

            </div>

          </div>

          <!-- Content Row -->
          <div class="row">
          	  <!-- Illustrations -->
              <div class="card shadow mb-4" id='sidebox'>
                <div class="card-header py-3" >
                  <h6 class="m-0 font-weight-bold text-primary">실시간 의료 관련 기사</h6>
                </div>
                <div class="card-body" id="koreaNewsDiv">       

                </div>

                 <div style="text-align:center">
                    <span style="color:red">출처</span>
                    <span>
                      <a href="http://medifonews.com/news/article_list_all.html">메디포 뉴스
                        </a>
                    </span>
                 </div>

              </div>     
            </div>

          </div>

        </div>
        <!-- /.container-fluid -->

      </div>
      <!-- End of Main Content -->

      <!-- Footer -->
      <footer class="sticky-footer bg-white">
        <div class="container my-auto">
          <div class="copyright text-center my-auto">
            <span>(법적 한계에 대한 고지) </span>
            <br><br>
            <span>본 정보는 건강정보에 대한 소비자의 이해를 돕기 위한 참고자료일 뿐이며 <br> 개별 환자의 증상과 질병에 대한 정확한 판단을 위해서는 의사의 진료가 반드시 필요합니다.</span>
          </div>
        </div>
      </footer>
      <!-- End of Footer -->

    </div>
    <!-- End of Content Wrapper -->

  </div>
  <!-- End of Page Wrapper -->

  <!-- Scroll to Top Button-->
  <a class="scroll-to-top rounded" href="#page-top">
    <i class="fas fa-angle-up"></i>
  </a>

  <!-- Logout Modal-->
  <div class="modal fade" id="logoutModal" tabindex="-1" role="dialog" aria-labelledby="exampleModalLabel" aria-hidden="true">
    <div class="modal-dialog" role="document">
      <div class="modal-content">
        <div class="modal-header">
          <h5 class="modal-title" id="exampleModalLabel">Ready to Leave?</h5>
          <button class="close" type="button" data-dismiss="modal" aria-label="Close">
            <span aria-hidden="true">×</span>
          </button>
        </div>
        <div class="modal-body">Select "Logout" below if you are ready to end your current session.</div>
        <div class="modal-footer">
          <button class="btn btn-secondary" type="button" data-dismiss="modal">Cancel</button>
          <a class="btn btn-primary" href="login.html">Logout</a>
        </div>
      </div>
    </div>
  </div>

  <!-- Bootstrap core JavaScript-->
  <script src="vendor/jquery/jquery.min.js"></script>
  <script src="vendor/bootstrap/js/bootstrap.bundle.min.js"></script>

  <!-- Core plugin JavaScript-->
  <script src="vendor/jquery-easing/jquery.easing.min.js"></script>

  <!-- Custom scripts for all pages-->
  <script src="js/sb-admin-2.min.js"></script>

  <!-- Page level plugins -->
  <script src="vendor/chart.js/Chart.min.js"></script>

  <!-- Page level custom scripts -->
  <script src="js/demo/chart-area-demo.js"></script>
  <script src="js/demo/chart-pie-demo.js"></script>
  <script src="./crawlingData.js"></script>
  <script>

		  	function createNews(newsData, newsDiv, sliceValue) {
		      newsData.forEach(news => {
		        // console.log(news["title"]);
		        // console.log(news["title"].substring( 0, sliceValue ) + "...");
		        var cardElement = document.createElement("div");
		        cardElement.setAttribute("class", "card");

		        var cardHeader = document.createElement("div");
		        cardHeader.setAttribute("class", "card-header");

		        var text = document.createElement("h2");
		        text.setAttribute("class", "mb-0 cases-title");

		        var link = document.createElement("a");
		        link.setAttribute("href", 'http://medifonews.com/' + news["href"]);
		        link.setAttribute("target", "_blank");
		        link.setAttribute("rel", "noopener noreferrer");

		        var button = document.createElement("button");
		        button.setAttribute("class", "btn btn-link");
		        button.setAttribute("type", "button");

		        if (window.innerWidth > 500) {
		          var title = document.createTextNode(news["text"]);
		        } else {
		          var title = document.createTextNode(news["text"].substring(0, sliceValue) + "...");
		        }

		        button.appendChild(title);
		        link.appendChild(button);
		        text.appendChild(link);
		        cardHeader.appendChild(text);
		        cardElement.appendChild(cardHeader);
		        newsDiv.appendChild(cardElement);
		      });
		    };

		    var koreaNewsDiv = document.getElementById("koreaNewsDiv");

		    createNews(NewsData, koreaNewsDiv, 19)

  </script>

</body>

</html>

'''
      )
