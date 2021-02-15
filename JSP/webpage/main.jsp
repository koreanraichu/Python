<%@ page import="java.sql.DriverManager"%>

<%@ page language="java" contentType="text/html; charset=UTF-8"

    pageEncoding="UTF-8"%>
       <%@ page import="javax.naming.*" %>
   <%@ page import="java.sql.*" %>
   <%@ page import="javax.sql.*" %>
   <%@ page import="java.text.SimpleDateFormat,java.util.Date"%>
   <%@ page import = "java.util.Calendar" %>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<link rel="stylesheet" type="text/css" href="style.css">
<meta http-equiv="Content-Type" content="text/html; charset=EUC-KR">
<title>부추곱창이먹고싶섬 섬페이지</title>
</head>
<body>
<div class="link">
<jsp:include page="link.jsp"/>
</div>
<div class="banner">
<p>부추곱창이먹고싶섬 섬페이지에 오신 여러분을 환영합니다! </p>
<jsp:include page="banner.jsp"/>
</div>
<div class="news">
<span>Lorem ipsum dolor sit amet</span>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Diam donec adipiscing tristique risus nec feugiat in fermentum. Elit sed vulputate mi sit amet mauris. Odio facilisis mauris sit amet massa vitae tortor.</p>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Tincidunt ornare massa eget egestas. Risus nullam eget felis eget. Viverra orci sagittis eu volutpat odio. <a href="">...More</a></p>
</div>
<div class="news">
<span>pulvinar etiam non quam</span>
<p>Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Diam donec adipiscing tristique risus nec feugiat in fermentum. Elit sed vulputate mi sit amet mauris. Odio facilisis mauris sit amet massa vitae tortor.<a href="">...More</a></p>
</div>
<div class="footer">
<jsp:include page="footer.jsp"/>
</div>
</body>
</html>