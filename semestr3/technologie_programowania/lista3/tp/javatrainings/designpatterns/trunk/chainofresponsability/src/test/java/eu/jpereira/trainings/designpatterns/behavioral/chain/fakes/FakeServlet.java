/**
 * Copyright 2011 Joao Miguel Pereira
 *
 *  Licensed under the Apache License, Version 2.0 (the "License");
 *  you may not use this file except in compliance with the License.
 *  You may obtain a copy of the License at
 *
 *      http://www.apache.org/licenses/LICENSE-2.0
 *
 *  Unless required by applicable law or agreed to in writing, software
 *  distributed under the License is distributed on an "AS IS" BASIS,
 *  WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
 *  See the License for the specific language governing permissions and
 *  limitations under the License.
 */
package eu.jpereira.trainings.designpatterns.behavioral.chain.fakes;

import java.io.File;
import java.io.IOException;
import java.util.ArrayList;
import java.util.Arrays;
import java.util.List;
import java.util.Queue;

import javax.servlet.*;

/**
 * @author jpereira
 * 
 */
public class FakeServlet implements Servlet {

	private Queue<Filter> filters;
	private String temp;
	private String filterType;
	private String[] table;

	/*
	 * (non-Javadoc)
	 * 
	 * @see javax.servlet.Servlet#init(javax.servlet.ServletConfig)
	 */
	@Override
	public void init(ServletConfig config) throws ServletException {
		// TODO Auto-generated method stub

	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see javax.servlet.Servlet#getServletConfig()
	 */
	@Override
	public ServletConfig getServletConfig() {
		// TODO Auto-generated method stub
		return null;
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see javax.servlet.Servlet#service(javax.servlet.ServletRequest,
	 * javax.servlet.ServletResponse)
	 */
	@Override
	public void service(ServletRequest req, ServletResponse res) throws ServletException, IOException {
		this.filters = FakeFilterChain.getFilters();

		String name = req.getAttribute("name").toString();
		String out = "Hello " + name;


		for(Filter filter : filters){
			filterType = filter.toString().split("\\.")[7].split("@")[0];
			if(filterType.equals("FakeFormatFilter")){
				temp = out + " :Formated";
				out = temp;
			}
			else if(filterType.equals("FakeLoggingFilter")){
				temp = "Logging: " + out;
				out = temp;
			}
			else{
				if(out.contains("Logging:")){
					table = out.split(":");
					out = "";

					for(String tab : table){
						if(tab.equals("Logging")){
							out+= tab +": Authorized:";
						}
						else
							out += tab;

					}
				}
				else {
					temp = "Authorized: " + out;
					out = temp;
				}
			}
		}

		res.getOutputStream().print(out);

	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see javax.servlet.Servlet#getServletInfo()
	 */
	@Override
	public String getServletInfo() {
		// TODO Auto-generated method stub
		return null;
	}

	/*
	 * (non-Javadoc)
	 * 
	 * @see javax.servlet.Servlet#destroy()
	 */
	@Override
	public void destroy() {
		// TODO Auto-generated method stub

	}

}
