import fuction_all
import get_dtp

def get_svg (point):

    dmp = fuction_all.dm_points(point)

    file_svg = f"""
        <svg version="1.1" xmlns="http://www.w3.org/2000/svg" x="0px" y="0px" viewBox="0 0 801 514" style="enable-background:new 0 0 801 514;" xml:space="preserve" class="B damageMap {dmp}">
							<style type="text/css">
								.B * {{
                                    fill: none;
                                }}

                                .B .path path, .path polygon, .path rect,
                                .B .path circle, .path line {{
                                    fill: none;
                                    stroke: #000000;
                                    stroke-width: 1;
                                    stroke-linejoin: round;
                                }}

                                .B .path .fill {{
                                    fill: #000000;
                                }}

                                .B .w05 {{
                                    stroke-width: 0.5 !important;
                                }}

                                .B .w2 {{
                                    stroke-width: 2 !important;
                                }}

                                .B polygon.well {{
                                    fill: #000000;
                                    stroke: none;
                                }}

                                .B .well path {{
                                    fill: #000000;
                                    stroke: none;
                                }}

                                .B .well circle {{
                                    stroke-width: 0.5;
                                }}

                                .B .red {{
                                    fill: red !important;
                                }}

                                .B .white {{
                                    fill: white !important;
                                }}

                                .B .yellow {{
                                    fill: yellow !important;
                                }}

                                .B .dashdot {{
                                    fill: none;
                                    stroke: #7C7C7C;
                                    stroke-width: 1.5;
                                    stroke-dasharray: 7;
                                }}

                                .B .selected &gt; * {{
                                    stroke: none;
                                    stroke-width: 0;
                                }}

                                .B .hover &gt; * {{
                                    opacity: 0.01;
                                    fill: #FFFFFF;
                                }}

                                .V130 .B .selected .id_01 {{
                                    fill: yellow;
                                }}

                                .V230 .B .selected .id_01 {{
                                    fill: red;
                                }}

                                .V131 .B .selected .id_02 {{
                                    fill: yellow;
                                }}

                                .V231 .B .selected .id_02 {{
                                    fill: red;
                                }}

                                .V132 .B .selected .id_03 {{
                                    fill: yellow;
                                }}

                                .V232 .B .selected .id_03 {{
                                    fill: red;
                                }}

                                .V133 .B .selected .id_04 {{
                                    fill: yellow;
                                }}

                                .V233 .B .selected .id_04 {{
                                    fill: red;
                                }}

                                .V134 .B .selected .id_05 {{
                                    fill: yellow;
                                }}

                                .V234 .B .selected .id_05 {{
                                    fill: red;
                                }}

                                .V135 .B .selected .id_06 {{
                                    fill: yellow;
                                }}

                                .V235 .B .selected .id_06 {{
                                    fill: red;
                                }}

                                .V136 .B .selected .id_07 {{
                                    fill: yellow;
                                }}

                                .V236 .B .selected .id_07 {{
                                    fill: red;
                                }}

                                .V137 .B .selected .id_08 {{
                                    fill: yellow;
                                }}

                                .V237 .B .selected .id_08 {{
                                    fill: red;
                                }}

                                .V138 .B .selected .id_09 {{
                                    fill: yellow;
                                }}

                                .V238 .B .selected .id_09 {{
                                    fill: red;
                                }}

                                .V139 .B .selected .id_10 {{
                                    fill: yellow;
                                }}

                                .V239 .B .selected .id_10 {{
                                    fill: red;
                                }}

                                .V140 .B .selected .id_11 {{
                                    fill: yellow;
                                }}

                                .V240 .B .selected .id_11 {{
                                    fill: red;
                                }}

                                .V141 .B .selected .id_12 {{
                                    fill: yellow;
                                }}

                                .V241 .B .selected .id_12 {{
                                    fill: red;
                                }}

                                .V142 .B .selected .id_13 {{
                                    fill: yellow;
                                }}

                                .V242 .B .selected .id_13 {{
                                    fill: red;
                                }}

                                .V143 .B .selected .id_14 {{
                                    fill: yellow;
                                }}

                                .V243 .B .selected .id_14 {{
                                    fill: red;
                                }}
							</style>

                            <g class="B">
								<g class="bottom">
									<g class="selected">
										<path class="id_14" d="M664.3,506.8c0,3.1-2.6,5.7-5.7,5.7H152c-3.1,0-5.7-2.6-5.7-5.7v-96c0-3.1,2.6-5.7,5.7-5.7h506.7c3.1,0,5.7,2.6,5.7,5.7V506.8z"></path>
									</g>
                                    <g class="path">
										<path class="body w2" d="M664.3,506.8c0,3.1-2.6,5.7-5.7,5.7H152c-3.1,0-5.7-2.6-5.7-5.7v-96c0-3.1,2.6-5.7,5.7-5.7h506.7c3.1,0,5.7,2.6,5.7,5.7V506.8z"></path>
                                        <g class="transmissions">
											<rect x="247.1" y="456.8" width="32.4" height="3.7"></rect>
                                            <path d="M295.2,458.8c0-3.2-1.9-6-4.7-7.2V437H284v14.5c-2.8,1.2-4.7,4-4.7,7.2c0,3.2,1.9,6,4.7,7.2v14.5h6.5V466C293.3,464.8,295.2,462,295.2,458.8z"></path>
                                            <rect x="549" y="421.3" width="6.5" height="75"></rect>
										</g>
                                        <g class="engine">
											<rect x="222.1" y="451.8" width="25" height="13.6"></rect>
                                            <rect x="174.3" y="446.9" width="47.8" height="23.4"></rect>
                                            <rect x="171.1" y="486.6" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -293.611 273.7299)" width="24.9" height="9.4"></rect>
                                            <rect class="fill" x="164.9" y="501.7" transform="matrix(0.7071 -0.7071 0.7071 0.7071 -306.5184 268.3646)" width="11.6" height="5"></rect>
                                            <path class="fill" d="M231,474.7v-9.3h-5v9.3c-0.1,0-0.4,0.1-0.8,0.1h-27.6c-0.7,0-1.3,0.3-1.8,0.7l-5.2,5.2l3.5,3.5l4.5-4.5h26.5c2.1,0,3.6-0.6,4.7-1.8C230.8,476.9,231,475.6,231,474.7z"></path>
										</g>
                                        <g class="wells">
											<polygon class="well" points="308.3,493.3 266.3,493.3 264.4,491.3 264.4,482.4 266.3,480.5 308.3,480.5 310.2,482.4 310.2,491.3 308.3,493.3"></polygon>
                                            <polygon class="well" points="308.3,509 266.3,509 264.4,507.1 264.4,498.2 266.3,496.2 308.3,496.2 310.2,498.2 310.2,507.1 308.3,509"></polygon>
                                            <polygon class="well" points="308.3,421.3 266.3,421.3 264.4,419.4 264.4,410.4 266.3,408.5 308.3,408.5 310.2,410.4 310.2,419.4 308.3,421.3"></polygon>
                                            <polygon class="well" points="573.2,509 531.2,509 529.3,507.1 529.3,498.2 531.2,496.2 573.2,496.2 575.1,498.2 575.1,507.1 573.2,509"></polygon>
                                            <polygon class="well" points="573.2,421.3 531.2,421.3 529.3,419.4 529.3,410.4 531.2,408.5 573.2,408.5 575.1,410.4 575.1,419.4 573.2,421.3"></polygon>
                                            <polygon class="well" points="308.3,437 266.3,437 264.4,435.1 264.4,426.2 266.3,424.3 308.3,424.3 310.2,426.2 310.2,435.1 308.3,437"></polygon>
										</g>
									</g>
                                    <g class="hover">
										<path d="M664.3,506.8c0,3.1-2.6,5.7-5.7,5.7H152c-3.1,0-5.7-2.6-5.7-5.7v-96c0-3.1,2.6-5.7,5.7-5.7h506.7c3.1,0,5.7,2.6,5.7,5.7V506.8z">
											<title>Днище</title>
										</path>
									</g>
								</g>

                                <g class="right">
									<g class="selected">
										<path class="id_04" d="M293.9,267.4v-4.5h-32.7v4.5h-94.7v-4h-3.1V262h-7.3v1.4H153v4H152c-3.2,0-5.8,2.6-5.9,5.7l-2.5,91.9c-0.1,3.1,2.4,6,5.5,6.4l42,5c3.1,0.4,8.3,0.7,11.4,0.7h58.8v-1.6h4.8h0c3.2,8.7,11.6,14.8,21.4,14.8c9.8,0,18.1-6.2,21.4-14.8h0h4.5v1.6h9.7V267.4H293.9z"></path>
                                        <path class="id_03" d="M556.9,267.4v-4.5h-32.7v4.5h-99v-4.5h-32.7v4.5H323v109.7h203.5v-1.6h4.5c3.2,8.7,11.6,14.8,21.4,14.8c9.8,0,18.1-6.2,21.4-14.8h4.7v1.6h6V267.4H556.9z"></path>
                                        <path class="id_02" d="M656.9,267.4h-72.3v109.7h64.3c3.2,0,8.3-0.5,11.4-1l0.7-0.1c3.1-0.6,5.5-3.6,5.4-6.7l-3.6-96C662.7,270,660,267.4,656.9,267.4z"></path>
									</g>
                                    <g class="path">
										<g class="body">
											<path class="w2" d="M662.8,273.1c-0.1-3.1-2.8-5.7-5.9-5.7H152c-3.2,0-5.8,2.6-5.9,5.7l-2.5,91.9c-0.1,3.2,2.4,6,5.5,6.4l42,5c3.1,0.4,8.3,0.7,11.4,0.7h58.8v-11.5c0-13.2,10.8-24,24-24h4c13.2,0,24,10.8,24,24v11.5h213.3v-11.5c0-13.2,10.8-24,24-24h4c13.2,0,24,10.8,24,24v11.5h70.4c3.2,0,8.3-0.5,11.4-1l0.7-0.1c3.1-0.6,5.5-3.6,5.4-6.7L662.8,273.1z"></path>
                                            <rect class="w05" x="151.5" y="327.1" width="26.4" height="5.4"></rect>
                                            <rect class="w05" x="151.5" y="335" width="26.4" height="5.4"></rect>
                                            <rect class="w05" x="151.5" y="342.9" width="26.4" height="5.4"></rect>
                                            <rect class="w05" x="151.5" y="350.8" width="26.4" height="5.4"></rect>
                                            <polygon points="143.8,359.9 148.5,355.5 148.6,311.9 145.2,309.1"></polygon>
                                            <rect x="261.3" y="262.9" width="32.7" height="4.5"></rect>
                                            <rect x="392.6" y="262.9" width="32.7" height="4.5"></rect>
                                            <rect x="524.3" y="262.9" width="32.7" height="4.5"></rect>
                                            <path d="M666.1,361l-0.4-10.9h-13c0,0,1.7,11.2,8.7,11C663.1,361,664.7,361,666.1,361z"></path>
                                            <rect class="w05" x="369.8" y="361.6" width="9.3" height="2.4"></rect>
                                            <rect class="w05" x="369.8" y="365.2" width="9.3" height="2.4"></rect>
                                            <rect class="w05" x="369.8" y="368.7" width="9.3" height="2.4"></rect>
                                            <rect class="w05" x="357.9" y="361.6" width="9.3" height="2.4"></rect>
                                            <rect class="w05" x="357.9" y="365.2" width="9.3" height="2.4"></rect>
                                            <rect class="w05" x="357.9" y="368.7" width="9.3" height="2.4"></rect>
                                            <rect x="331.8" y="359.3" width="52.7" height="17.7"></rect>
                                            <rect x="156.1" y="262" width="7.3" height="1.4"></rect>
                                            <rect x="153" y="263.4" width="13.6" height="4"></rect>
										</g>
                                        <g class="wells">
											<g class="well">
												<circle cx="287.5" cy="367.4" r="2.7"></circle>
                                                <circle cx="287.5" cy="367.4" r="6.3"></circle>
                                                <circle cx="287.5" cy="367.4" r="9.5"></circle>
                                                <circle cx="287.5" cy="359.5" r="0.6"></circle>
                                                <circle cx="282.8" cy="361" r="0.6"></circle>
                                                <circle cx="279.9" cy="365" r="0.6"></circle>
                                                <circle cx="279.9" cy="369.9" r="0.6"></circle>
                                                <circle cx="282.8" cy="373.8" r="0.6"></circle>
                                                <circle cx="287.5" cy="375.3" r="0.6"></circle>
                                                <circle cx="292.1" cy="373.8" r="0.6"></circle>
                                                <circle cx="295" cy="369.9" r="0.6"></circle>
                                                <circle cx="295" cy="365" r="0.6"></circle>
                                                <circle cx="292.1" cy="361" r="0.6"></circle>
                                                <path d="M287.5,344.6c-12.6,0-22.8,10.2-22.8,22.8c0,12.6,10.2,22.8,22.8,22.8c12.6,0,22.8-10.2,22.8-22.8C310.3,354.8,300.1,344.6,287.5,344.6z M287.5,380.4c-7.2,0-13-5.8-13-13c0-7.2,5.8-13,13-13s13,5.8,13,13C300.5,374.6,294.6,380.4,287.5,380.4z"></path>
											</g>
                                            <g class="well">
												<circle cx="552.5" cy="367.4" r="2.7"></circle>
                                                <circle cx="552.5" cy="367.4" r="6.3"></circle>
                                                <circle cx="552.5" cy="367.4" r="9.5"></circle>
                                                <circle cx="552.5" cy="359.5" r="0.6"></circle>
                                                <circle cx="547.8" cy="361" r="0.6"></circle>
                                                <circle cx="544.9" cy="365" r="0.6"></circle>
                                                <circle cx="544.9" cy="369.9" r="0.6"></circle>
                                                <circle cx="547.8" cy="373.8" r="0.6"></circle>
                                                <circle cx="552.5" cy="375.3" r="0.6"></circle>
                                                <circle cx="557.1" cy="373.8" r="0.6"></circle>
                                                <circle cx="560" cy="369.9" r="0.6"></circle>
                                                <circle cx="560" cy="365" r="0.6"></circle>
                                                <circle cx="557.1" cy="361" r="0.6"></circle>
                                                <path d="M552.5,344.6c-12.6,0-22.8,10.2-22.8,22.8c0,12.6,10.2,22.8,22.8,22.8c12.6,0,22.8-10.2,22.8-22.8C575.3,354.8,565.1,344.6,552.5,344.6z M552.5,380.4c-7.2,0-13-5.8-13-13c0-7.2,5.8-13,13-13s13,5.8,13,13C565.5,374.6,559.6,380.4,552.5,380.4z"></path>
											</g>
										</g>
                                        <g class="doors">
											<g class="door">
												<line x1="218.2" y1="286.9" x2="218.2" y2="373.4"></line>
                                                <rect x="188" y="286.9" width="60.4" height="86.5"></rect>
                                                <rect class="w05" x="191.7" y="289.6" width="20.9" height="59.5"></rect>
                                                <rect class="w05" x="223.7" y="289.6" width="20.9" height="59.5"></rect>
                                                <line class="w05" x1="214.9" y1="287" x2="214.9" y2="373.5"></line>
                                                <line class="w05" x1="221.5" y1="287" x2="221.5" y2="373.5"></line>
											</g>
                                            <g class="door">
												<line x1="418" y1="286.9" x2="418" y2="373.4"></line>
                                                <rect x="387.8" y="286.9" width="60.4" height="86.5"></rect>
                                                <rect class="w05" x="391.6" y="289.6" width="20.9" height="59.5"></rect>
                                                <rect class="w05" x="423.6" y="289.6" width="20.9" height="59.5"></rect>
                                                <line class="w05" x1="414.7" y1="287" x2="414.7" y2="373.5"></line>
                                                <line class="w05" x1="421.3" y1="287" x2="421.3" y2="373.5"></line>
											</g>
                                            <g class="door">
												<line x1="617.7" y1="286.9" x2="617.7" y2="373.4"></line>
                                                <rect x="587.5" y="286.9" width="60.4" height="86.5"></rect>
                                                <rect class="w05" x="591.2" y="289.6" width="20.9" height="59.5"></rect>
                                                <rect x="623.2" y="289.6" class="w05" width="20.9" height="59.5"></rect>
                                                <line class="w05" x1="614.4" y1="287" x2="614.4" y2="373.5"></line>
                                                <line class="w05" x1="621" y1="287" x2="621" y2="373.5"></line>
											</g>
										</g>
                                        <g class="windows">
											<g class="window">
												<rect x="252.4" y="280.5" width="65.6" height="48"></rect>
                                                <rect x="318" y="280.5" width="65.5" height="48"></rect>
                                                <line x1="318" y1="295.9" x2="252.4" y2="295.9"></line>
                                                <line x1="318" y1="295.9" x2="383.5" y2="295.9"></line>
                                                <rect class="w05" x="254" y="282.3" width="62.5" height="12.2"></rect>
                                                <rect class="w05" x="319.4" y="282.3" width="62.5" height="12.2"></rect>
											</g>
                                            <polyline class="window" points="663.1,280.4 652.3,280.4 652.3,339 665.3,339"></polyline>
                                            <g class="window">
												<rect x="452.7" y="280.5" width="65.6" height="48"></rect>
                                                <rect x="518.3" y="280.5" width="65.5" height="48"></rect>
                                                <line x1="518.3" y1="295.9" x2="583.8" y2="295.9"></line>
                                                <rect class="w05" x="519.7" y="282.3" width="62.5" height="12.2"></rect>
											</g>
										</g>
									</g>
                                    <g class="hover">
										<path d="M293.9,267.4v-4.5h-32.7v4.5h-94.7v-4h-3.1V262h-7.3v1.4H153v4H152c-3.2,0-5.8,2.6-5.9,5.7l-2.5,91.9c-0.1,3.1,2.4,6,5.5,6.4l42,5c3.1,0.4,8.3,0.7,11.4,0.7h58.8v-1.6h4.8h0c3.2,8.7,11.6,14.8,21.4,14.8c9.8,0,18.1-6.2,21.4-14.8h0h4.5v1.6h9.7V267.4H293.9z">
											<title>Правая боковая (задняя) сторона (дверь, стекло, элементы кузова, колеса и т.д.)</title>
										</path>
                                        <path d="M556.9,267.4v-4.5h-32.7v4.5h-99v-4.5h-32.7v4.5H323v109.7h203.5v-1.6h4.5c3.2,8.7,11.6,14.8,21.4,14.8c9.8,0,18.1-6.2,21.4-14.8h4.7v1.6h6V267.4H556.9z">
											<title>Правая боковая (средняя) сторона (дверь, стекло, элементы кузова, колеса и т.д.)</title>
										</path>
                                        <path d="M656.9,267.4h-72.3v109.7h64.3c3.2,0,8.3-0.5,11.4-1l0.7-0.1c3.1-0.6,5.5-3.6,5.4-6.7l-3.6-96C662.7,270,660,267.4,656.9,267.4z">
											<title>Правая боковая (передняя) сторона (дверь, стекло, элементы кузова и т.д.)</title>
										</path>
									</g>
								</g>

                                <g class="front">
									<g class="selected">
										<path class="id_01" d="M799.1,231.1h-11.8v-37.5H677.4v23.9h3.9v26.7c0,1.7,1.4,3,3,3h7.8l12.2,8.5v2.1h17.8v-7.1h-17.8v1.1l-6.8-4.6h86.8c1.6,0,3-1.3,3-3v-0.4h11.8l1.9-1.9V233L799.1,231.1z"></path>
                                        <path class="id_10" d="M799.1,143.4h-11.8v-0.5c0-1.6-1.4-3-3-3h-86.8l6.8-4.6v1.1h17.8v-7.1h-17.8v2.1l-12.2,8.5h-7.8c-1.6,0-3,1.4-3,3v26.8h-3.9v23.9h109.9v-37.5h11.8l1.9-1.9v-8.9L799.1,143.4z"></path>
									</g>
                                    <g class="path">
										<g class="body">
											<path class="w2" d="M787.3,244.2c0,1.7-1.4,3-3,3h-100c-1.6,0-3-1.3-3-3V142.9c0-1.6,1.4-3,3-3h100c1.6,0,3,1.4,3,3V244.2z"></path>
                                            <rect x="677.4" y="169.7" width="3.8" height="47.8"></rect>
                                            <path d="M686,142.2c-1.1,0-2,0.9-2,2v98.1c0,1.1,0.9,2,2,2h4.9c1.1,0,2-0.9,2-2v-98.1c0-1.1-0.9-2-2-2H686z"></path>
                                            <circle class="w05" cx="686.5" cy="241.5" r="1.4"></circle>
                                            <circle class="w05" cx="686.5" cy="144.9" r="1.4"></circle>
                                            <line x1="772.4" y1="139.9" x2="772.4" y2="247.3"></line>
                                            <path d="M762,228.8v18.5h22.3c1.6,0,3-1.3,3-3v-23.5H770C765.6,220.8,762,224.4,762,228.8z"></path>
                                            <path d="M784.3,139.9H762v18.5c0,4.4,3.6,8,8,8h17.3v-23.5C787.3,141.2,785.9,139.9,784.3,139.9z"></path>
                                            <rect x="775.3" y="182.4" width="4.4" height="22.4"></rect>
                                            <circle cx="766.9" cy="193.6" r="3.3"></circle>
                                            <path d="M753,161h-2.3v65.2h2.3c2.8,0,5-2.3,5-5V166C758,163.2,755.7,161,753,161z"></path>
										</g>
                                        <g class="wells">
											<polygon class="well" points="787.2,243.8 799.1,243.8 801,241.9 801,233 799.1,231.1 787.2,231.1"></polygon>
                                            <polygon class="well" points="787.2,156.1 799.1,156.1 801,154.2 801,145.3 799.1,143.4 787.2,143.4"></polygon>
										</g>
                                        <g class="lights">
											<circle class="light" cx="767" cy="243" r="2.3"></circle>
                                            <circle class="light" cx="778.9" cy="243" r="2.3"></circle>
                                            <circle class="light" cx="767.4" cy="227.8" r="3.8"></circle>
                                            <circle class="light" cx="767.4" cy="236.2" r="3.8"></circle>
                                            <circle class="light" cx="767" cy="144.5" r="2.3"></circle>
                                            <circle class="light" cx="778.9" cy="144.5" r="2.3"></circle>
                                            <circle class="light" cx="767.4" cy="159.7" r="3.8"></circle>
                                            <circle class="light" cx="767.4" cy="151.3" r="3.8"></circle>
										</g>
                                        <rect class="window" x="695.1" y="139.9" width="55.5" height="107.3"></rect>
                                        <g class="wipers">
											<g class="wiper">
												<circle class="w05" cx="754" cy="166.4" r="2.5"></circle>
                                                <line class="w2" x1="710.4" y1="189.5" x2="745.3" y2="189.5"></line>
                                                <line class="w05" x1="729.1" y1="189.5" x2="751.6" y2="167"></line>
                                                <line class="w05" x1="732.1" y1="189.5" x2="753" y2="168.6"></line>
											</g>
                                            <g class="wiper">
												<circle class="w05" cx="754" cy="220.8" r="2.5"></circle>
                                                <line class="w2" x1="710.4" y1="197.6" x2="745.3" y2="197.6"></line>
                                                <line class="w05" x1="729.1" y1="197.6" x2="751.6" y2="220.1"></line>
                                                <line class="w05" x1="732.1" y1="197.6" x2="753" y2="218.4"></line>
											</g>
										</g>
                                        <g class="mirrors">
											<g class="mirror">
												<rect x="704.4" y="250.8" width="17.8" height="7.1"></rect>
                                                <polygon points="704.4,255.8 692.1,247.2 697.5,247.2 704.4,251.8"></polygon>
											</g>
                                            <g class="mirror">
												<rect x="704.4" y="129.2" width="17.8" height="7.1"></rect>
                                                <polygon points="704.4,131.4 692.1,139.9 697.5,139.9 704.4,135.3"></polygon>
											</g>
										</g>
									</g>
                                    <g class="hover">
										<path d="M799.1,231.1h-11.8v-37.5H677.4v23.9h3.9v26.7c0,1.7,1.4,3,3,3h7.8l12.2,8.5v2.1h17.8v-7.1h-17.8v1.1l-6.8-4.6h86.8c1.6,0,3-1.3,3-3v-0.4h11.8l1.9-1.9V233L799.1,231.1z">
											<title>Правая передняя сторона (фары, стекло, бампер и т.д.)</title>
										</path>
                                        <path d="M799.1,143.4h-11.8v-0.5c0-1.6-1.4-3-3-3h-86.8l6.8-4.6v1.1h17.8v-7.1h-17.8v2.1l-12.2,8.5h-7.8c-1.6,0-3,1.4-3,3v26.8h-3.9v23.9h109.9v-37.5h11.8l1.9-1.9v-8.9L799.1,143.4z">
											<title>Левая передняя сторона (фары, стекло, бампер и т.д.)</title>
										</path>
									</g>
								</g>

                                <g class="top">
									<g class="selected">
										<path class="id_11" d="M658.6,247.3c3.1,0,5.7-2.6,5.7-5.7v-96c0-3.1-2.6-5.7-5.7-5.7h-74v107.3H658.6z"></path>
                                        <rect class="id_12" x="323" y="139.9" width="261.6" height="107.3"></rect>
                                        <path class="id_13" d="M152,139.9c-3.1,0-5.7,2.6-5.7,5.7v96c0,3.1,2.6,5.7,5.7,5.7h171V139.9H152z"></path>
									</g>
                                    <g class="path">
										<g class="body">
											<circle cx="159.8" cy="236.8" r="6.7"></circle>
                                            <circle class="w05" cx="159.8" cy="236.8" r="3.7"></circle>
                                            <rect x="150.9" y="146.1" width="15.3" height="6.8"></rect>
                                            <rect class="w05" x="150.9" y="148" width="9.9" height="2.9"></rect>
                                            <path class="w2" d="M658.6,139.9h-74H323H152c-3.1,0-5.7,2.6-5.7,5.7v96c0,3.1,2.6,5.7,5.7,5.7h171h261.6h74c3.1,0,5.7-2.6,5.7-5.7v-96C664.3,142.5,661.7,139.9,658.6,139.9z"></path>
										</g>
                                        <g class="hatchways">
											<g class="hatchway">
												<rect x="261.3" y="165.4" width="32.7" height="56.5"></rect>
                                                <rect class="w05" x="265.5" y="169.8" width="24.2" height="47.7"></rect>
                                                <path class="w05" d="M273.9,196.7c0,1.1-0.8,2-1.9,2s-1.9-0.9-1.9-2v-6.3c0-1.1,0.8-2,1.9-2s1.9,0.9,1.9,2V196.7z"></path>
											</g>
                                            <g class="hatchway">
												<rect x="392.6" y="165.4" width="32.7" height="56.5"></rect>
                                                <rect class="w05" x="396.9" y="169.8" width="24.2" height="47.7"></rect>
                                                <path class="w05" d="M405.2,196.7c0,1.1-0.8,2-1.9,2s-1.9-0.9-1.9-2v-6.3c0-1.1,0.8-2,1.9-2s1.9,0.9,1.9,2V196.7z"></path>
											</g>
                                            <g class="hatchway">
												<rect x="524.3" y="165.4" width="32.7" height="56.5"></rect>
                                                <rect class="w05" x="528.5" y="169.8" width="24.2" height="47.7"></rect>
                                                <path class="w05" d="M536.9,196.7c0,1.1-0.8,2-1.9,2s-1.9-0.9-1.9-2v-6.3c0-1.1,0.8-2,1.9-2s1.9,0.9,1.9,2V196.7z"></path>
											</g>
										</g>
									</g>
                                    <g class="hover">
										<path class="id_11" d="M658.6,247.3c3.1,0,5.7-2.6,5.7-5.7v-96c0-3.1-2.6-5.7-5.7-5.7h-74v107.3H658.6z">
											<title>Передняя сторона крыши (габаритные огни, элементы кузова и т.д.)</title>
										</path>
                                        <rect class="id_12" x="323" y="139.9" width="261.6" height="107.3">
											<title>Средняя сторона крыши (габаритные огни, элементы кузова. люки и т.д.)</title>

                                            <path class="id_13" d="M152,139.9c-3.1,0-5.7,2.6-5.7,5.7v96c0,3.1,2.6,5.7,5.7,5.7h171V139.9H152z">
											<title>Задняя сторона крыши (габаритные огни, элементы кузова. люки и т.д.)</title>
										</path>
									</rect></g>
								</g>

                                <g class="back">
									<g class="selected">
										<path class="id_06" d="M125.9,148c-0.1,0-0.1,0-0.2,0v0h-6v-5.1c0-1.7-1.3-3-3-3h-100c-1.6,0-3,1.3-3,3v0.5H1.9L0,145.3v8.9l1.9,1.9h11.9v3H1.9L0,161v8.9l1.9,1.9h11.9v21.7h109.8v-23.9h-3.8v-18.8h6v0c0,0,0,0,0,0c0.1,0,0.1,0,0.2,0c0.8,0,1.4-0.6,1.4-1.4C127.4,148.6,126.7,148,125.9,148z"></path>
                                        <path class="id_05" d="M123.8,233.2V230h-4v-12.5h3.8v-23.9H13.8v21.7H1.9L0,217.2v8.9l1.9,1.9h11.9v3H1.9L0,233v8.9l1.9,1.9h11.9v0.4c0,1.7,1.4,3,3,3h100c1.7,0,3-1.3,3-3v-0.6h4v-3.1h1.4v-7.3H123.8z"></path>
									</g>
                                    <g class="path">
										<g class="body">
											<path class="w2" d="M119.8,244.2c0,1.6-1.3,3-3,3h-100c-1.6,0-3-1.4-3-3V142.9c0-1.6,1.4-3,3-3h100c1.7,0,3,1.4,3,3V244.2z"></path>
                                            <rect x="67.1" y="212.9" width="9" height="21.6"></rect>
                                            <rect x="67.1" y="152.6" width="9" height="21.6"></rect>
                                            <rect x="67.1" y="176.6" width="9" height="33.8"></rect>
                                            <rect x="109.4" y="185.9" width="6.3" height="15.3"></rect>
                                            <rect x="123.8" y="233.2" width="1.4" height="7.3"></rect>
                                            <rect x="119.8" y="230" width="4" height="13.6"></rect>
                                            <rect x="119.8" y="169.7" width="3.8" height="47.8"></rect>
                                            <circle cx="125.9" cy="149.4" r="1.4"></circle>
                                            <path d="M124.5,149.4c0-0.7,0.6-1.3,1.3-1.4v0h-6v2.9h6v0C125,150.8,124.5,150.2,124.5,149.4z"></path>
                                            <rect x="20.6" y="175.8" width="9" height="32.3"></rect>
                                            <polygon points="27.1,139.9 27.1,175.8 29.6,175.8 29.6,208.1 27.1,208.1 27.1,247.2 78.2,247.2 78.2,139.9"></polygon>
										</g>
                                        <rect class="window" x="84.1" y="152.8" width="20.5" height="81.6"></rect>
                                        <g class="wells">
											<polygon class="well" points="13.8,143.4 1.9,143.4 0,145.3 0,154.2 1.9,156.1 13.8,156.1"></polygon>
                                            <polygon class="well" points="13.8,159.1 1.9,159.1 0,161 0,170 1.9,171.9 13.8,171.9"></polygon>
                                            <polygon class="well" points="13.8,215.3 1.9,215.3 0,217.2 0,226.2 1.9,228.1 13.8,228.1"></polygon>
                                            <polygon class="well" points="13.8,231.1 1.9,231.1 0,233 0,241.9 1.9,243.8 13.8,243.8"></polygon>
										</g>
                                        <g class="lights">
											<circle class="light red" cx="34.6" cy="238.9" r="2.4"></circle>
                                            <circle class="light white" cx="41.1" cy="238.9" r="2.4"></circle>
                                            <circle class="light yellow" cx="47.6" cy="238.9" r="2.4"></circle>
                                            <circle class="light red" cx="54.1" cy="238.9" r="2.4"></circle>
                                            <circle class="light red" cx="34.6" cy="148.2" r="2.4"></circle>
                                            <circle class="light white" cx="41.1" cy="148.2" r="2.4"></circle>
                                            <circle class="light yellow" cx="47.6" cy="148.2" r="2.4"></circle>
                                            <circle class="light red" cx="54.1" cy="148.2" r="2.4"></circle>
                                            <circle class="light red" cx="106.6" cy="239.4" r="2.1"></circle>
                                            <circle class="light red" cx="113" cy="237.5" r="2.1"></circle>
                                            <circle class="light red" cx="106.6" cy="147.7" r="2.1"></circle>
                                            <circle class="light red" cx="113" cy="149.6" r="2.1"></circle>
										</g>
									</g>
                                    <g class="hover">
										<path d="M125.9,148c-0.1,0-0.1,0-0.2,0v0h-6v-5.1c0-1.7-1.3-3-3-3h-100c-1.6,0-3,1.3-3,3v0.5H1.9L0,145.3v8.9l1.9,1.9h11.9v3H1.9L0,161v8.9l1.9,1.9h11.9v21.7h109.8v-23.9h-3.8v-18.8h6v0c0,0,0,0,0,0c0.1,0,0.1,0,0.2,0c0.8,0,1.4-0.6,1.4-1.4C127.4,148.6,126.7,148,125.9,148z">
											<title>Левая задняя сторона (фары, стекло, бампер и т.д.)</title>
										</path>
                                        <path d="M123.8,233.2V230h-4v-12.5h3.8v-23.9H13.8v21.7H1.9L0,217.2v8.9l1.9,1.9h11.9v3H1.9L0,233v8.9l1.9,1.9h11.9v0.4c0,1.7,1.4,3,3,3h100c1.7,0,3-1.3,3-3v-0.6h4v-3.1h1.4v-7.3H123.8z">
											<title>Правая задняя сторона (фары, стекло, бампер и т.д.)</title>
										</path>
									</g>
								</g>

                                <g class="left">
									<g class="selected">
										<path class="id_09" d="M656.9,122.8c3.2,0,5.8-2.6,5.9-5.7l3.6-96c0.1-3.1-2.3-6.2-5.4-6.7l-0.7-0.1c-3.1-0.6-8.2-1-11.4-1h-64.3v109.7H656.9z"></path>
                                        <path class="id_08" d="M584.6,13.2h-6v2.3h-4.5C571,6.5,562.5,0,552.5,0c-10,0-18.6,6.5-21.6,15.5h-4.3v-2.3H323v109.7h69.6v4.5h32.7v-4.5h99v4.5h32.7v-4.5h27.6V13.2z"></path>
                                        <path class="id_07" d="M313.3,13.2v1.3h-4.6C305.4,6,297.1,0,287.5,0c-9.7,0-17.9,6-21.3,14.5h-4.9v-1.3h-58.8c-3.2,0-8.3,0.3-11.4,0.7l-42,5c-3.1,0.4-5.6,3.3-5.5,6.4l2.5,91.9c0.1,3.2,2.7,5.7,5.9,5.7h6.3l-2.3,0c0,0-0.1,2.5-1.3,2.5c-2.4,0-3.9,0-3.9,0v4.3h6.9c0,0,3,0.3,3-3c0-2.8,0-3.6,0-3.8h100.5v4.5h32.7v-4.5H323V13.2H313.3z"></path>
									</g>
                                    <g class="path">
										<g class="body">
											<path class="w2" d="M662.8,117.1c-0.1,3.1-2.8,5.7-5.9,5.7H152c-3.2,0-5.8-2.6-5.9-5.7l-2.5-91.9c-0.1-3.2,2.4-6,5.5-6.4l42-5c3.1-0.4,8.3-0.7,11.4-0.7h58.8v11.5c0,13.2,10.8,24,24,24h4c13.2,0,24-10.8,24-24V13.2h213.3v11.5c0,13.2,10.8,24,24,24h4c13.2,0,24-10.8,24-24V13.2h70.4c3.2,0,8.3,0.5,11.4,1l0.7,0.1c3.1,0.6,5.5,3.6,5.4,6.7L662.8,117.1z"></path>
                                            <polygon points="143.8,30.3 148.5,34.8 148.6,78.4 145.2,81.2"></polygon>
                                            <rect x="261.3" y="122.8" width="32.7" height="4.5"></rect>
                                            <rect x="392.6" y="122.8" width="32.7" height="4.5"></rect>
                                            <rect x="524.3" y="122.8" width="32.7" height="4.5"></rect>
                                            <path d="M666.1,29.2l-0.4,10.9h-13c0,0,1.7-11.2,8.7-11C663.1,29.2,664.7,29.2,666.1,29.2z"></path>
                                            <rect x="336.8" y="27.3" width="8.3" height="8.9"></rect>
                                            <path d="M248.6,13.2h-46.1c-0.8,0-1.7,0-2.7,0.1v13.3h48.8V13.2z"></path>
                                            <path d="M156,122.9c0,0-0.1,2.5-1.3,2.5c-2.4,0-3.9,0-3.9,0v4.3h6.9c0,0,3,0.3,3-3s-0.1-3.8-0.1-3.8L156,122.9z"></path>
										</g>
                                        <g class="windows">
											<rect class="window" x="325.2" y="61.8" width="62.5" height="48"></rect>
                                            <rect class="window" x="192.7" y="61.8" width="62.8" height="48"></rect>
                                            <g class="window">
												<rect x="257.4" y="61.8" width="65.6" height="48"></rect>
                                                <line x1="323" y1="94.3" x2="257.4" y2="94.3"></line>
                                                <rect x="259" y="95.7" class="w05" width="62.5" height="12.2"></rect>
											</g>
                                            <g class="window">
												<rect x="389.7" y="61.8" width="65.5" height="48"></rect>
                                                <line x1="389.7" y1="94.3" x2="455.2" y2="94.3"></line>
                                                <rect x="391" y="95.7" class="w05" width="62.5" height="12.2"></rect>
											</g>
                                            <g class="window">
												<rect x="457.5" y="61.8" width="61.3" height="48"></rect>
                                                <rect x="518.8" y="61.8" width="65.5" height="48"></rect>
                                                <line x1="518.8" y1="94.3" x2="584.3" y2="94.3"></line>
                                                <rect x="520.2" y="95.7" class="w05" width="62.5" height="12.2"></rect>
											</g>
                                            <g class="window">
												<polygon points="586.6,61.8 650.3,51.4 650.3,109.8 586.6,109.8"></polygon>
                                                <line x1="650.4" y1="95.4" x2="586.6" y2="95.4"></line>
                                                <line x1="586.6" y1="67.7" x2="650.4" y2="67.7"></line>
                                                <rect x="587.9" y="69.4" class="w05" width="60.9" height="24.7"></rect>
											</g>
                                            <polygon class="window" points="663.1,109.8 652.3,109.8 652.3,51.2 665.3,51.2"></polygon>
										</g>
                                        <g class="wells">
											<g class="well">
												<path d="M552.5,0c-12.6,0-22.8,10.2-22.8,22.8c0,12.6,10.2,22.8,22.8,22.8c12.6,0,22.8-10.2,22.8-22.8C575.3,10.2,565.1,0,552.5,0z M552.5,35.8c-7.2,0-13-5.8-13-13c0-7.2,5.8-13,13-13s13,5.8,13,13C565.5,30,559.6,35.8,552.5,35.8z"></path>
                                                <circle cx="552.5" cy="22.8" r="2.7"></circle>
                                                <circle cx="552.5" cy="22.8" r="6.3"></circle>
                                                <circle cx="552.5" cy="22.8" r="9.5"></circle>
                                                <circle cx="552.5" cy="14.9" r="0.6"></circle>
                                                <circle cx="547.8" cy="16.4" r="0.6"></circle>
                                                <circle cx="544.9" cy="20.4" r="0.6"></circle>
                                                <circle cx="544.9" cy="25.3" r="0.6"></circle>
                                                <circle cx="547.8" cy="29.2" r="0.6"></circle>
                                                <circle cx="552.5" cy="30.8" r="0.6"></circle>
                                                <circle cx="557.1" cy="29.2" r="0.6"></circle>
                                                <circle cx="560" cy="25.3" r="0.6"></circle>
                                                <circle cx="560" cy="20.4" r="0.6"></circle>
                                                <circle cx="557.1" cy="16.4" r="0.6"></circle>
											</g>
                                            <g class="well">
												<path d="M287.5,0c-12.6,0-22.8,10.2-22.8,22.8c0,12.6,10.2,22.8,22.8,22.8c12.6,0,22.8-10.2,22.8-22.8C310.3,10.2,300.1,0,287.5,0z M287.5,35.8c-7.2,0-13-5.8-13-13c0-7.2,5.8-13,13-13s13,5.8,13,13C300.5,30,294.6,35.8,287.5,35.8z"></path>
                                                <circle cx="287.5" cy="22.8" r="2.7"></circle>
                                                <circle cx="287.5" cy="22.8" r="6.3"></circle>
                                                <circle cx="287.5" cy="22.8" r="9.5"></circle>
                                                <circle cx="287.5" cy="14.9" r="0.6"></circle>
                                                <circle cx="282.8" cy="16.4" r="0.6"></circle>
                                                <circle cx="279.9" cy="20.4" r="0.6"></circle>
                                                <circle cx="279.9" cy="25.3" r="0.6"></circle>
                                                <circle cx="282.8" cy="29.2" r="0.6"></circle>
                                                <circle cx="287.5" cy="30.8" r="0.6"></circle>
                                                <circle cx="292.1" cy="29.2" r="0.6"></circle>
                                                <circle cx="295" cy="25.3" r="0.6"></circle>
                                                <circle cx="295" cy="20.4" r="0.6"></circle>
                                                <circle cx="292.1" cy="16.4" r="0.6"></circle>
											</g>
										</g>
									</g>
                                    <g class="hover">
										<path d="M656.9,122.8c3.2,0,5.8-2.6,5.9-5.7l3.6-96c0.1-3.1-2.3-6.2-5.4-6.7l-0.7-0.1c-3.1-0.6-8.2-1-11.4-1h-64.3v109.7H656.9z">
											<title>Левая боковая (передняя) сторона (дверь, стекло, элементы кузова, колеса и т.д.)</title>
										</path>
                                        <path d="M584.6,13.2h-6v2.3h-4.5C571,6.5,562.5,0,552.5,0c-10,0-18.6,6.5-21.6,15.5h-4.3v-2.3H323v109.7h69.6v4.5h32.7v-4.5h99v4.5h32.7v-4.5h27.6V13.2z">
											<title>Левая боковая (средняя) сторона (стекло, элементы кузова, колеса и т.д.)</title>
										</path>
                                        <path d="M313.3,13.2v1.3h-4.6C305.4,6,297.1,0,287.5,0c-9.7,0-17.9,6-21.3,14.5h-4.9v-1.3h-58.8c-3.2,0-8.3,0.3-11.4,0.7l-42,5c-3.1,0.4-5.6,3.3-5.5,6.4l2.5,91.9c0.1,3.2,2.7,5.7,5.9,5.7h6.3l-2.3,0c0,0-0.1,2.5-1.3,2.5c-2.4,0-3.9,0-3.9,0v4.3h6.9c0,0,3,0.3,3-3c0-2.8,0-3.6,0-3.8h100.5v4.5h32.7v-4.5H323V13.2H313.3z">
											<title>Левая боковая (задняя) сторона (стекло, элементы кузова, колесо и т.д.)</title>
										</path>
									</g>
								</g>

                                <g id="dashed">
									<line class="dashdot" x1="323" y1="13.2" x2="323" y2="122.8"></line>
                                    <line class="dashdot" x1="584.3" y1="13.2" x2="584.3" y2="122.8"></line>
                                    <line class="dashdot" x1="323" y1="267.4" x2="323" y2="377.1"></line>
                                    <line class="dashdot" x1="584.3" y1="267.4" x2="584.3" y2="377.1"></line>
                                    <line class="dashdot" x1="323" y1="140.4" x2="323" y2="248.4"></line>
                                    <line class="dashdot" x1="584.3" y1="140.4" x2="584.3" y2="248.4"></line>
                                    <line class="dashdot" x1="683.9" y1="193.6" x2="788.1" y2="193.6"></line>
                                    <line class="dashdot" x1="14.6" y1="193.6" x2="118.8" y2="193.6"></line>
								</g>
							</g>
						</svg>
    """
    return file_svg