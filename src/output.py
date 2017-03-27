def generate_head(title, index):
    output_html = ""
    output_html += "<!DOCTYPE html>\n"
    output_html += "<html lang=\"en\">\n"
    output_html += "<head>\n"
    output_html += "<meta charset=\"UTF-8\">\n"
    output_html += "<title>" + title + "</title>\n"
    output_html += "<meta charset=\"utf-8\">\n"
    output_html += "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"

    output_html += "<link rel=\"stylesheet\" href=\"https://maxcdn.bootstrapcdn.com/bootstrap/3.3.7/css/bootstrap.min.css\">\n"
    output_html += "<script src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js\"></script>"
    output_html += "<link rel=\"stylesheet\" href=\"https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css\">\n"

    output_html += "</head>\n"
    output_html += "<style>\n"
    output_html += "    body{\n"
    output_html += "        font: 400 15px Lato, sans-serif;\n"
    output_html += "        background-color: #ddd;\n"
    output_html += "    }\n"
    output_html += "    .table>thead>tr>th {\n"
    output_html += "    border-bottom: none;\n"
    output_html += "}\n"

    output_html += "    .footer{\n"
    output_html += "        padding-top: 200px;\n"
    output_html += "        padding-bottom: 50px;\n"
    output_html += "    }\n"

    output_html += "    .table>tbody>tr>td {\n"
    output_html += "    padding: 8px;\n"
    output_html += "    line-height: 1.42857143;\n"
    output_html += "    vertical-align: top;\n"
    output_html += "    border-top: none;\n"
    output_html += "}\n"

    output_html += "    .panel{\n"
    output_html += "        padding: 20px;\n"
    output_html += "        color: white;\n"
    output_html += "        font-size: 24px;\n"

    output_html += "    }\n"
    output_html += "     .navbar {\n"
    output_html += "      margin-bottom: 0;\n"
    output_html += "      background-color: #2a313d;\n"
    output_html += "      z-index: 9999;\n"
    output_html += "      border: 0;\n"
    output_html += "      font-size: 12px !important;\n"
    output_html += "      line-height: 1.42857143 !important;\n"
    output_html += "      letter-spacing: 4px;\n"
    output_html += "      border-radius: 0;\n"
    output_html += "      font-family: Montserrat, sans-serif;\n"
    output_html += "  }\n"

    output_html += "     h2 {\n"
    output_html += "      font-size: 24px;\n"

    output_html += "      font-weight: 600;\n"
    output_html += "      margin-bottom: 30px;\n"
    output_html += "  }\n"

    output_html += "     h1{\n"
    output_html += "         margin-bottom: 30px;\n"
    output_html += "     }\n"
    output_html += "     .jumbotron {\n"

    output_html += "      background-color: #2a313d;\n"
    output_html += "      color: #fff;\n"
    output_html += "      padding: 100px 25px;\n"
    output_html += "      font-family: Montserrat, sans-serif;\n"
    output_html += "  }\n"
    output_html += "  .navbar li a, .navbar .navbar-brand {\n"
    output_html += "      color: #fff !important;\n"
    output_html += "  }\n"
    output_html += "  .navbar-nav li a:hover, .navbar-nav li.active a {\n"
    output_html += "      color: #8fcaeb !important;\n"
    output_html += "      border-bottom: 1px solid;\n"
    output_html += "  }\n"
    output_html += "  .navbar-default .navbar-toggle {\n"
    output_html += "      border-color: transparent;\n"
    output_html += "      color: #fff !important;\n"
    output_html += "  }\n"
    if index:
        output_html += "    .container-fluid{\n"
        output_html += "        margin-left: 25%;\n"
        output_html += "        margin-right: 25%;\n"
        output_html += "        padding: 60px 50px;\n"
        output_html += "    }\n"
    else:
        output_html += "    .container-fluid{\n"
        output_html += "        margin-left: 5%;\n"
        output_html += "        margin-right: 5%;\n"
        output_html += "        padding: 60px 50px;\n"
        output_html += "    }\n"
    output_html += "    .stat{\n"
    output_html += "        font-size: 32px;\n"
    output_html += "    }\n"
    output_html += "    .bgtan{\n"
    output_html += "        background-color: tan;\n"
    output_html += "        border-color: tan;\n"
    output_html += "    }\n"

    output_html += "    .bgteal{\n"
    output_html += "        background-color: teal;\n"
    output_html += "        border-color: teal;\n"
    output_html += "    }\n"

    output_html += "    .bgbrown{\n"
    output_html += "        background-color: #b67335;\n"
    output_html += "        border-color: #b67335;\n"
    output_html += "    }\n"

    output_html += "    .bglightteal{\n"
    output_html += "        background-color: #66b9bf;\n"
    output_html += "        border-color: #66b9bf;\n"
    output_html += "    }\n"

    output_html += "    .bgdark{\n"
    output_html += "        background-color: darkslategrey;\n"
    output_html += "        border-color: darkslategray;\n"
    output_html += "    }\n"

    output_html += "    .bgdarkbrown{\n"
    output_html += "        background-color: saddlebrown;\n"
    output_html += "        border-color: saddlebrown;\n"
    output_html += "    }\n"

    output_html += "    .header{\n"
    output_html += "        color: white;\n"
    output_html += "        border-radius: 8px 8px 0px 0px;\n"
    output_html += "        border-bottom:none;\n"
    output_html += "        padding: 2px;\n"
    output_html += "        text-align: center;\n"
    output_html += "    }\n"

    output_html += "    table {\n"
    output_html += "    display: table;\n"
    output_html += "    border-collapse: separate;\n"
    output_html += "    border-spacing: 2px;\n"

    output_html += "}\n"

    output_html += "    table {\n"
    output_html += "        white-space: normal;\n"
    output_html += "        line-height: normal;\n"
    output_html += "        font-weight: normal;\n"
    output_html += "        font-style: normal;\n"
    output_html += "        text-align: center;\n"
    output_html += "        font-size: 18px;\n"
    output_html += "    }\n"

    output_html += "</style>"

    return output_html


def generate_branch_history(path, branch_history, type):
    for key, value in branch_history.iteritems():
        output_html = generate_head(key, False)

        output_html += "<body id=\"myPage\" data-spy=\"scroll\" data-target=\".navbar\" data-offset=\"60\">\n"
        output_html += "<div id=\"general\" class=\"container-fluid cont2\" align=\"middle\">\n"
        output_html += "    <div class=\"row \">\n"
        output_html += "        <h2><a href=\"index.html#branches\"><i class=\"fa fa-arrow-circle-left\" aria-hidden=\"true\"> Go Back</i></a></h2>"
        output_html += "    </div>"
        output_html += "    <div class=\"row \">\n"
        output_html += "        <h1>" + key.strip('* \n').split("/")[-1] + "</h1>\n"
        output_html += "    </div\n>"
        output_html += "    <div class=\"row\">\n"
        output_html += "         <table class=\"table table-striped\">\n"
        output_html += "    <thead >\n"
        output_html += "      <tr>\n"
        output_html += "        <th class=\"header bgbrown\" >Commit id</th>\n"
        output_html += "        <th class=\"header bgbrown\" >Commit message</th>\n"
        output_html += "        <th class=\"header bgbrown\" >Date</th>\n"
        output_html += "        <th class=\"header bgbrown\" >Author</th>\n"
        output_html += "      </tr>\n"
        output_html += "    </thead>\n"
        output_html += " <tbody>\n"
        for j in range(0, len(value)):
            output_html += "<tr>\n"
            output_html += "<td>" + value[j]["id"] + "</td>\n"
            output_html += "<td>" + value[j]["message"] + "</td>\n"
            output_html += "<td>" + value[j]["date"] + "</td>\n"
            output_html += "<td>" + value[j]["author"] + "</td>\n"
            output_html += "</tr>\n"
        output_html += "</tbody>\n</table>\n</div>\n"

        output_html += "</body>\n"
        output_html += "</html>\n"

        f = open(path + "/" + key.strip('* \n').split("/")[-1] + "_" + type + ".html", 'w')
        f.write(output_html)
        f.close()


def generate_output(statistics, path):
    output_html = generate_head("Git Statistics", True)
    output_html += "<body id=\"myPage\" data-spy=\"scroll\" data-target=\".navbar\" data-offset=\"60\">\n"
    output_html += "<nav class=\"navbar navbar-default navbar-fixed-top\">\n"
    output_html += "  <div class=\"container\">\n"
    output_html += "    <div class=\"navbar-header\">\n"
    output_html += "      <button type=\"button\" class=\"navbar-toggle\" data-toggle=\"collapse\" data-target=\"#myNavbar\">\n"
    output_html += "        <span class=\"icon-bar\"></span>\n"
    output_html += "        <span class=\"icon-bar\"></span>\n"
    output_html += "        <span class=\"icon-bar\"></span>\n"
    output_html += "      </button>\n"
    output_html += "      <a class=\"navbar-brand\" href=\"#myPage\">Home</a>\n"
    output_html += "    </div>\n"
    output_html += "    <div class=\"collapse navbar-collapse\" id=\"myNavbar\">\n"
    output_html += "      <ul class=\"nav navbar-nav navbar-right\">\n"
    output_html += "        <li><a href=\"#general\">GENERAL</a></li>\n"
    output_html += "        <li><a href=\"#stats\">STATISTICS</a></li>\n"
    output_html += "          <li><a href=\"#branches\">BRANCHES</a></li>\n"

    output_html += "      </ul>\n"
    output_html += "    </div>\n"
    output_html += "  </div>\n"
    output_html += "</nav>\n"
    output_html += "<div class=\"jumbotron text-center\">\n"
    output_html += "  <h1>Git Repository Report</h1>\n"
    output_html += "<p>for\n"
    output_html += "    <h2>" + statistics["gitname"].rsplit('/', 1)[-1] + "</h2>\n"

    output_html += "</p>\n"
    output_html += "</div>\n"
    output_html += "<div id=\"general\" class=\"container-fluid slideanim\" align=\"middle\">\n"
    output_html += "    <h1>General</h1>\n"
    output_html += "    <div class=\"row \">\n"
    output_html += "        <div class=\"col-md-6\">\n"
    output_html += "            <div id=\"p1\" class=\"panel panel-default bgdark\"><div class=\"stat\">" + str(statistics[
        "file_count"]) + "</div> Files</div>\n"
    output_html += "        </div>\n"
    output_html += "         <div class=\"col-md-6\">\n"
    output_html += "             <div  id=\"p2\" class=\"panel panel-default bgteal\"><div class=\"stat\">" + \
                   str(statistics["line_count_total"]) + "</div> Lines </div>\n"
    output_html += "        </div>\n"

    output_html += "    </div>\n"
    output_html += "    <div class=\"row \">\n"
    output_html += "        <div class=\"col-md-6\">"
    output_html += "            <div  id=\"p4\" class=\"panel panel-default bgdarkbrown\"><div class=\"stat\">" + \
                   str(statistics["com_stats"]["commits"]) + "</div> Commits</div>\n"
    output_html += "        </div>\n"
    output_html += "        <div class=\"col-md-6\">\n"
    output_html += "             <div id=\"p3\" class=\"panel panel-default bg bglightteal\"><div class=\"stat\">" + \
                   str(statistics["com_stats"]["committers"]) + "</div> Committers </div>\n"
    output_html += "        </div>\n"

    output_html += "    </div>\n"
    output_html += "    <div class=\"row\">\n"
    output_html += "        <div class=\"col-md-4\">\n"
    output_html += "             <div  id=\"p5\" class=\"panel panel-default bgbrown\"><div class=\"stat\">" + \
                   str(statistics["br_stats"]["tags"]) + " </div> Tags </div>\n"
    output_html += "        </div>\n"
    output_html += "         <div class=\"col-md-4\">"
    output_html += "             <div  id=\"p6\" class=\"panel panel-default bgtan\"><div class=\"stat\">" + \
                   str(statistics["br_stats"]["localCount"]) + "</div> Local Branches </div>\n"
    output_html += "        </div>\n"
    output_html += "        <div class=\"col-md-4\">\n"
    output_html += "             <div   class=\"panel panel-default bgtan\"><div class=\"stat\">" + \
                   str(statistics["br_stats"]["remoteCount"]) + "</div> Remote Branches </div>\n"
    output_html += "        </div>\n"
    output_html += "    </div>\n"
    output_html += "</div>\n"
    output_html += "<div id=\"stats\" class=\"container-fluid slideanim\" align=\"middle\">\n"
    output_html += "    <div class=\"row \">\n"
    output_html += "        <h1>Statistics</h1>\n"
    output_html += "    </div>\n"
    output_html += "    <div class=\"row \">\n"
    output_html += "        <h2>Percentage of commits per author</h2>\n"
    output_html += "    </div>\n"
    output_html += "    <div class=\"row\">\n"
    output_html += "         <table class=\"table table-striped\">\n"
    output_html += "    <thead >\n"
    output_html += "      <tr>\n"
    output_html += "        <th class=\"header bgdarkbrown\" >Author</th>\n"
    output_html += "        <th class=\"header bgdarkbrown\" >% of commits</th>\n"
    output_html += "      </tr>\n"
    output_html += "    </thead>\n"
    output_html += " <tbody>\n"

    com_auth = statistics["com_stats"]["com_per_author"]
    for key, value in com_auth.iteritems():
        output_html += "<tr>\n"
        output_html += "<td>" + key + "</td>\n"
        output_html += "<td>" + str(value) + "%</td>\n"
        output_html += "</tr>\n"
    output_html += "</tbody>\n</table>\n</div>\n"

    output_html += "    <div class=\"row \">\n"
    output_html += "        <h2>Average commits</h2>\n"
    output_html += "    </div\n>"
    output_html += "    <div class=\"row\">\n"
    output_html += "         <table class=\"table table-striped\">\n"
    output_html += "    <thead >\n"
    output_html += "      <tr>\n"
    output_html += "        <th class=\"header bgbrown\" >Author</th>\n"
    output_html += "        <th class=\"header bgbrown\" >per day</th>\n"
    output_html += "        <th class=\"header bgbrown\" >per week</th>\n"
    output_html += "        <th class=\"header bgbrown\" >per month</th>\n"
    output_html += "      </tr>\n"
    output_html += "    </thead>\n"
    output_html += " <tbody>\n"

    com_rates = statistics["br_stats"]["com_rates"]
    for key, value in com_rates.iteritems():
        output_html += "<tr>\n"
        output_html += "<td>" + key + "</td>\n"
        output_html += "<td>" + str(value[0]) + "</td>\n"
        output_html += "<td>" + str(value[1]) + "</td>\n"
        output_html += "<td>" + str(value[2]) + "</td>\n"
        output_html += "</tr>\n"
    output_html += "</tbody>\n</table>\n</div>\n"

    output_html += "    <div class=\"row \">\n"
    output_html += "        <h2>Number of insertions and deletions per author</h2>\n"
    output_html += "    </div>\n"
    output_html += "    <div class=\"row\">\n"
    output_html += "         <table class=\"table table-striped\">\n"
    output_html += "    <thead >\n"
    output_html += "      <tr>\n"
    output_html += "        <th class=\"header bgtan\" >Author</th>\n"
    output_html += "        <th class=\"header bgtan\" >Insertions</th>\n"
    output_html += "        <th class=\"header bgtan\" >Deletions</th>\n"
    output_html += "      </tr>\n"
    output_html += "    </thead>\n"
    output_html += " <tbody>\n"

    adds = statistics["com_stats"]["adds"]
    dels = statistics["com_stats"]["dels"]
    for key, value in adds.iteritems():
        output_html += "<tr>\n"
        output_html += "<td>" + key.encode('utf-8').strip() + "</td>\n"
        output_html += "<td>" + str(adds[key]/statistics["com_stats"]["commits"]) + " (+)</td>\n"
        output_html += "<td>" + str(dels[key]/statistics["com_stats"]["commits"]) + " (-)</td>\n"
        output_html += "</tr>\n"
    output_html += "</tbody>\n</table>\n</div>\n"

    output_html += "    <div class=\"row \">\n"
    output_html += "        <h2>Number of commits per branch</h2>\n"
    output_html += "    </div>\n"
    output_html += "    <div class=\"row\">\n"
    output_html += "         <table class=\"table table-striped\">\n"
    output_html += "    <thead >\n"
    output_html += "      <tr>\n"
    output_html += "        <th class=\"header bgdark\" >Local Branch</th>\n"
    output_html += "        <th class=\"header bgdark\" >Number of commits</th>\n"
    output_html += "      </tr>\n"
    output_html += "    </thead>\n"
    output_html += " <tbody>\n"

    com_branchR = statistics["br_stats"]["com_branchR"]
    com_branchL = statistics["br_stats"]["com_branchL"]
    for key, value in com_branchL.iteritems():
        output_html += "<tr>\n"
        output_html += "<td>" + key + "</td>\n"
        output_html += "<td>" + str(value) + " (+)</td>\n"
        output_html += "</tr>\n"
    output_html += "</tbody>\n</table>\n</div>\n"

    output_html += "    <div class=\"row\">\n"
    output_html += "         <table class=\"table table-striped\">\n"
    output_html += "    <thead >\n"
    output_html += "      <tr>\n"
    output_html += "        <th class=\"header bgteal\" >Remote Branch</th>\n"
    output_html += "        <th class=\"header bgteal\" >Number of commits</th>\n"
    output_html += "      </tr>\n"
    output_html += "    </thead>\n"
    output_html += " <tbody>\n"

    for key, value in com_branchR.iteritems():
        output_html += "<tr>\n"
        output_html += "<td>" + key + "</td>\n"
        output_html += "<td>" + str(value) + "</td>\n"
        output_html += "</tr>\n"
    output_html += "</tbody>\n</table>\n</div>\n"

    output_html += "    <div class=\"row \">\n"
    output_html += "        <h2>Percentage of commits per author per branch</h2>\n"
    output_html += "    </div>\n"
    output_html += "    <div class=\"row\">\n"
    output_html += "         <table class=\"table table-striped\">\n"
    output_html += "    <thead >\n"
    output_html += "      <tr>\n"
    output_html += "        <th class=\"header bglightteal\" >Remote Branch</th>\n"
    output_html += "        <th class=\"header bglightteal\" >Author</th>\n"
    output_html += "        <th class=\"header bglightteal\" >% of commits</th>\n"
    output_html += "      </tr>\n"
    output_html += "    </thead>\n"
    output_html += " <tbody>\n"

    com_br_authR = statistics["br_stats"]["com_br_authR"]
    for key, value in com_br_authR.iteritems():
        output_html += "<tr>\n"
        output_html += "<td>" + key + "</td>\n"
        output_html += "<td>" + str(value[0]) + "</td>\n"
        output_html += "<td>" + str(value[1]) + "%</td>\n"
        output_html += "</tr>\n"
    output_html += "</tbody>\n</table>\n</div></div>\n"

    output_html += "<div id=\"branches\" class=\"container-fluid slideanim\" align=\"middle\">\n"
    output_html += "    <div class=\"row \">\n"
    output_html += "        <h1>Branches</h1>\n"
    output_html += "         <p>Click on the link of each branch to see its commit history.\n"
    output_html += "    </div>\n"
    output_html += "    <div class=\"row \">\n"
    output_html += "        <h2>Remote Branches</h2>\n"
    output_html += "    </div>\n"
    output_html += "    <div class=\"row\">\n"
    output_html += "         <table class=\"table table-striped\">\n"
    output_html += "    <thead >\n"
    output_html += "      <tr>\n"
    output_html += "        <th class=\"header bglightteal\" >Branch</th>\n"
    output_html += "        <th class=\"header bglightteal\" >Date created</th>\n"
    output_html += "        <th class=\"header bglightteal\" >Date modified</th>\n"
    output_html += "      </tr>\n"
    output_html += "    </thead>\n"
    output_html += " <tbody>\n"

    """
        Remote Branches with dates go here.
    """
    remoteB = statistics["br_stats"]["remoteB"]
    br_stats = statistics["br_stats"]
    for i in range(0, len(remoteB)):
        output_html += "<tr>\n"
        output_html += "<td><a href=\"" + remoteB[i].split("/")[-1] + "_remote.html\">" + remoteB[i] + "</a></td>\n"
        output_html += "<td>" + str(br_stats['branch_dates_remote'][remoteB[i].strip()][0]) + "</td>\n"
        output_html += "<td>" + str(br_stats['branch_dates_remote'][remoteB[i].strip()][1]) + "</td>\n"
        output_html += "</tr>\n"
    output_html += "</tbody></table></div>\n"

    output_html += "    <div class=\"row \">\n"
    output_html += "        <h2>Local Branches</h2>\n"
    output_html += "    </div>\n"
    output_html += "    <div class=\"row\">\n"
    output_html += "         <table class=\"table table-striped\">\n"
    output_html += "    <thead >\n"
    output_html += "      <tr>\n"
    output_html += "        <th class=\"header bglightteal\" >Branch</th>\n"
    output_html += "        <th class=\"header bglightteal\" >Date created</th>\n"
    output_html += "        <th class=\"header bglightteal\" >Date modified</th>\n"
    output_html += "      </tr>\n"
    output_html += "    </thead>\n"
    output_html += " <tbody>\n"

    """
        Local Branches with dates go here.
    """
    localB = statistics["br_stats"]["localB"]
    for i in range(0, len(localB)):
        output_html += "<tr>\n"
        output_html += "<td><a href=\"" + localB[i].strip('* \n').split("/")[-1] + "_local.html\" >" + localB[i] + "</a></td>\n"
        output_html += "<td>" + str(br_stats['branch_dates_local'][localB[i].strip('* \n')][0]) + "</td>\n"
        output_html += "<td>" + str(br_stats['branch_dates_local'][localB[i].strip('* \n')][1]) + "</td>\n"
        output_html += "</tr>\n"

    output_html += "</tbody></table></div></div>\n"

    output_html += "<footer class=\"text-center footer\">\n"
    output_html += "<a href=\"#myPage\" title=\"To Top\"><i class=\"fa fa-arrow-up\" aria-hidden=\"true\" " \
                   "style=\"font-size:40px; color:#2a313d\"></i> \n"
    output_html += "  </a>\n"
    output_html += "</footer>\n"
    output_html += "</div>\n"
    output_html += "<script>\n"
    output_html += "$(document).ready(function(){\n"
    output_html += "  $(\".navbar a, footer a[href='#myPage'], td a\").on('click', function(event) {\n"
    output_html += "    if (this.hash !== \"\") {\n"
    output_html += "      event.preventDefault();\n"
    output_html += "      var hash = this.hash;\n"
    output_html += "      $('html, body').animate({\n"
    output_html += "        scrollTop: $(hash).offset().top\n"
    output_html += "      }, 900, function(){\n"
    output_html += "        window.location.hash = hash;\n"
    output_html += "      });\n"
    output_html += "    }\n"
    output_html += "  })\n;"
    output_html += "})\n"
    output_html += "</script>\n"
    output_html += "</body>\n"
    output_html += "</html>\n"

    f = open(path + "/index.html", 'w')
    f.write(output_html)
    f.close()
    branch_stats_local = statistics["br_stats"]["branch_stats_local"]
    branch_stats_remote = statistics["br_stats"]["branch_stats_remote"]

    generate_branch_history(path, branch_stats_local, "local")
    generate_branch_history(path, branch_stats_remote, "remote")
