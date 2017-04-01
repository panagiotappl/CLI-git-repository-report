import codecs
import os


def generate_template(path):
    output_html = ""
    with codecs.open(path, "r", "utf-8") as myfile:
        output_html = myfile.read()
    return output_html


def generate_branch_history(path, branch_history, type, tags):
    for key, value in branch_history.iteritems():
        output_html = generate_template("./html_templates/html_head.html")

        output_html += "<body id=\"myPage\" data-spy=\"scroll\" data-target=\".navbar\" data-offset=\"60\">\n"
        output_html += "<div id=\"history\" class=\"container-fluid cont2\" align=\"middle\">\n"
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

        if len(tags[key.strip("* \n")]) != 0:
            output_html += "    <div class=\"row\">\n"
            output_html += "         <table class=\"table table-striped\">\n"
            output_html += "    <thead >\n"
            output_html += "      <tr>\n"
            output_html += "        <th class=\"header bgbrown\" >Tags</th>\n"

            output_html += "      </tr>\n"
            output_html += "    </thead>\n"
            output_html += " <tbody>\n"
            for tag in tags[key.strip("* \n")]:
                output_html += "<tr>\n"
                output_html += "<td>" + tag + "</td>\n"

                output_html += "</tr>\n"
                output_html += "</tbody>\n</table>\n</div>\n"
        else:
            output_html += "    <div class=\"row\">\n"
            output_html += "        <h1>No tags available</h1>"
            output_html += "    </div>"

        output_html += generate_template("./html_templates/html_footer.html")
        f = open(path + "/" + key.strip('* \n').split("/")[-1] + "_" + type + ".html", 'w')
        f.write(output_html)
        f.close()


def generate_piecharts(dictionary, pieChart):
    output_html = "<script type=\"text/javascript\" src=\"http://d3js.org/d3.v4.min.js\" charset=\"utf-8\"></script>\n"
    output_html += "<script src=\"https://rawgit.com/benkeen/d3pie/master/d3pie/d3pie.min.js\">   </script>\n"
    output_html += "<script> var pie = {\n"
    output_html += "	\"footer\": {\n"
    output_html += "		\"color\": \"#999999\",\n"
    output_html += "		\"fontSize\": 10,\n"
    output_html += "		\"font\": \"open sans\",\n"
    output_html += "		\"location\": \"bottom-left\"\n"
    output_html += "	},\n"
    output_html += "	\"size\": {\n"
    output_html += "		\"canvasWidth\": 590,\n"
    output_html += "		\"pieOuterRadius\": \"90%\"\n"
    output_html += "	},\n"
    output_html += "	\"data\": {\n"
    output_html += "		\"sortOrder\": \"value-desc\",\n"
    output_html += "		\"content\": [\n"
    for key, value in dictionary.iteritems():
        output_html += "			{"
        output_html += "				\"label\": \"" + key + "\",\n"
        output_html += "				\"value\": " + str(value) + ",\n"
        if dictionary.keys()[-1] == key:
            output_html += "			}\n"
        else:
            output_html += "			},\n"

    output_html += "	]},\n"
    output_html += "	\"labels\": {\n"
    output_html += "		\"outer\": {\n"
    output_html += "			\"pieDistance\": 32\n"
    output_html += "		},\n"
    output_html += "		\"inner\": {\n"
    output_html += "			\"hideWhenLessThanPercentage\": 3\n"
    output_html += "		},\n"
    output_html += "		\"mainLabel\": {\n"
    output_html += "			\"fontSize\": 11\n"
    output_html += "		},\n"
    output_html += "		\"percentage\": {\n"
    output_html += "			\"color\": \"#ffffff\",\n"
    output_html += "			\"decimalPlaces\": 0\n"
    output_html += "		},\n"
    output_html += "		\"value\": {\n"
    output_html += "			\"color\": \"#adadad\",\n"
    output_html += "			\"fontSize\": 11\n"
    output_html += "		},\n"
    output_html += "		\"lines\": {\n"
    output_html += "			\"enabled\": true\n"
    output_html += "		},\n"
    output_html += "		\"truncation\": {\n"
    output_html += "			\"enabled\": true\n"
    output_html += "		}\n"
    output_html += "	},\n"
    output_html += "	\"effects\": {\n"
    output_html += "		\"pullOutSegmentOnClick\": {\n"
    output_html += "			\"effect\": \"linear\",\n"
    output_html += "			\"speed\": 400,\n"
    output_html += "			\"size\": 8\n"
    output_html += "		}\n"
    output_html += "	},\n"
    output_html += "	\"misc\": {\n"
    output_html += "		\"gradient\": {\n"
    output_html += "			\"enabled\": true,\n"
    output_html += "			\"percentage\": 100\n"
    output_html += "		}\n"
    output_html += "	}\n"
    output_html += "};\n"
    output_html += """
                   $(window).scroll(function() {
                       var hT = $('#pieChart').offset().top,
                           hH = $('#pieChart').outerHeight(),
                           wH = $(window).height(),
                           wS = $(this).scrollTop();
                       if (wS > (hT+hH-wH)){
                            new d3pie("pieChart", pie);
                            $(window).off('scroll')
                       }
                    });
                   """
    output_html += "</script>\n"

    return output_html


def generate_barchart(data):
    output = """
                    <!-- Styles -->
                    <style>
                    #chartdiv {
                        width		: 100%;
                        height		: 500px;
                        font-size	: 10px;
                    }
                    </style>

                    <!-- Resources -->
                    <script src="https://www.amcharts.com/lib/3/amcharts.js"></script>
                    <script src="https://www.amcharts.com/lib/3/serial.js"></script>
                    <script src="https://www.amcharts.com/lib/3/plugins/export/export.min.js"></script>
                    <link rel="stylesheet" href="https://www.amcharts.com/lib/3/plugins/export/export.css" type="text/css" media="all" />
                    <script src="https://www.amcharts.com/lib/3/themes/light.js"></script>

                    <!-- Chart code -->
                    <script>
                    AmCharts.lazyLoadMakeChart = AmCharts.makeChart;

                    // override makeChart function
                    AmCharts.makeChart = function(a, b, c) {

                      // set scroll events
                      jQuery(document).on('scroll load touchmove', handleScroll);
                      jQuery(window).on('load', handleScroll);

                      function handleScroll() {
                        var $ = jQuery;
                        if (true === b.lazyLoaded)
                          return;
                        var hT = $('#' + a).offset().top,
                          hH = $('#' + a).outerHeight() / 2,
                          wH = $(window).height(),
                          wS = $(window).scrollTop();
                        if (wS > (hT + hH - wH)) {
                          b.lazyLoaded = true;
                          AmCharts.lazyLoadMakeChart(a, b, c);
                          return;
                        }
                      }

                      // Return fake listener to avoid errors
                      return {
                        addListener: function() {}
                      };
                    };

                    var chart = AmCharts.makeChart( "chartdiv", {
                      "type": "serial",
                      "theme": "light",
                      "startEffect": "easeOutSine",
                      "dataProvider":
                      """

    pers = []
    for key, value in data.iteritems():
        pers.append({
            'branch': key,
            'per': value
        })
    import json
    output += json.dumps(pers)

    output += """,
                      "valueAxes": [ {
                        "title": "Percentage of all commits",
                        "gridColor": "#FFFFFF",
                        "gridAlpha": 0.2,
                        "dashLength": 0
                      } ],
                      "gridAboveGraphs": true,
                      "startDuration": 1,
                      "graphs": [ {
                        "balloonText": "[[category]]: <b>[[value]]</b>",
                        "fillAlphas": 0.8,
                        "fillColors": "#008080",
                        "lineAlpha": 0.2,
                        "type": "column",
                        "valueField": "per"
                      } ],
                      "chartCursor": {
                        "categoryBalloonEnabled": false,
                        "cursorAlpha": 0,
                        "zoomable": false
                      },
                      "categoryField": "branch",
                      "categoryAxis": {
                        "gridPosition": "start",
                        "gridAlpha": 0,
                        "labelRotation": 45,
                        "tickPosition": "start",
                        "tickLength": 10
                      },
                      "export": {
                        "enabled": true
                      }

                    });

                    </script>
    """
    return output


def generate_output(statistics, path):
    output_html = generate_template("./html_templates/html_head.html")
    output_html += "<body id=\"myPage\" data-spy=\"scroll\" data-target=\".navbar\" data-offset=\"60\">\n"

    output_html += generate_template("./html_templates/html_navbar.html")
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
    output_html += "            <div id=\"p1\" class=\"panel panel-default bgdark\"><div class=\"stat\">" + str(
        statistics[
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
                   str(statistics["com_stats"]["committers"]) + "</div> Authors </div>\n"
    output_html += "        </div>\n"

    output_html += "    </div>\n"
    output_html += "    <div class=\"row\">\n"
    output_html += "        <div class=\"col-md-4\">\n"
    output_html += "             <div  id=\"p5\" class=\"panel panel-default bgbrown\"><div class=\"stat\">" + \
                   str(statistics["br_stats"]["tags"]) + " </div> Tags Count </div>\n"
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
        output_html += "<td>" + key.decode('utf-8') + "</td>\n"
        output_html += "<td>" + str(value) + "%</td>\n"
        output_html += "</tr>\n"
    output_html += "</tbody>\n</table>\n"
    output_html += "<div id=\"pieChart\"></div>"
    output_html += "</div>\n"

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
    output_html += "        <th class=\"header bgtan\" >Changes</th>\n"
    output_html += "      </tr>\n"
    output_html += "    </thead>\n"
    output_html += " <tbody>\n"

    adds = statistics["com_stats"]["adds"]
    dels = statistics["com_stats"]["dels"]
    changes = statistics["com_stats"]["changes"]
    for key, value in adds.iteritems():
        output_html += "<tr>\n"
        output_html += "<td>" + key.decode('utf-8').strip() + "</td>\n"
        output_html += "<td>" + key.encode('utf-8').strip() + "</td>\n"
        output_html += "<td>" + str(adds[key]) + " (+)</td>\n"
        output_html += "<td>" + str(dels[key]) + " (-)</td>\n"
        output_html += "<td>" + str(changes[key]) + " </td>\n"
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
        output_html += "<td>" + str(value) + "</td>\n"
        output_html += "</tr>\n"
    output_html += "</tbody>\n</table>\n</div>\n"

    # Percentage of commits per branch.
    branch_per = statistics["br_stats"]["branchCommits"]

    output_html += "    <div class=\"row \">\n"
    output_html += "        <h2>Percentage of commits per branch</h2>\n"
    output_html += "    </div>\n"
    output_html += "    <div class=\"row\">\n"
    output_html += "         <table class=\"table table-striped\">\n"
    output_html += "    <thead >\n"
    output_html += "      <tr>\n"
    output_html += "        <th class=\"header bgteal\" >Branch</th>\n"
    output_html += "        <th class=\"header bgteal\" >Percentage of commits</th>\n"
    output_html += "      </tr>\n"
    output_html += "    </thead>\n"
    output_html += " <tbody>\n"

    for key, value in branch_per.iteritems():
        output_html += "<tr>\n"
        output_html += "<td>" + key + "</td>\n"
        output_html += "<td>" + str(value) + " %</td>\n"
        output_html += "</tr>\n"
    output_html += "</tbody>\n</table>\n</div>\n"

    output_html += "<div id=\"chartdiv\"></div>"

    # Percentage of commits per author per branch
    output_html += "    <div class=\"row \">\n"
    output_html += "        <h2>Percentage of commits per author per branch</h2>\n"
    output_html += "    </div>\n"

    output_html += "    <div class=\"row\">\n"
    output_html += "         <table class=\"table table-striped\">\n"
    output_html += "    <thead >\n"
    output_html += "      <tr>\n"
    output_html += "        <th class=\"header bglightteal\" >Local Branch</th>\n"
    output_html += "        <th class=\"header bglightteal\" >Author</th>\n"
    output_html += "        <th class=\"header bglightteal\" >% of commits</th>\n"
    output_html += "      </tr>\n"
    output_html += "    </thead>\n"
    output_html += " <tbody>\n"

    com_br_authL = statistics["br_stats"]["com_br_authL"]
    for key, value in com_br_authL.iteritems():
        for commiter in value:
            output_html += "<tr>\n"
            output_html += "<td>" + key + "</td>\n"
            output_html += "<td>" + str(commiter[0]) + "</td>\n"
            output_html += "<td>" + str(commiter[1]) + "%</td>\n"
            output_html += "</tr>\n"
    output_html += "</tbody>\n</table>\n</div></div>\n"

    output_html += "<div id=\"branches\" class=\"container-fluid slideanim\" align=\"middle\">\n"

    br_stats = statistics["br_stats"]

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

    localB = statistics["br_stats"]["localB"]
    for i in range(0, len(localB)):
        output_html += "<tr>\n"
        output_html += "<td><a href=\"" + localB[i].strip('* \n').split("/")[-1] + "_local.html\" >" + localB[
            i] + "</a></td>\n"
        output_html += "<td>" + str(br_stats['branch_dates_local'][localB[i].strip('* \n')][0]) + "</td>\n"
        output_html += "<td>" + str(br_stats['branch_dates_local'][localB[i].strip('* \n')][1]) + "</td>\n"
        output_html += "</tr>\n"

    output_html += "</tbody></table></div></div>\n"

    output_html += generate_template("./html_templates/html_footer.html")

    output_html += generate_piecharts(com_auth, "pieChart")
    output_html += generate_barchart(branch_per)
    output_html += "</body>\n"
    output_html += "</html_templates>\n"

    if not os.path.exists(path):
        os.makedirs(path)

    f = open(path + "/index.html", 'w+')
    f.write(output_html)
    f.close()

    if not os.path.exists(path + "/style"):
        os.makedirs(path + "/style")
    f = open(path + "/style/style.css", "w+")
    css_output = generate_template("./styles/style.css")
    f.write(css_output)
    f.close()

    branch_stats_local = statistics["br_stats"]["branch_stats_local"]

    generate_branch_history(path, branch_stats_local, "local", statistics["br_stats"]["tagsR"])
