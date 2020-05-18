import javax.swing.*;
import java.awt.*;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;

public class GUI {
    public static void main(String [] args) {
        SwingUtilities.invokeLater(new Runnable() {
            @Override
            public void run() {
                MakeGUI();
            }
        });
    }

    public static void MakeGUI(){


        JFrame frame = new JFrame();
        JPanel panelFirst = new JPanel();
        JPanel panelSecond = new JPanel();
        JButton buttonWypisz = new JButton("Wypisz");
        JLabel informLabel = new JLabel("Podaj dane: ");
        JTextField dataTextField = new JTextField(15);

        buttonWypisz.addActionListener(new ActionListener() {
            @Override
            public void actionPerformed(ActionEvent e) {
                try{
                    Process pro = Runtime.getRuntime().exec("C:\\Users\\piotr\\OneDrive\\Pulpit\\KP\\WiP-2\\Lista2\\WierszTrojkataPascala.exe " + dataTextField.getText());
                    StringBuilder processOutput = new StringBuilder();
                    try(BufferedReader processOutputReader = new BufferedReader(
                        new InputStreamReader(pro.getInputStream())))
                    {

                        String readLine;
                        int ileWiersz = 0;

                        while((readLine = processOutputReader.readLine()) != null) {

                            JLabel outputLabel = new JLabel();
                            outputLabel.setText(readLine);
                            panelSecond.add(outputLabel);
                            processOutput.append(readLine + System.lineSeparator());
                            ileWiersz++;
                        }
                        panelSecond.setLayout(new GridLayout(ileWiersz,1));
                        pro.destroy();
                        frame.remove(panelFirst);
                        frame.add(panelSecond);
                        frame.pack();

                    }
                } catch (IOException e1) {
                    e1.printStackTrace();
                }
            }
        });

        frame.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
        frame.add(panelFirst);
        panelFirst.add(informLabel);
        panelFirst.add(dataTextField);
        panelFirst.add(buttonWypisz);

        frame.pack();
        frame.setLocationRelativeTo(null);
        frame.setVisible(true);

    }
}
