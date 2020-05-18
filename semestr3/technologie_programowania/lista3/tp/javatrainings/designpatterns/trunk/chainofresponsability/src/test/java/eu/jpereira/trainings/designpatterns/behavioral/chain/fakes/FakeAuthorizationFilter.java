package eu.jpereira.trainings.designpatterns.behavioral.chain.fakes;

import eu.jpereira.trainings.designpatterns.behavioral.chain.filter.AbstractFilter;

import javax.servlet.FilterChain;
import javax.servlet.ServletException;
import javax.servlet.ServletRequest;
import javax.servlet.ServletResponse;
import java.io.IOException;

public class FakeAuthorizationFilter extends AbstractFilter {
    @Override
    public void doFilter(ServletRequest request, ServletResponse response, FilterChain chain) throws IOException, ServletException {
        super.doFilter(request, response, chain);
    }

}
