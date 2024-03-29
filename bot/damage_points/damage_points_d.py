from ..damage_points import fuction_all

def get_svg (point):

    dmp = fuction_all.dm_points(point)

    file_svg = f"""
        <svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 442 320" style="enable-background:new 0 0 442 320;" xml:space="preserve" class="D damageMap {dmp}">
							<style type="text/css">
								.D text {{
                                    font-family: 'PTSans-Bold';
                                    font-size: 14pt;
                                }}

                                .D line, .D polygon, .D rect {{
                                    fill: none;
                                    stroke: #000000;
                                    stroke-width: 2;
                                    stroke-linecap: round;
                                    stroke-linejoin: round;
                                    stroke-miterlimit: 10;
                                }}

                                .D .selected &gt; * {{
                                    stroke: none;
                                    stroke-width: 0;
                                }}

                                .V190 .D .selected .id_90 {{
                                    fill: yellow;
                                }}

                                .V290 .D .selected .id_90 {{
                                    fill: red;
                                }}

                                .V191 .D .selected .id_91 {{
                                    fill: yellow;
                                }}

                                .V291 .D .selected .id_91 {{
                                    fill: red;
                                }}

                                .V192 .D .selected .id_92 {{
                                    fill: yellow;
                                }}

                                .V292 .D .selected .id_92 {{
                                    fill: red;
                                }}

                                .V193 .D .selected .id_93 {{
                                    fill: yellow;
                                }}

                                .V293 .D .selected .id_93 {{
                                    fill: red;
                                }}

                                .V194 .D .selected .id_94 {{
                                    fill: yellow;
                                }}

                                .V294 .D .selected .id_94 {{
                                    fill: red;
                                }}

                                .V195 .D .selected .id_95 {{
                                    fill: yellow;
                                }}

                                .V295 .D .selected .id_95 {{
                                    fill: red;
                                }}

                                .V196 .D .selected .id_96 {{
                                    fill: yellow;
                                }}

                                .V296 .D .selected .id_96 {{
                                    fill: red;
                                }}

                                .V197 .D .selected .id_97 {{
                                    fill: yellow;
                                }}

                                .V297 .D .selected .id_97 {{
                                    fill: red;
                                }}

                                .V198 .D .selected .id_98 {{
                                    fill: yellow;
                                }}

                                .V298 .D .selected .id_98 {{
                                    fill: red;
                                }}

                                .V199 .D .selected .id_99 {{
                                    fill: yellow;
                                }}

                                .V299 .D .selected .id_99 {{
                                    fill: red;
                                }}
							</style>

                            <font horiz-adv-x="1000">
								<font-face font-family="PTSans-Bold" units-per-em="1000" underline-position="-75" underline-thickness="50"></font-face>
                                <missing-glyph horiz-adv-x="750" d="M50,700l650,0l0,-700l-650,0M570,620l-195,-217l-195,217l-50,-50l197,-220l-197,-220l50,-50l195,217l195,-217l50,50l-198,220l198,220M129,27l8,0l0,12l4,0C145,39 149,40 152,42C155,43 157,46 157,51C157,56 155,60 152,61C148,62 144,63 140,63l-11,0M141,57C146,57 149,55 149,52C149,49 148,47 147,47C145,46 143,46 140,46l-3,0l0,11M189,63l-31,0l0,-6l12,0l0,-30l7,0l0,30l12,0M222,37C222,34 220,33 215,33C210,33 207,34 206,35l-3,-7C204,28 206,28 208,27C210,26 213,26 216,26C225,26 230,30 230,38C230,44 227,47 221,48C215,49 212,51 212,54C212,56 214,57 218,57C221,57 224,56 227,55l2,7C225,63 221,64 218,64C209,64 204,60 204,53C204,50 205,47 207,46C209,45 211,44 213,43C215,42 217,41 219,40C221,39 222,38 222,37M237,47C240,48 243,49 246,49C249,49 251,48 251,45l0,-2C250,43 250,43 249,44C248,44 247,44 246,44C238,44 234,41 234,34C234,29 237,26 242,26C246,26 249,28 251,31l2,-4l6,0C258,28 258,31 258,34l0,11C258,52 255,55 248,55C245,55 243,55 241,54C238,53 236,53 235,52M245,32C242,32 241,33 241,36C241,39 243,40 246,40C247,40 248,40 249,40C250,39 250,39 251,39l0,-3C250,33 248,32 245,32M292,27l0,16C292,51 289,55 283,55C278,55 275,53 273,50l-2,4l-5,0l0,-27l7,0l0,17C274,47 276,48 279,48C282,48 284,46 284,42l0,-15M297,28C300,27 303,26 307,26C314,26 318,29 318,35C318,38 317,40 316,41C314,42 312,43 310,44C307,45 305,46 305,47C305,48 306,49 308,49C311,49 313,48 316,47l2,6C315,54 312,55 308,55C301,55 298,52 298,46C298,43 299,41 301,40C303,39 305,38 306,37C309,37 311,36 311,34C311,33 310,32 308,32C305,32 302,33 299,34M338,42C338,28 345,21 358,21C371,21 378,28 378,42C378,55 371,62 358,62C353,62 348,60 344,57C340,53 338,48 338,42M344,42C344,52 349,57 358,57C367,57 372,52 372,42C372,32 367,27 358,27C349,27 344,32 344,42M364,38C363,37 361,37 360,37C357,37 356,39 356,42C356,45 357,46 360,46l3,0l2,4C362,51 360,52 358,52C352,52 349,49 349,42C349,35 352,31 358,31C361,31 364,32 365,33M399,27l8,0l0,12l4,0C415,39 419,40 422,42C425,43 427,46 427,51C427,56 425,60 422,61C418,62 414,63 410,63l-11,0M411,57C416,57 419,55 419,52C419,49 418,47 417,47C415,46 413,46 410,46l-3,0l0,11M432,47C435,48 438,49 441,49C444,49 446,48 446,45l0,-2C445,43 445,43 444,44C443,44 442,44 441,44C432,44 428,41 428,34C428,29 431,26 437,26C441,26 444,28 446,31l2,-4l6,0C453,28 453,31 453,34l0,11C453,52 450,55 443,55C440,55 438,55 436,54C433,53 431,53 430,52M440,32C437,32 436,33 436,36C436,39 438,40 441,40C442,40 443,40 444,40C445,39 445,39 446,39l0,-3C445,33 443,32 440,32M478,54C477,55 476,55 474,55C471,55 469,53 468,50l-1,0l-1,4l-6,0l0,-27l8,0l0,17C468,47 470,48 474,48l1,0C476,48 476,48 476,48C476,47 476,47 477,47M483,47C487,48 490,49 492,49C495,49 497,48 497,45l0,-2C496,43 496,43 495,44C494,44 493,44 492,44C483,44 479,41 479,34C479,29 482,26 488,26C493,26 496,28 497,31l1,0l1,-4l6,0C504,28 504,31 504,34l0,11C504,52 501,55 494,55C491,55 489,55 487,54C485,53 483,53 482,52M491,32C488,32 487,33 487,36C487,39 489,40 492,40C493,40 494,40 495,40C496,39 496,39 497,39l0,-3C496,33 494,32 491,32M533,63l-31,0l0,-6l11,0l0,-30l8,0l0,30l12,0M541,54l-8,0l12,-27C544,24 543,22 540,22l-1,1l-2,-6C538,16 540,16 542,16C545,16 549,20 552,29l10,25l-8,0l-5,-15l0,-5l-1,0l-1,5M565,16l8,0l0,12C574,27 575,26 578,26C587,26 592,31 592,41C592,50 588,55 581,55C578,55 575,54 572,51l-1,0l-1,3l-5,0M579,49C582,49 584,46 584,41C584,35 582,32 577,32C576,32 574,33 573,34l0,10C573,47 575,49 579,49M618,34C617,33 614,32 611,32C606,32 604,34 603,38l19,0l0,6C622,48 621,51 619,53C616,54 613,55 610,55C601,55 596,50 596,40C596,31 601,26 610,26C612,26 614,26 616,27C618,28 620,28 621,29M610,49C614,49 616,47 615,43l-11,0C604,47 606,49 610,49z"></missing-glyph>
                                <glyph unicode="Д" horiz-adv-x="691" d="M674,-125l-97,0l-15,125l-450,0l-15,-125l-97,0l0,247l74,0C79,129 86,146 97,171C108,196 118,232 129,279C140,325 149,383 156,453C163,522 167,605 166,700l419,0l0,-578l89,0M448,122l0,456l-155,0C289,459 280,362 265,287C250,211 234,156 219,122z"></glyph>
                                <glyph unicode="З" horiz-adv-x="526" d="M120,310l0,107l24,0C150,417 157,417 166,417C175,417 184,417 193,418C202,418 210,419 219,420C228,421 235,422 240,423C263,428 283,438 300,452C317,465 325,484 325,507C325,539 315,561 295,573C274,584 247,590 214,590C184,590 156,586 130,578C104,570 84,562 71,555l-35,116C43,675 54,679 68,684C81,689 97,693 115,698C132,702 151,705 172,708C193,711 214,712 235,712C264,712 293,709 321,704C349,699 374,689 396,676C418,663 436,645 449,623C462,600 469,572 469,537C469,502 460,470 442,441C423,412 394,390 353,377l0,-5C396,363 430,345 455,316C479,287 491,249 491,201C491,163 483,131 468,104C453,77 433,54 408,37C383,20 354,7 321,-1C288,-10 255,-14 221,-14C177,-14 137,-10 101,-3C65,4 37,13 18,23l35,119C68,135 90,127 119,120C148,112 182,108 221,108C236,108 251,110 266,114C281,117 294,123 306,132C318,140 328,151 335,164C342,177 346,193 346,212C346,243 334,267 311,283C288,299 246,308 186,309C178,310 172,310 168,310C164,310 157,310 147,310z"></glyph>
                                <glyph unicode="К" horiz-adv-x="620" d="M233,299l-36,0l0,-299l-137,0l0,700l137,0l0,-310l32,14l193,296l156,0l-204,-294l-54,-38l56,-39l233,-329l-169,0z"></glyph>
                                <glyph unicode="П" horiz-adv-x="639" d="M442,578l-245,0l0,-578l-137,0l0,700l519,0l0,-700l-137,0z"></glyph>
                                <glyph unicode="У" horiz-adv-x="568" d="M294,391l20,-91l6,0l16,94l105,306l141,0l-186,-484C381,178 367,145 354,117C340,89 325,66 310,48C294,29 276,16 257,7C238,-2 215,-7 189,-7C167,-7 149,-5 136,-2C122,1 107,7 91,17l35,111C137,122 148,118 157,117C166,116 176,115 187,115C218,115 240,140 253,189l-262,511l161,0z"></glyph>
                                <glyph unicode="а" horiz-adv-x="496" d="M54,471C81,483 112,493 149,500C186,507 224,510 264,510C299,510 328,506 351,498C374,489 393,477 407,462C420,447 430,428 436,407C441,386 444,362 444,335C444,306 443,276 441,247C439,217 438,188 438,159C437,130 438,103 440,76C442,49 447,23 455,-1l-106,0l-21,69l-5,0C310,47 291,30 268,15C244,0 213,-8 176,-8C153,-8 132,-4 113,3C94,10 78,20 65,33C52,46 41,61 34,79C27,96 23,116 23,138C23,169 30,195 44,216C57,237 77,254 103,267C128,280 159,289 195,294C230,299 270,300 314,298C319,335 316,362 306,379C296,395 274,403 239,403C213,403 186,400 157,395C128,390 104,383 85,374M219,99C245,99 266,105 281,117C296,128 308,141 315,154l0,65C294,221 275,221 256,220C237,219 220,216 205,211C190,206 179,200 170,191C161,182 157,171 157,158C157,139 163,125 174,115C185,104 200,99 219,99z"></glyph>
                                <glyph unicode="б" horiz-adv-x="537" d="M142,406C161,435 184,457 211,470C237,483 269,489 306,489C367,489 415,471 451,434C486,397 504,339 504,261C504,171 484,103 443,56C402,9 345,-14 271,-14C194,-14 135,12 94,63C53,114 33,194 33,303C33,360 36,409 43,450C50,491 59,525 72,553C84,581 99,603 116,620C133,637 152,650 173,660C194,669 216,676 240,680C264,684 289,687 316,690C351,693 380,698 405,703C430,708 448,716 460,727l5,-116C452,600 433,592 408,588C383,583 350,579 308,576C283,575 260,572 241,567C222,562 205,554 191,542C177,530 166,513 158,492C149,470 143,441 139,406M167,244C167,201 175,166 192,138C209,110 234,96 269,96C305,96 331,109 347,134C362,159 370,196 370,244C370,287 363,321 348,344C333,367 309,379 275,379C238,379 211,367 194,343C176,319 167,286 167,244z"></glyph>
                                <glyph unicode="в" horiz-adv-x="505" d="M57,499C80,501 109,503 142,505C175,507 210,508 248,508C321,508 374,498 405,477C436,456 451,424 451,382C451,359 444,336 431,314C418,292 397,276 368,266l0,-4C404,254 430,240 446,220C462,199 470,173 470,141C470,91 451,54 413,29C374,4 313,-8 228,-8C200,-8 170,-7 139,-5C108,-4 80,-2 57,1M184,100C193,99 202,98 210,97C218,96 228,96 240,96C276,96 302,101 317,111C332,121 340,136 340,157C340,174 334,189 321,200C308,211 284,216 251,216l-67,0M253,296C274,296 292,301 306,312C319,322 326,335 326,351C326,368 320,382 309,391C297,400 276,404 245,404C230,404 218,404 209,403C200,402 191,402 184,401l0,-105z"></glyph>
                                <glyph unicode="г" horiz-adv-x="376" d="M380,385l-189,0l0,-385l-134,0l0,500l323,0z"></glyph>
                                <glyph unicode="д" horiz-adv-x="568" d="M554,-114l-95,0l-15,114l-336,0l-15,-114l-95,0l0,229l59,0C62,122 69,135 78,153C86,170 94,194 103,225C111,256 118,294 124,339C130,384 133,438 133,500l348,0l0,-385l73,0M351,109l0,281l-105,0C245,366 242,341 239,314C236,287 232,260 227,235C222,210 216,186 209,164C202,142 195,124 187,109z"></glyph>
                                <glyph unicode="е" horiz-adv-x="508" d="M457,43C437,27 410,14 376,3C341,-8 305,-14 266,-14C185,-14 126,10 89,57C52,104 33,168 33,250C33,338 54,404 96,448C138,492 197,514 273,514C298,514 323,511 347,504C371,497 392,486 411,471C430,456 445,435 456,409C467,383 473,351 473,312C473,298 472,283 471,267C469,251 466,234 463,217l-300,0C165,175 176,143 196,122C215,101 247,90 291,90C318,90 343,94 365,103C386,111 403,119 414,128M271,410C237,410 212,400 196,380C179,359 169,332 166,298l186,0C355,334 349,362 336,381C322,400 300,410 271,410z"></glyph>
                                <glyph unicode="з" horiz-adv-x="432" d="M109,207l0,91l61,0C193,298 213,303 228,312C243,321 250,334 250,349C250,367 243,380 230,388C217,395 196,399 169,399C143,399 120,396 100,389C80,382 64,375 52,368l-28,99C44,478 71,488 104,497C137,505 172,509 209,509C266,509 309,498 338,477C366,456 380,425 380,384C380,373 379,361 376,350C373,338 368,327 361,316C354,305 346,296 337,288C327,279 315,273 302,268l0,-4C337,256 362,242 377,222C392,201 399,174 399,140C399,119 395,99 386,81C377,62 364,46 347,33C329,20 307,9 280,1C253,-7 222,-11 185,-11C148,-11 117,-7 90,1C63,8 40,17 22,27l28,101C65,119 84,112 106,107C127,102 151,99 178,99C239,99 269,118 269,157C269,174 261,187 246,195C230,203 201,207 158,207z"></glyph>
                                <glyph unicode="и" horiz-adv-x="545" d="M358,228l5,71l-3,0l-43,-73l-178,-226l-82,0l0,500l130,0l0,-238l-6,-68l4,0l41,71l180,235l82,0l0,-500l-130,0z"></glyph>
                                <glyph unicode="й" horiz-adv-x="545" d="M358,228l5,71l-3,0l-43,-73l-178,-226l-82,0l0,500l130,0l0,-238l-6,-68l4,0l41,71l180,235l82,0l0,-500l-130,0M219,704C224,678 232,660 243,649C254,638 268,633 285,633C304,633 319,638 330,649C341,660 348,678 352,703l99,-25C443,635 423,603 392,582C361,561 324,550 282,550C261,550 241,552 222,557C203,562 185,569 170,580C155,590 142,603 131,619C120,635 113,655 109,678z"></glyph>
                                <glyph unicode="к" horiz-adv-x="489" d="M222,207l-35,0l0,-207l-130,0l0,500l130,0l0,-213l31,14l117,199l139,0l-121,-190l-51,-38l56,-39l135,-233l-149,0z"></glyph>
                                <glyph unicode="л" horiz-adv-x="515" d="M329,385l-99,0C226,338 221,291 216,244C211,197 202,156 191,119C179,82 163,52 143,29C123,6 97,-6 65,-6C26,-6 -1,-1 -17,9l16,108C10,113 20,111 29,111C42,111 54,117 64,128C74,139 83,160 90,189C97,218 102,258 107,309C111,359 114,423 116,500l343,0l0,-500l-130,0z"></glyph>
                                <glyph unicode="н" horiz-adv-x="537" d="M350,197l-163,0l0,-197l-130,0l0,500l130,0l0,-188l163,0l0,188l130,0l0,-500l-130,0z"></glyph>
                                <glyph unicode="о" horiz-adv-x="537" d="M33,250C33,335 54,400 95,446C136,491 194,514 269,514C309,514 344,508 373,495C402,482 427,465 446,442C465,419 480,391 490,358C499,325 504,289 504,250C504,165 484,100 443,55C402,9 344,-14 269,-14C229,-14 194,-8 165,5C136,18 111,36 92,59C72,82 57,109 48,142C38,175 33,211 33,250M167,250C167,228 169,208 173,189C177,170 183,154 191,140C199,126 210,115 223,108C236,100 251,96 269,96C303,96 328,108 345,133C362,158 370,197 370,250C370,296 362,333 347,362C332,390 306,404 269,404C237,404 212,392 194,368C176,344 167,305 167,250z"></glyph>
                                <glyph unicode="п" horiz-adv-x="532" d="M345,385l-158,0l0,-385l-130,0l0,500l418,0l0,-500l-130,0z"></glyph>
                                <glyph unicode="р" horiz-adv-x="540" d="M57,500l95,0l15,-60l4,0C188,465 209,484 233,496C256,508 285,514 319,514C382,514 429,494 460,455C491,415 507,351 507,263C507,220 502,182 492,148C482,113 467,84 448,60C428,36 404,18 376,5C347,-8 315,-14 278,-14C257,-14 240,-12 227,-9C214,-6 200,-2 187,5l0,-205l-130,0M280,404C255,404 235,398 221,385C206,372 195,353 187,328l0,-208C196,113 207,107 218,103C229,98 243,96 261,96C298,96 326,109 345,136C364,162 373,205 373,266C373,310 366,344 351,368C336,392 313,404 280,404z"></glyph>
                                <glyph unicode="у" horiz-adv-x="478" d="M239,219l18,-78l6,0l13,79l76,280l134,0l-152,-451C321,12 309,-22 298,-53C286,-84 273,-111 259,-134C245,-157 230,-174 213,-186C196,-199 175,-205 152,-205C117,-205 90,-199 69,-188l24,104C103,-88 113,-90 123,-90C138,-90 153,-83 168,-70C182,-57 193,-34 200,0l-209,500l156,0z"></glyph>
                                <glyph unicode="ш" horiz-adv-x="754" d="M57,0l0,500l130,0l0,-385l125,0l0,385l130,0l0,-385l125,0l0,385l130,0l0,-500z"></glyph>
                                <glyph unicode="щ" horiz-adv-x="783" d="M769,-114l-94,0l-15,114l-603,0l0,500l130,0l0,-385l125,0l0,385l130,0l0,-385l125,0l0,385l130,0l0,-385l72,0z"></glyph>
                                <glyph unicode="ы" horiz-adv-x="703" d="M187,109C207,105 226,103 244,103C274,103 295,109 307,120C319,131 325,148 325,171C325,192 319,209 307,220C295,231 275,236 247,236C225,236 205,234 187,229M187,322C203,325 219,327 236,328C252,329 267,329 280,329C314,329 342,325 365,318C388,310 406,299 420,285C434,271 444,255 450,236C456,217 459,196 459,174C459,144 455,118 447,95C439,72 426,54 408,39C390,24 367,12 338,5C309,-3 274,-7 232,-7C194,-7 161,-6 134,-5C106,-4 80,-2 57,0l0,500l130,0M516,500l130,0l0,-500l-130,0z"></glyph>
							</font>

                            <g class="D">
								<g class="selected">
									<polygon class="id_90" points="441,136 441,274 350,183.2 350,136"></polygon>
                                    <polygon class="id_91" points="350,183 441,274 223,274 223,183 293,183"></polygon>
                                    <polygon class="id_92" points="223,183 223,274 1,274 94,183"></polygon>
                                    <polygon class="id_93" points="94,141.8 94,183 1,274 1,142"></polygon>
                                    <polygon class="id_94" points="94,85 94,142 1,142 1,1"></polygon>
                                    <polygon class="id_95" points="223,1 223,85 94,85 1,1"></polygon>
                                    <polygon class="id_96" points="441,1 350,85 293,85 223,85 223,1"></polygon>
                                    <polygon class="id_97" points="441,1 441,136 350,136 350,85"></polygon>
                                    <polygon class="id_98" points="350,85 350,183 94,183 94,85 223,85"></polygon>
                                    <rect class="id_99" x="1" y="275" width="440" height="45"></rect>
								</g>
                                <g class="scheme">
									<text transform="matrix(1 0 0 1 357 173)"><tspan x="0" y="0">Передний</tspan>
                                        <tspan x="19.2" y="21.6">правый</tspan>
                                        <tspan x="44.7" y="43.2">угол</tspan></text>
                                    <text transform="matrix(1 0 0 1 244 210)"><tspan x="0" y="0">Передний</tspan>
                                        <tspan x="0" y="21.6">правый</tspan>
                                        <tspan x="0" y="43.2">бок</tspan></text>
                                    <text transform="matrix(1 0 0 1 137 210)"><tspan x="0" y="0">Задний</tspan>
                                        <tspan x="-1.9" y="21.6">правый</tspan>
                                        <tspan x="29.8" y="43.2">бок</tspan></text>
                                    <text transform="matrix(1 0 0 1 12 173)"><tspan x="0" y="0">Задний</tspan>
                                        <tspan x="0" y="21.6">правый</tspan>
                                        <tspan x="0" y="43.2">угол</tspan></text>
                                    <text transform="matrix(1 0 0 1 12 73)"><tspan x="0" y="0">Угол</tspan>
                                        <tspan x="0" y="21.6">левый</tspan>
                                        <tspan x="0" y="43.2">задний</tspan></text>
                                    <text transform="matrix(1 0 0 1 137 27)"><tspan x="0" y="0">Задний</tspan>
                                        <tspan x="7.9" y="21.6">левый</tspan>
                                        <tspan x="29.8" y="43.2">бок</tspan></text>
                                    <text transform="matrix(1 0 0 1 244 27)"><tspan x="0" y="0">Передний</tspan>
                                        <tspan x="0" y="21.6">левый</tspan>
                                        <tspan x="0" y="43.2">бок</tspan></text>
                                    <text transform="matrix(1 0 0 1 400 73)"><tspan x="0" y="0">Угол</tspan>
                                        <tspan x="-14" y="21.6">левый</tspan>
                                        <tspan x="-41.2" y="43.2">передний</tspan></text>
                                    <text transform="matrix(1 0 0 1 195 304)">Днище</text>
                                    <text transform="matrix(1 0 0 1 195 138)">Крыша</text>

                                    <line x1="350" y1="136" x2="293" y2="85"></line>
                                    <line x1="350" y1="136" x2="293" y2="183"></line>
                                    <line x1="1" y1="274" x2="94" y2="183"></line>
                                    <line x1="223" y1="183" x2="223" y2="274"></line>
                                    <line x1="441" y1="274" x2="350" y2="183"></line>
                                    <line x1="350" y1="136" x2="441" y2="136"></line>
                                    <line x1="350" y1="85" x2="441" y2="1"></line>
                                    <line x1="223" y1="85" x2="223" y2="1"></line>
                                    <line x1="94" y1="142" x2="1" y2="142"></line>
                                    <polygon points="94,85 223,85 293,85 350,85 350,136 350,183 293,183 223,183 94,183 94,142"></polygon>
                                    <line x1="94" y1="85" x2="1" y2="1"></line>
                                    <line x1="1" y1="274" x2="441" y2="274"></line>
								</g>
							</g>
						</svg>
    """
    return file_svg