/*
 * Click nbfs://nbhost/SystemFileSystem/Templates/Licenses/license-default.txt to change this license
 * Click nbfs://nbhost/SystemFileSystem/Templates/GUIForms/JFrame.java to edit this template
 */
package com.mycompany.prog_exer1;

import java.awt.Color;
import javax.swing.JOptionPane;



/**
 *
 * @author jofel
 */
public class Customers extends javax.swing.JFrame {

    /**
     * Creates new form Customers
     */
    public Customers() {
        initComponents();
    }

    /**
     * This method is called from within the constructor to initialize the form.
     * WARNING: Do NOT modify this code. The content of this method is always
     * regenerated by the Form Editor.
     */
    @SuppressWarnings("unchecked")
    // <editor-fold defaultstate="collapsed" desc="Generated Code">//GEN-BEGIN:initComponents
    private void initComponents() {

        jLabel1 = new javax.swing.JLabel();
        jLabel2 = new javax.swing.JLabel();
        jLabel3 = new javax.swing.JLabel();
        jLabel4 = new javax.swing.JLabel();
        jLabel5 = new javax.swing.JLabel();
        jLabel6 = new javax.swing.JLabel();
        jScrollPane1 = new javax.swing.JScrollPane();
        custID = new javax.swing.JTextPane();
        jScrollPane2 = new javax.swing.JScrollPane();
        custName = new javax.swing.JTextPane();
        jScrollPane3 = new javax.swing.JScrollPane();
        custAddress = new javax.swing.JTextPane();
        jScrollPane4 = new javax.swing.JScrollPane();
        custPhone = new javax.swing.JTextPane();
        jScrollPane5 = new javax.swing.JScrollPane();
        custEmail = new javax.swing.JTextPane();
        jScrollPane6 = new javax.swing.JScrollPane();
        custBday = new javax.swing.JTextPane();
        jLabel7 = new javax.swing.JLabel();
        emLabel = new javax.swing.JLabel();
        saveB = new javax.swing.JButton();
        jLabel8 = new javax.swing.JLabel();
        jScrollPane7 = new javax.swing.JScrollPane();
        custGender = new javax.swing.JTextPane();
        jLabel9 = new javax.swing.JLabel();
        bdLabel = new javax.swing.JLabel();
        pLabel = new javax.swing.JLabel();
        nLabel = new javax.swing.JLabel();
        jLabel10 = new javax.swing.JLabel();
        jMenuBar1 = new javax.swing.JMenuBar();
        jMenu1 = new javax.swing.JMenu();
        jMenuItem1 = new javax.swing.JMenuItem();

        setDefaultCloseOperation(javax.swing.WindowConstants.EXIT_ON_CLOSE);

        jLabel1.setText("ID:");

        jLabel2.setText("Name:");

        jLabel3.setText("Address:");

        jLabel4.setText("Phone:");

        jLabel5.setText("Email:");

        jLabel6.setText("Birthday:");

        jScrollPane1.setViewportView(custID);

        custName.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyReleased(java.awt.event.KeyEvent evt) {
                custNameKeyReleased(evt);
            }
        });
        jScrollPane2.setViewportView(custName);

        jScrollPane3.setViewportView(custAddress);

        custPhone.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyReleased(java.awt.event.KeyEvent evt) {
                custPhoneKeyReleased(evt);
            }
        });
        jScrollPane4.setViewportView(custPhone);

        custEmail.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyReleased(java.awt.event.KeyEvent evt) {
                custEmailKeyReleased(evt);
            }
        });
        jScrollPane5.setViewportView(custEmail);

        custBday.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyReleased(java.awt.event.KeyEvent evt) {
                custBdayKeyReleased(evt);
            }
        });
        jScrollPane6.setViewportView(custBday);

        emLabel.setText("( ex. pat@gmail.com )");

        saveB.setText("Save");
        saveB.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                saveBActionPerformed(evt);
            }
        });

        jLabel8.setText("Gender:");

        jScrollPane7.setViewportView(custGender);

        bdLabel.setText("( mm/dd/yyyy )");

        pLabel.setText("( 09**-******* )");

        nLabel.setText("( Last name, First name MI )");
        nLabel.addKeyListener(new java.awt.event.KeyAdapter() {
            public void keyReleased(java.awt.event.KeyEvent evt) {
                nLabelKeyReleased(evt);
            }
        });

        jLabel10.setFont(new java.awt.Font("Bahnschrift", 1, 24)); // NOI18N
        jLabel10.setText("Customer Information");

        jMenu1.setText("File");

        jMenuItem1.setText("Products");
        jMenuItem1.addActionListener(new java.awt.event.ActionListener() {
            public void actionPerformed(java.awt.event.ActionEvent evt) {
                jMenuItem1ActionPerformed(evt);
            }
        });
        jMenu1.add(jMenuItem1);

        jMenuBar1.add(jMenu1);

        setJMenuBar(jMenuBar1);

        javax.swing.GroupLayout layout = new javax.swing.GroupLayout(getContentPane());
        getContentPane().setLayout(layout);
        layout.setHorizontalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(431, 431, 431)
                .addComponent(jLabel9, javax.swing.GroupLayout.PREFERRED_SIZE, 37, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel7, javax.swing.GroupLayout.PREFERRED_SIZE, 58, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE))
            .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                .addContainerGap(javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(jLabel1, javax.swing.GroupLayout.PREFERRED_SIZE, 37, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jLabel2, javax.swing.GroupLayout.PREFERRED_SIZE, 37, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jLabel3, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jLabel6, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jLabel4, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                            .addComponent(jLabel5, javax.swing.GroupLayout.PREFERRED_SIZE, 37, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(jLabel8, javax.swing.GroupLayout.PREFERRED_SIZE, 58, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(33, 33, 33)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                            .addComponent(jScrollPane1)
                            .addComponent(jScrollPane2)
                            .addComponent(jScrollPane3)
                            .addComponent(jScrollPane4)
                            .addComponent(jScrollPane5)
                            .addComponent(jScrollPane6)
                            .addComponent(jScrollPane7, javax.swing.GroupLayout.PREFERRED_SIZE, 128, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(12, 12, 12)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(pLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 83, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING, false)
                                .addComponent(emLabel, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                                .addGroup(layout.createSequentialGroup()
                                    .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                                        .addComponent(saveB)
                                        .addComponent(bdLabel, javax.swing.GroupLayout.PREFERRED_SIZE, 91, javax.swing.GroupLayout.PREFERRED_SIZE))
                                    .addGap(43, 43, 43)))
                            .addComponent(nLabel))
                        .addGap(66, 66, 66))
                    .addGroup(javax.swing.GroupLayout.Alignment.TRAILING, layout.createSequentialGroup()
                        .addComponent(jLabel10, javax.swing.GroupLayout.PREFERRED_SIZE, 261, javax.swing.GroupLayout.PREFERRED_SIZE)
                        .addGap(133, 133, 133))))
        );
        layout.setVerticalGroup(
            layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
            .addGroup(layout.createSequentialGroup()
                .addGap(10, 10, 10)
                .addComponent(jLabel7)
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED)
                .addComponent(jLabel9)
                .addGap(12, 12, 12)
                .addComponent(jLabel10, javax.swing.GroupLayout.PREFERRED_SIZE, 33, javax.swing.GroupLayout.PREFERRED_SIZE)
                .addGap(18, 18, 18)
                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.TRAILING)
                    .addComponent(jScrollPane7, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                    .addGroup(layout.createSequentialGroup()
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel1)
                            .addComponent(jScrollPane1, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel2)
                            .addComponent(jScrollPane2, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                            .addComponent(nLabel))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addComponent(jLabel3)
                            .addComponent(jScrollPane3, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                        .addGap(18, 18, 18)
                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                            .addGroup(layout.createSequentialGroup()
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel4)
                                    .addComponent(jScrollPane4, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                                .addGap(18, 18, 18)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addComponent(jLabel5)
                                    .addComponent(jScrollPane5, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE)
                                    .addComponent(emLabel))
                                .addGap(18, 18, 18)
                                .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                    .addGroup(layout.createSequentialGroup()
                                        .addGroup(layout.createParallelGroup(javax.swing.GroupLayout.Alignment.LEADING)
                                            .addComponent(jLabel6)
                                            .addComponent(jScrollPane6, javax.swing.GroupLayout.PREFERRED_SIZE, javax.swing.GroupLayout.DEFAULT_SIZE, javax.swing.GroupLayout.PREFERRED_SIZE))
                                        .addGap(18, 18, 18)
                                        .addComponent(jLabel8))
                                    .addComponent(bdLabel)))
                            .addComponent(pLabel))))
                .addPreferredGap(javax.swing.LayoutStyle.ComponentPlacement.RELATED, javax.swing.GroupLayout.DEFAULT_SIZE, Short.MAX_VALUE)
                .addComponent(saveB)
                .addGap(35, 35, 35))
        );

        pack();
    }// </editor-fold>//GEN-END:initComponents

    private void custEmailKeyReleased(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_custEmailKeyReleased
     String email = custEmail.getText().trim();  
boolean isValid = false;

if (email.isEmpty()) {
    emLabel.setText("( ex. pat@gmail.com )");
    emLabel.setForeground(Color.black);  
} else {
    
    int atIndex = email.indexOf('@');
    int dotIndex = email.indexOf(".com");
    
    if (email.length() > 1 && atIndex > 0 && dotIndex > (atIndex + 3) && dotIndex == email.length() - 4) {
        isValid = true;
    }

    if (isValid) {
        emLabel.setForeground(Color.green);
        emLabel.setText("Valid Email");
    } else {
        emLabel.setForeground(Color.red);
        emLabel.setText("Invalid Email");
    }
}

    }//GEN-LAST:event_custEmailKeyReleased

    private void saveBActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_saveBActionPerformed
        
    if (custID.getText().isEmpty() || 
        custName.getText().isEmpty() || 
        custAddress.getText().isEmpty() || 
        custPhone.getText().isEmpty() || 
        custEmail.getText().isEmpty() || 
        custBday.getText().isEmpty() || 
        custGender.getText().isEmpty()) {

      
        JOptionPane.showMessageDialog(this, "Fill all the empty boxes", "Error", JOptionPane.ERROR_MESSAGE);
    } else {
        
        if (nLabel.getForeground().equals(Color.RED) || 
            pLabel.getForeground().equals(Color.RED) || 
            emLabel.getForeground().equals(Color.RED) || 
            bdLabel.getForeground().equals(Color.RED)) {

           
            JOptionPane.showMessageDialog(this, "Cannot save. Data is invalid.", "Error", JOptionPane.ERROR_MESSAGE);
        } else {
           
            JOptionPane.showMessageDialog(this, "File saved successfully!", "Save", JOptionPane.INFORMATION_MESSAGE);
        }
    }
    }//GEN-LAST:event_saveBActionPerformed




    
    private void custBdayKeyReleased(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_custBdayKeyReleased
     String bDay = custBday.getText().trim();
     boolean isValid = false;
     
     if (bDay.isEmpty()) {
    bdLabel.setText("( mm/dd/yyyy )");
    bdLabel.setForeground(Color.black);  
} else {

    String dateFormatRegex = "^\\d{2}/\\d{2}/\\d{4}$";
    isValid = bDay.matches(dateFormatRegex);

    if (isValid) {
        bdLabel.setForeground(Color.green);
        bdLabel.setText("Valid Date");
    } else {
        bdLabel.setForeground(Color.red);
        bdLabel.setText("Invalid Date");
    }
}
    }//GEN-LAST:event_custBdayKeyReleased

    private void custPhoneKeyReleased(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_custPhoneKeyReleased
    String phoneN = custPhone.getText().trim();
    boolean isValid = false;
    if (phoneN.isEmpty()) {
        pLabel.setForeground(Color.black);
        pLabel.setText("Ex. 0912-1234567");
    } else {
    String phoneFormatRegex = "^\\d{4}-\\d{7}$";
    isValid = phoneN.matches(phoneFormatRegex);

    if (isValid) {
        pLabel.setForeground(Color.green);
        pLabel.setText("Valid Phone Number");
    } else {
        pLabel.setForeground(Color.red);
        pLabel.setText("Invalid Phone Number");
    }
}
    }//GEN-LAST:event_custPhoneKeyReleased

    private void custNameKeyReleased(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_custNameKeyReleased
        String namestr = custName.getText().trim();
        boolean isValid = false;
        
        if (namestr.isEmpty()) {
            nLabel.setForeground(Color.black);
            nLabel.setText("( Last name, First name, MI )");
        }
        
        else {
            String nameFormatRegex = "[A-Za-z]+( [A-Za-z]+)*, [A-Za-z]+( [A-Za-z]+)*( [A-Za-z]+\\.)"
;

            isValid = namestr.matches(nameFormatRegex);
            
            if (isValid) {
                nLabel.setText("Valid Full Name");
                nLabel.setForeground(Color.green);           
            }
            else {
                nLabel.setForeground(Color.red);
                nLabel.setText("Invalid Full Name");
            }
        }    
        
    }//GEN-LAST:event_custNameKeyReleased

    private void nLabelKeyReleased(java.awt.event.KeyEvent evt) {//GEN-FIRST:event_nLabelKeyReleased
        // TODO add your handling code here:
    }//GEN-LAST:event_nLabelKeyReleased

    private void jMenuItem1ActionPerformed(java.awt.event.ActionEvent evt) {//GEN-FIRST:event_jMenuItem1ActionPerformed
        Products abc = new Products();
        abc.setVisible(true);        // TODO add your handling code here:
    }//GEN-LAST:event_jMenuItem1ActionPerformed

    /**
     * @param args the command line arguments
     */
    public static void main(String args[]) {
        /* Set the Nimbus look and feel */
        //<editor-fold defaultstate="collapsed" desc=" Look and feel setting code (optional) ">
        /* If Nimbus (introduced in Java SE 6) is not available, stay with the default look and feel.
         * For details see http://download.oracle.com/javase/tutorial/uiswing/lookandfeel/plaf.html 
         */
        try {
            for (javax.swing.UIManager.LookAndFeelInfo info : javax.swing.UIManager.getInstalledLookAndFeels()) {
                if ("Nimbus".equals(info.getName())) {
                    javax.swing.UIManager.setLookAndFeel(info.getClassName());
                    break;
                }
            }
        } catch (ClassNotFoundException ex) {
            java.util.logging.Logger.getLogger(Customers.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (InstantiationException ex) {
            java.util.logging.Logger.getLogger(Customers.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (IllegalAccessException ex) {
            java.util.logging.Logger.getLogger(Customers.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        } catch (javax.swing.UnsupportedLookAndFeelException ex) {
            java.util.logging.Logger.getLogger(Customers.class.getName()).log(java.util.logging.Level.SEVERE, null, ex);
        }
        //</editor-fold>

        /* Create and display the form */
        java.awt.EventQueue.invokeLater(new Runnable() {
            public void run() {
                new Customers().setVisible(true);
            }
        });
    }

    // Variables declaration - do not modify//GEN-BEGIN:variables
    private javax.swing.JLabel bdLabel;
    private javax.swing.JTextPane custAddress;
    private javax.swing.JTextPane custBday;
    private javax.swing.JTextPane custEmail;
    private javax.swing.JTextPane custGender;
    private javax.swing.JTextPane custID;
    private javax.swing.JTextPane custName;
    private javax.swing.JTextPane custPhone;
    private javax.swing.JLabel emLabel;
    private javax.swing.JLabel jLabel1;
    private javax.swing.JLabel jLabel10;
    private javax.swing.JLabel jLabel2;
    private javax.swing.JLabel jLabel3;
    private javax.swing.JLabel jLabel4;
    private javax.swing.JLabel jLabel5;
    private javax.swing.JLabel jLabel6;
    private javax.swing.JLabel jLabel7;
    private javax.swing.JLabel jLabel8;
    private javax.swing.JLabel jLabel9;
    private javax.swing.JMenu jMenu1;
    private javax.swing.JMenuBar jMenuBar1;
    private javax.swing.JMenuItem jMenuItem1;
    private javax.swing.JScrollPane jScrollPane1;
    private javax.swing.JScrollPane jScrollPane2;
    private javax.swing.JScrollPane jScrollPane3;
    private javax.swing.JScrollPane jScrollPane4;
    private javax.swing.JScrollPane jScrollPane5;
    private javax.swing.JScrollPane jScrollPane6;
    private javax.swing.JScrollPane jScrollPane7;
    private javax.swing.JLabel nLabel;
    private javax.swing.JLabel pLabel;
    private javax.swing.JButton saveB;
    // End of variables declaration//GEN-END:variables

    private boolean custBdayKeyReleased() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }

    private boolean custPhoneKeyReleased() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }

    private boolean custNameKeyReleased() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }

    private boolean isValidCustomerName() {
        throw new UnsupportedOperationException("Not supported yet."); // Generated from nbfs://nbhost/SystemFileSystem/Templates/Classes/Code/GeneratedMethodBody
    }
}
