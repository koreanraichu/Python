<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
int elephant = 1;
while (elephant < 10){
%>
<%=elephant %>마리 코끼리가 거미줄에 걸렸네 신나게 그네를 탔다네 너무너무 재밌어 좋아좋아 랄랄라 다른 친구 코끼리를 불렀네 <br>
<%
elephant=elephant+1;
}
%>
<%=elephant %>마리 코끼리가 거미줄에 걸렸네 신나게 그네를 탔다네 너무많은 코끼리가 올라탔네 랄랄라 그만그만 뚝하고 끊어졌대요
</body>
</html>
