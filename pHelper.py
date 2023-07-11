import tkinter as tk
import tkinter.ttk as ttk
from PIL import ImageTk, Image
import numpy as np

ph_val = ""
poh_val = ""
h_molarity_val = ""
oh_molarity_val = ""
salt_molarity_val = ""
ka_val = ""
kb_val = ""
pka_val = ""
pkb_val = ""


# Variables
def get_variable(*args):
    global ph_val
    ph_val = ph.get()
    ph_val = ph_val.replace("^", "**")
    try:
        ph_val = str(eval(ph_val))
    except:
        ph_val = str("")
    global poh_val
    poh_val = poh.get()
    poh_val = poh_val.replace("^", "**")
    try:
        poh_val = str(eval(poh_val))
    except:
        poh_val = str("")
    global h_molarity_val
    h_molarity_val = h_molarity.get()
    h_molarity_val = h_molarity_val.replace("^", "**")
    try:
        h_molarity_val = str(eval(h_molarity_val))
    except:
        h_molarity_val = str("")
    global oh_molarity_val
    oh_molarity_val = oh_molarity.get()
    oh_molarity_val = oh_molarity_val.replace("^", "**")
    try:
        oh_molarity_val = str(eval(oh_molarity_val))
    except:
        oh_molarity_val = str("")
    global salt_molarity_val
    salt_molarity_val = salt_molarity.get()
    salt_molarity_val = salt_molarity_val.replace("^", "**")
    try:
        salt_molarity_val = str(eval(salt_molarity_val))
    except:
        salt_molarity_val = str("")
    global ka_val
    ka_val = ka.get()
    ka_val = ka_val.replace("^", "**")
    try:
        ka_val = str(eval(ka_val))
    except:
        ka_val = str("")
    global kb_val
    kb_val = kb.get()
    kb_val = kb_val.replace("^", "**")
    try:
        kb_val = str(eval(kb_val))
    except:
        kb_val = str("")
    global pka_val
    pka_val = pka.get()
    pka_val = pka_val.replace("^", "**")
    try:
        pka_val = str(eval(pka_val))
    except:
        pka_val = str("")
    global pkb_val
    pkb_val = pkb.get()
    pkb_val = pkb_val.replace("^", "**")
    try:
        pkb_val = str(eval(pkb_val))
    except:
        pkb_val = str("")


# Calculation
def ph_calculation(*args):
    global ph_val
    ph_val = ""
    global poh_val
    poh_val = ""
    global h_molarity_val
    h_molarity_val = ""
    global oh_molarity_val
    oh_molarity_val = ""
    global salt_molarity_val
    salt_molarity_val = ""
    global ka_val
    ka_val = ""
    global kb_val
    kb_val = ""
    global pka_val
    pka_val = ""
    global pkb_val
    pkb_val = ""
    get_variable()
    ph_res = ""
    if sol_type.get() == "Strong Acid and Base Solution":
        try:
            ph_res = str(eval(ph_val))
        except:
            if h_molarity_val != "":
                ph_res = str(eval("-np.log10(" + h_molarity_val + ")"))
            elif oh_molarity_val != "":
                ph_res = str(eval("14+np.log10(" + oh_molarity_val + ")"))
            elif poh_val != "":
                ph_res = str(eval("14-" + poh_val))
            else:
                ph_res = str("Error")
        finally:
            if ph_i.get() == 1:
                if "e-0" in ph_res:
                    ph_res = ph_res.replace("e-0", "*10^(") + ")"
                elif "e" in ph_res:
                    ph_res = ph_res.replace("e", "*10^(-") + ")"
                ph_dis.config(text="pH = " + ph_res)
                ph_dis.grid(row=1, column=0, pady=10)
            else:
                ph_dis.grid_forget()
    elif sol_type.get() == "Weak Base and Strong Acid Salt Hydrolysis" or sol_type.get() == "Weak Acid and Strong " \
                                                                                            "Base Salt Hydrolysis":
        try:
            ph_res = str(eval(ph_val))
        except:
            if salt_molarity_val != "" and kb_val != "":
                ph_res = str(eval("-np.log10(np.sqrt(((10**(-14))*" + salt_molarity_val + ")/" + kb_val + "))"))
            elif salt_molarity_val != "" and ka_val != "":
                ph_res = str(eval("14+np.log10(np.sqrt(((10**(-14))*" + salt_molarity_val + ")/" + ka_val + "))"))
            elif salt_molarity_val != "" and pkb_val != "":
                ph_res = str(eval("-np.log10(np.sqrt(((10**(-14))*" + salt_molarity_val + ")/10**(" + pkb_val + ")))"))
            elif salt_molarity_val != "" and pka_val != "":
                ph_res = str(
                    eval("14+np.log10(np.sqrt(((10**(-14))*" + salt_molarity_val + ")/10**(" + pka_val + ")))"))
            elif poh_val != "":
                ph_res = str(eval("14-" + poh_val))
            else:
                ph_res = str("Error")
        finally:
            if ph_i.get() == 1:
                if "e-0" in ph_res:
                    ph_res = ph_res.replace("e-0", "*10^(") + ")"
                elif "e" in ph_res:
                    ph_res = ph_res.replace("e", "*10^(-") + ")"
                ph_dis.config(text="pH = " + ph_res)
                ph_dis.grid(row=1, column=0, pady=10)
            else:
                ph_dis.grid_forget()
    elif sol_type.get() == "Weak Acid and Base Salt Hydrolysis":
        try:
            ph_res = str(eval(ph_val))
        except:
            if kb_val != "" and ka_val != "" and kb_val > ka_val:
                ph_res = str(eval("14+np.log10(np.sqrt(10**(-14)*(" + kb_val + "/" + ka_val + ")))"))
            elif kb_val != "" and ka_val != "" and ka_val > kb_val:
                ph_res = str(eval("-np.log10(np.sqrt(10**(-14)*(" + ka_val + "/" + kb_val + ")))"))
            elif pkb_val != "" and ka_val != "" and ka_val > pkb_val:
                ph_res = str(eval("-np.log10(np.sqrt(10**(-14)*(" + ka_val + "/10**(-" + pkb_val + ")))"))
            elif kb_val != "" and pka_val != "" and pka_val > kb_val:
                ph_res = str(eval("-np.log10(np.sqrt(10**(-14)*(10**(-" + pka_val + ")/" + kb_val + ")))"))
            elif pkb_val != "" and pka_val != "" and pka_val > pkb_val:
                ph_res = str(eval("-np.log10(np.sqrt(10**(-14))*(10**(-" + pka_val + ")/10**(-" + pkb_val + ")))"))
            elif pka_val != "" and kb_val != "" and kb_val > pka_val:
                ph_res = str(eval("14+np.log10(np.sqrt(10**(-14)*(" + kb_val + "/10**(-" + pka_val + ")))"))
            elif ka_val != "" and pkb_val != "" and pkb_val > ka_val:
                ph_res = str(eval("14+np.log10(np.sqrt(10**(-14)*(10**(-" + pkb_val + ")/" + ka_val + ")))"))
            elif pkb_val != "" and pka_val != "" and pkb_val > pka_val:
                ph_res = str(eval("14+np.log10(np.sqrt(10**(-14))*(10**(-" + pkb_val + ")/10**(-" + pka_val + ")))"))
            elif ph_val != "":
                ph_res = str(eval("14-" + poh_val))
            else:
                ph_res = str("Error")
        finally:
            if ph_i.get() == 1:
                if "e-0" in ph_res:
                    ph_res = ph_res.replace("e-0", "*10^(") + ")"
                elif "e" in ph_res:
                    ph_res = ph_res.replace("e", "*10^(-") + ")"
                ph_dis.config(text="pH = " + ph_res)
                ph_dis.grid(row=1, column=0, pady=10)
            else:
                ph_dis.grid_forget()
    else:
        try:
            ph_res = str(eval(ph_val))
        except:
            if pka_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                ph_res = str(eval(pka_val + "+np.log10(" + h_molarity_val + "/" + oh_molarity_val + ")"))
            elif ka_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                ph_res = str(eval(
                    "-np.log10(" + ka_val + ")+np.log10(" + h_molarity_val + "/" + oh_molarity_val + ")"))
            elif pkb_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                ph_res = str(
                    eval("14-" + pkb_val + "+np.log10(" + h_molarity_val + "/" + oh_molarity_val + ")"))
            elif kb_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                ph_res = str(eval(
                    "14+np.log10(" + kb_val + ")+np.log10(" + h_molarity_val + "/" + oh_molarity_val + ")"))
            elif poh_val != "":
                ph_res = str(eval("14-" + poh_val))
            else:
                ph_res = str("Error")
        finally:
            if ph_i.get() == 1:
                if "e-0" in ph_res:
                    ph_res = ph_res.replace("e-0", "*10^(") + ")"
                elif "e" in ph_res:
                    ph_res = ph_res.replace("e", "*10^(-") + ")"
                ph_dis.config(text="pH = " + ph_res)
                ph_dis.grid(row=1, column=0, pady=10)
            else:
                ph_dis.grid_forget()


def poh_calculation(*args):
    global ph_val
    ph_val = ""
    global poh_val
    poh_val = ""
    global h_molarity_val
    h_molarity_val = ""
    global oh_molarity_val
    oh_molarity_val = ""
    global salt_molarity_val
    salt_molarity_val = ""
    global ka_val
    ka_val = ""
    global kb_val
    kb_val = ""
    global pka_val
    pka_val = ""
    global pkb_val
    pkb_val = ""
    get_variable()
    poh_res = ""
    if sol_type.get() != "Weak Acid Buffer Solution" or sol_type.get() != "Weak Base Buffer Solution":
        try:
            poh_res = str(eval(poh_val))
        except:
            if h_molarity_val != "":
                poh_res = str(eval("14+np.log10(" + h_molarity_val + ")"))
            elif oh_molarity_val != "":
                poh_res = str(eval("-np.log10(" + oh_molarity_val + ")"))
            elif ph_val != "":
                poh_res = str(eval("14-" + ph_val))
            else:
                poh_res = str("Error")
        finally:
            if poh_i.get() == 1:
                if "e-0" in poh_res:
                    poh_res = poh_res.replace("e-0", "*10^(") + ")"
                elif "e" in poh_res:
                    poh_res = poh_res.replace("e", "*10^(-") + ")"
                poh_dis.config(text="pOH = " + poh_res)
                poh_dis.grid(row=2, column=0, pady=10)
            else:
                poh_dis.grid_forget()
    elif sol_type.get() == "Weak Base and Strong Acid Salt Hydrolysis" or sol_type.get() == "Weak Acid and Strong " \
                                                                                            "Base Salt Hydrolysis":
        try:
            poh_res = str(eval(poh_val))
        except:
            if salt_molarity_val != "" and ka_val != "":
                poh_res = str(eval("-np.log10(np.sqrt(((10**(-14))*" + salt_molarity_val + ")/" + ka_val + "))"))
            elif salt_molarity_val != "" and kb_val != "":
                poh_res = str(eval("14+np.log10(np.sqrt(((10**(-14))*" + salt_molarity_val + ")/" + kb_val + "))"))
            elif salt_molarity_val != "" and pka_val != "":
                poh_res = str(eval("-np.log10(np.sqrt(((10**(-14))*" + salt_molarity_val + ")/10**(" + pka_val + ")))"))
            elif salt_molarity_val != "" and pkb_val != "":
                poh_res = str(
                    eval("14+np.log10(np.sqrt(((10**(-14))*" + salt_molarity_val + ")/10**(" + pkb_val + ")))"))
            elif ph_val != "":
                poh_res = str(eval("14-" + ph_val))
            else:
                poh_res = str("Error")
        finally:
            if poh_i.get() == 1:
                if "e-0" in poh_res:
                    poh_res = poh_res.replace("e-0", "*10^(") + ")"
                elif "e" in poh_res:
                    poh_res = poh_res.replace("e", "*10^(-") + ")"
                poh_dis.config(text="pOH = " + poh_res)
                poh_dis.grid(row=1, column=0, pady=10)
            else:
                poh_dis.grid_forget()
    elif sol_type.get() == "Weak Acid and Base Salt Hydrolysis":
        try:
            poh_res = str(eval(poh_val))
        except:
            if kb_val != "" and ka_val != "" and kb_val > ka_val:
                poh_res = str(eval("-np.log10(np.sqrt(10**(-14)*(" + kb_val + "/" + ka_val + ")))"))
            elif kb_val != "" and ka_val != "" and ka_val > kb_val:
                poh_res = str(eval("14+np.log10(np.sqrt(10**(-14)*(" + ka_val + "/" + kb_val + ")))"))
            elif pkb_val != "" and ka_val != "" and ka_val > pkb_val:
                poh_res = str(eval("14+np.log10(np.sqrt(10**(-14)*(" + ka_val + "/10**(-" + pkb_val + ")))"))
            elif kb_val != "" and pka_val != "" and pka_val > kb_val:
                poh_res = str(eval("14+np.log10(np.sqrt(10**(-14)*(10**(-" + pka_val + ")/" + kb_val + ")))"))
            elif pkb_val != "" and pka_val != "" and pka_val > pkb_val:
                poh_res = str(eval("14+np.log10(np.sqrt(10**(-14))*(10**(-" + pka_val + ")/10**(-" + pkb_val + ")))"))
            elif pka_val != "" and kb_val != "" and kb_val > pka_val:
                poh_res = str(eval("-np.log10(np.sqrt(10**(-14)*(" + kb_val + "/10**(-" + pka_val + ")))"))
            elif ka_val != "" and pkb_val != "" and pkb_val > ka_val:
                poh_res = str(eval("-np.log10(np.sqrt(10**(-14)*(10**(-" + pkb_val + ")/" + ka_val + ")))"))
            elif pkb_val != "" and pka_val != "" and pkb_val > pka_val:
                poh_res = str(eval("-np.log10(np.sqrt(10**(-14))*(10**(-" + pkb_val + ")/10**(-" + pka_val + ")))"))
            elif ph_val != "":
                poh_res = str(eval("14-" + ph_val))
            else:
                poh_res = str("Error")
        finally:
            if poh_i.get() == 1:
                if "e-0" in poh_res:
                    poh_res = poh_res.replace("e-0", "*10^(") + ")"
                elif "e" in poh_res:
                    poh_res = poh_res.replace("e", "*10^(-") + ")"
                poh_dis.config(text="pOH = " + poh_res)
                poh_dis.grid(row=1, column=0, pady=10)
            else:
                poh_dis.grid_forget()
    else:
        try:
            poh_res = str(eval(ph_val))
        except:
            if pkb_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                poh_res = str(eval(pkb_val + "+np.log10(" + h_molarity_val + "/" + oh_molarity_val + ")"))
            elif kb_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                poh_res = str(eval(
                    "-np.log10(" + kb_val + ")+np.log10(" + h_molarity_val + "/" + oh_molarity_val + ")"))
            elif pka_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                poh_res = str(
                    eval("14-" + pka_val + "+np.log10(" + h_molarity_val + "/" + oh_molarity_val + ")"))
            elif ka_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                poh_res = str(eval(
                    "14+np.log10(" + ka_val + ")+np.log10(" + h_molarity_val + "/" + oh_molarity_val + ")"))
            elif poh_val != "":
                poh_res = str(eval("14-" + poh_val))
            else:
                poh_res = str("Error")
        finally:
            if poh_i.get() == 1:
                if "e-0" in poh_res:
                    poh_res = poh_res.replace("e-0", "*10^(") + ")"
                elif "e" in poh_res:
                    poh_res = poh_res.replace("e", "*10^(-") + ")"
                poh_dis.config(text="pOH = " + poh_res)
                poh_dis.grid(row=2, column=0, pady=10)
            else:
                poh_dis.grid_forget()


def h_molarity_calculation(*args):
    global ph_val
    ph_val = ""
    global poh_val
    poh_val = ""
    global h_molarity_val
    h_molarity_val = ""
    global oh_molarity_val
    oh_molarity_val = ""
    global salt_molarity_val
    salt_molarity_val = ""
    global ka_val
    ka_val = ""
    global kb_val
    kb_val = ""
    global pka_val
    pka_val = ""
    global pkb_val
    pkb_val = ""
    get_variable()
    h_molarity_res = ""
    if sol_type.get() == "Weak Acid and Strong Base Salt Hydrolysis":
        try:
            h_molarity_res = str(eval(h_molarity_val))
        except:
            if salt_molarity_val != "" and kb_val != "":
                h_molarity_res = str(eval("np.sqrt((10**(-14))*" + salt_molarity_val + "/" + kb_val + ")"))
            elif salt_molarity_val != "" and ka_val != "":
                h_molarity_res = str(eval("10**(-14)/(np.sqrt((10**(-14))*" + salt_molarity_val + "/" + ka_val + "))"))
            elif salt_molarity_val != "" and pkb_val != "":
                h_molarity_res = str(eval("np.sqrt((10**(-14))*" + salt_molarity_val + "/10**(" + pkb_val + "))"))
            elif salt_molarity_val != "" and pka_val != "":
                h_molarity_res = str(
                    eval("10**(-14)/(np.sqrt((10**(-14))*" + salt_molarity_val + "/10**" + pka_val + ")))"))
            else:
                h_molarity_res = str("Error")
        finally:
            if h_molarity_i.get() == 1:
                if "e-0" in h_molarity_res:
                    h_molarity_res = h_molarity_res.replace("e-0", "*10^(") + ")"
                elif "e" in h_molarity_res:
                    h_molarity_res = h_molarity_res.replace("e", "*10^(-") + ")"
                h_molarity_dis.config(text="[H+] = " + h_molarity_res)
                h_molarity_dis.grid(row=3, column=0, pady=10)
            else:
                h_molarity_dis.grid_forget()
    elif sol_type.get() == "Weak Acid and Base Salt Hydrolysis":
        try:
            h_molarity_res = str(eval(h_molarity_val))
        except:
            if kb_val != "" and ka_val != "" and kb_val > ka_val:
                h_molarity_res = str(eval("10**(-14)/np.sqrt(10**(-14)*(" + kb_val + "/" + ka_val + "))"))
            elif kb_val != "" and ka_val != "" and ka_val > kb_val:
                h_molarity_res = str(eval("np.sqrt(10**(-14)*(" + ka_val + "/" + kb_val + "))"))
            elif pkb_val != "" and ka_val != "" and ka_val > pkb_val:
                h_molarity_res = str(eval("np.sqrt(10**(-14)*(" + ka_val + "/10**(-" + pkb_val + ")))"))
            elif kb_val != "" and pka_val != "" and pka_val > kb_val:
                h_molarity_res = str(eval("np.sqrt(10**(-14)*(10**(-" + pka_val + ")/" + kb_val + ")))"))
            elif pkb_val != "" and pka_val != "" and pka_val > pkb_val:
                h_molarity_res = str(eval("np.sqrt(10**(-14))*(10**(-" + pka_val + ")/10**(-" + pkb_val + ")))"))
            elif pka_val != "" and kb_val != "" and kb_val > pka_val:
                h_molarity_res = str(eval("10**(-14)/np.sqrt(10**(-14)*(" + kb_val + "/10**(-" + pka_val + ")))"))
            elif ka_val != "" and pkb_val != "" and pkb_val > ka_val:
                h_molarity_res = str(eval("10**(-14)/np.sqrt(10**(-14)*(10**(-" + pkb_val + ")/" + ka_val + ")))"))
            elif pkb_val != "" and pka_val != "" and pkb_val > pka_val:
                h_molarity_res = str(eval("10**(-14)/np.sqrt(10**(-14))*(10**(-" + pkb_val + ")/10**(-" + pka_val + ")))"))
            else:
                h_molarity_res = str("Error")
        finally:
            if h_molarity_i.get() == 1:
                if "e-0" in h_molarity_res:
                    h_molarity_res = h_molarity_res.replace("e-0", "*10^(") + ")"
                elif "e" in h_molarity_res:
                    h_molarity_res = h_molarity_res.replace("e", "*10^(-") + ")"
                h_molarity_dis.config(text="[H+] = " + h_molarity_res)
                h_molarity_dis.grid(row=1, column=0, pady=10)
            else:
                h_molarity_dis.grid_forget()
    else:
        try:
            h_molarity_res = str(eval(h_molarity_val))
        except:
            if ph_val != "":
                h_molarity_res = str(eval("10**(-" + ph_val + ")"))
            elif poh_val != "":
                h_molarity_res = str(eval("10**(-14)/10**(-" + poh_val + ")"))
            elif oh_molarity_val != "":
                h_molarity_res = str(eval("10**(-14)/" + oh_molarity_val))
            else:
                h_molarity_res = str("Error")
        finally:
            if h_molarity_i.get() == 1:
                if "e-0" in h_molarity_res:
                    h_molarity_res = h_molarity_res.replace("e-0", "*10^(") + ")"
                elif "e" in h_molarity_res:
                    h_molarity_res = h_molarity_res.replace("e", "*10^(-") + ")"
                h_molarity_dis.config(text="[H+] = " + h_molarity_res)
                h_molarity_dis.grid(row=3, column=0, pady=10)
            else:
                h_molarity_dis.grid_forget()


def oh_molarity_calculation(*args):
    global ph_val
    ph_val = ""
    global poh_val
    poh_val = ""
    global h_molarity_val
    h_molarity_val = ""
    global oh_molarity_val
    oh_molarity_val = ""
    global salt_molarity_val
    salt_molarity_val = ""
    global ka_val
    ka_val = ""
    global kb_val
    kb_val = ""
    global pka_val
    pka_val = ""
    global pkb_val
    pkb_val = ""
    get_variable()
    oh_molarity_res = ""
    if sol_type.get() == "Weak Base and Strong Acid Salt Hydrolysis":
        try:
            oh_molarity_res = str(eval(oh_molarity_val))
        except:
            if salt_molarity_val != "" and ka_val != "":
                oh_molarity_res = str(eval("np.sqrt((10**(-14))*" + salt_molarity_val + "/" + ka_val + ")"))
            elif salt_molarity_val != "" and kb_val != "":
                oh_molarity_res = str(
                    eval("10**(-14)/(np.sqrt((10**(-14))*" + salt_molarity_val + "/" + kb_val + "))"))
            elif salt_molarity_val != "" and pka_val != "":
                oh_molarity_res = str(eval("np.sqrt((10**(-14))*" + salt_molarity_val + "/10**(" + pka_val + "))"))
            elif salt_molarity_val != "" and kb_val != "":
                oh_molarity_res = str(
                    eval("10**(-14)/(np.sqrt((10**(-14))*" + salt_molarity_val + "/10**" + kb_val + ")))"))
            else:
                oh_molarity_res = str("Error")
        finally:
            if oh_molarity_i.get() == 1:
                if "e-0" in oh_molarity_res:
                    oh_molarity_res = oh_molarity_res.replace("e-0", "*10^(") + ")"
                elif "e" in oh_molarity_res:
                    oh_molarity_res = oh_molarity_res.replace("e", "*10^(-") + ")"
                oh_molarity_dis.config(text="[OH-] = " + oh_molarity_res)
                oh_molarity_dis.grid(row=3, column=0, pady=10)
            else:
                oh_molarity_dis.grid_forget()
    elif sol_type.get() == "Weak Acid and Base Salt Hydrolysis":
        try:
            oh_molarity_res = str(eval(oh_molarity_val))
        except:
            if kb_val != "" and ka_val != "" and kb_val > ka_val:
                oh_molarity_res = str(eval("np.sqrt(10**(-14)*(" + kb_val + "/" + ka_val + "))"))
            elif kb_val != "" and ka_val != "" and ka_val > kb_val:
                oh_molarity_res = str(eval("10**(-14)/np.sqrt(10**(-14)*(" + ka_val + "/" + kb_val + "))"))
            elif pkb_val != "" and ka_val != "" and ka_val > pkb_val:
                oh_molarity_res = str(eval("10**(-14)/np.sqrt(10**(-14)*(" + ka_val + "/10**(-" + pkb_val + ")))"))
            elif kb_val != "" and pka_val != "" and pka_val > kb_val:
                oh_molarity_res = str(eval("10**(-14)/np.sqrt(10**(-14)*(10**(-" + pka_val + ")/" + kb_val + ")))"))
            elif pkb_val != "" and pka_val != "" and pka_val > pkb_val:
                oh_molarity_res = str(eval("10**(-14)/np.sqrt(10**(-14))*(10**(-" + pka_val + ")/10**(-" + pkb_val + ")))"))
            elif pka_val != "" and kb_val != "" and kb_val > pka_val:
                oh_molarity_res = str(eval("np.sqrt(10**(-14)*(" + kb_val + "/10**(-" + pka_val + ")))"))
            elif ka_val != "" and pkb_val != "" and pkb_val > ka_val:
                oh_molarity_res = str(eval("np.sqrt(10**(-14)*(10**(-" + pkb_val + ")/" + ka_val + ")))"))
            elif pkb_val != "" and pka_val != "" and pkb_val > pka_val:
                oh_molarity_res = str(eval("np.sqrt(10**(-14))*(10**(-" + pkb_val + ")/10**(-" + pka_val + ")))"))
            else:
                oh_molarity_res = str("Error")
        finally:
            if oh_molarity_i.get() == 1:
                if "e-0" in oh_molarity_res:
                    oh_molarity_res = oh_molarity_res.replace("e-0", "*10^(") + ")"
                elif "e" in oh_molarity_res:
                    oh_molarity_res = oh_molarity_res.replace("e", "*10^(-") + ")"
                oh_molarity_dis.config(text="[OH-] = " + oh_molarity_res)
                oh_molarity_dis.grid(row=1, column=0, pady=10)
            else:
                oh_molarity_dis.grid_forget()
    else:
        try:
            oh_molarity_res = str(eval(oh_molarity_val))
        except:
            if ph_val != "":
                oh_molarity_res = str(eval("10**(-14)/10**(-" + ph_val + ")"))
            elif poh_val != "":
                oh_molarity_res = str(eval("10**(-" + poh_val + ")"))
            elif h_molarity_val != "":
                oh_molarity_res = str(eval("10**(-14)/" + h_molarity_val))
            else:
                oh_molarity_res = str("Error")
        finally:
            if oh_molarity_i.get() == 1:
                if "e-0" in oh_molarity_res:
                    oh_molarity_res = oh_molarity_res.replace("e-0", "*10^(") + ")"
                elif "e" in oh_molarity_res:
                    oh_molarity_res = oh_molarity_res.replace("e", "*10^(-") + ")"
                oh_molarity_dis.config(text="[OH-] = " + oh_molarity_res)
                oh_molarity_dis.grid(row=4, column=0, pady=10)
            else:
                oh_molarity_dis.grid_forget()


def salt_molarity_calculation(*args):
    global ph_val
    ph_val = ""
    global poh_val
    poh_val = ""
    global h_molarity_val
    h_molarity_val = ""
    global oh_molarity_val
    oh_molarity_val = ""
    global salt_molarity_val
    salt_molarity_val = ""
    global ka_val
    ka_val = ""
    global kb_val
    kb_val = ""
    global pka_val
    pka_val = ""
    global pkb_val
    pkb_val = ""
    get_variable()
    salt_molarity_res = ""
    try:
        salt_molarity_res = str(eval(salt_molarity_val))
    except:
        if oh_molarity_val != "" and ka_val != "":
            salt_molarity_res = str(eval("(" + oh_molarity_val + "**2)*" + ka_val + "/10**(-14))"))
        elif h_molarity_val != "" and kb_val != "":
            salt_molarity_res = str(eval("(" + h_molarity_val + "**2)*" + kb_val + "/10**(-14))"))
        elif h_molarity_val != "" and ka_val != "":
            salt_molarity_res = str(eval(ka_val + "/" + h_molarity_val))
        elif oh_molarity_val != "" and kb_val != "":
            salt_molarity_res = str(eval(ka_val + "/" + h_molarity_val))
        else:
            salt_molarity_res = str("Error")
    finally:
        if salt_molarity_i.get() == 1:
            if "e-0" in salt_molarity_res:
                salt_molarity_res = salt_molarity_res.replace("e-0", "*10^(") + ")"
            elif "e" in salt_molarity_res:
                salt_molarity_res = salt_molarity_res.replace("e", "*10^(-") + ")"
            salt_molarity_dis.config(text="[Salt] = " + salt_molarity_res)
            salt_molarity_dis.grid(row=5, column=0, pady=10)
        else:
            salt_molarity_dis.grid_forget()


def ka_calculation(*args):
    global ph_val
    ph_val = ""
    global poh_val
    poh_val = ""
    global h_molarity_val
    h_molarity_val = ""
    global oh_molarity_val
    oh_molarity_val = ""
    global salt_molarity_val
    salt_molarity_val = ""
    global ka_val
    ka_val = ""
    global kb_val
    kb_val = ""
    global pka_val
    pka_val = ""
    global pkb_val
    pkb_val = ""
    get_variable()
    ka_res = ""
    if sol_type.get() != "Strong Acid and Base Solution":
        try:
            ka_res = str(eval(ka_val))
        except:
            if pka_val != "":
                ka_res = str(eval("10**(-" + pka_val + ")"))
            elif pkb_val != "":
                ka_res = str(eval("10**(-14)/10**(-" + pkb_val + ")"))
            elif kb_val != "":
                ka_res = str(eval("10**(-14)/" + kb_val))
            elif ph_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                ka_res = str(
                    eval("10**(np.log10(" + h_molarity_val + "/" + oh_molarity_val + ")-" + ph_val + ")"))
            elif ph_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                ka_res = str(
                    eval("10**(" + poh_val + "-14-np.log10(" + h_molarity_val + "/" + oh_molarity_val + "))"))
            else:
                ka_res = str("Error")
        finally:
            if ka_i.get() == 1:
                if "e-0" in ka_res:
                    ka_res = ka_res.replace("e-0", "*10^(") + ")"
                elif "e" in ka_res:
                    ka_res = ka_res.replace("e", "*10^(-") + ")"
                ka_dis.config(text="Ka = " + ka_res)
                ka_dis.grid(row=6, column=0, pady=10)
            else:
                ka_dis.grid_forget()


def kb_calculation(*args):
    global ph_val
    ph_val = ""
    global poh_val
    poh_val = ""
    global h_molarity_val
    h_molarity_val = ""
    global oh_molarity_val
    oh_molarity_val = ""
    global salt_molarity_val
    salt_molarity_val = ""
    global ka_val
    ka_val = ""
    global kb_val
    kb_val = ""
    global pka_val
    pka_val = ""
    global pkb_val
    pkb_val = ""
    get_variable()
    kb_res = ""
    if sol_type.get() != "Strong Acid and Base Solution":
        try:
            kb_res = str(eval(kb_val))
        except:
            if pkb_val != "":
                kb_res = str(eval("10**(-" + pkb_val + ")"))
            elif pka_val != "":
                kb_res = str(eval("10**(-14)/10**(-" + pka_val + ")"))
            elif ka_val != "":
                kb_res = str(eval("10**(-14)/" + ka_val))
            elif poh_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                kb_res = str(
                    eval("10**(np.log10(" + oh_molarity_val + "/" + h_molarity_val + ")-" + poh_val + ")"))
            elif ph_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                kb_res = str(
                    eval("10**(" + ph_val + "-14-np.log10(" + oh_molarity_val + "/" + h_molarity_val + "))"))
            else:
                kb_res = str("Error")
        finally:
            if kb_i.get() == 1:
                if "e-0" in kb_res:
                    kb_res = kb_res.replace("e-0", "*10^(") + ")"
                elif "e" in kb_res:
                    kb_res = kb_res.replace("e", "*10^(-") + ")"
                kb_dis.config(text="Kb = " + kb_res)
                kb_dis.grid(row=7, column=0, pady=10)
            else:
                kb_dis.grid_forget()


def pka_calculation(*args):
    global ph_val
    ph_val = ""
    global poh_val
    poh_val = ""
    global h_molarity_val
    h_molarity_val = ""
    global oh_molarity_val
    oh_molarity_val = ""
    global salt_molarity_val
    salt_molarity_val = ""
    global ka_val
    ka_val = ""
    global kb_val
    kb_val = ""
    global pka_val
    pka_val = ""
    global pkb_val
    pkb_val = ""
    get_variable()
    pka_res = ""
    if sol_type.get() != "Strong Acid and Base Solution":
        try:
            pka_res = str(eval(pka_val))
        except:
            if ka_val != "":
                pka_res = str(eval("-np.log10(" + ka_val + ")"))
            elif pkb_val != "":
                pka_res = str(eval("14-" + pkb_val))
            elif kb_val != "":
                pka_res = str(eval("14+np.log10(" + kb_val + ")"))
            elif ph_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                pka_res = str(eval(ph_val + "-np.log10(" + h_molarity_val + "/" + oh_molarity_val + ")"))
            elif poh_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                pka_res = str(
                    eval("14-" + poh_val + "+np.log(" + h_molarity_val + "/" + oh_molarity_val + ")"))
            else:
                pka_res = str("Error")
        finally:
            if pka_i.get() == 1:
                if "e-0" in pka_res:
                    pka_res = pka_res.replace("e-0", "*10^(") + ")"
                elif "e" in pka_res:
                    pka_res = pka_res.replace("e", "*10^(-") + ")"
                pka_dis.config(text="pKa = " + pka_res)
                pka_dis.grid(row=8, column=0, pady=10)
            else:
                pka_dis.grid_forget()


def pkb_calculation(*args):
    global ph_val
    ph_val = ""
    global poh_val
    poh_val = ""
    global h_molarity_val
    h_molarity_val = ""
    global oh_molarity_val
    oh_molarity_val = ""
    global salt_molarity_val
    salt_molarity_val = ""
    global ka_val
    ka_val = ""
    global kb_val
    kb_val = ""
    global pka_val
    pka_val = ""
    global pkb_val
    pkb_val = ""
    get_variable()
    pkb_res = ""
    if sol_type.get() != "Strong Acid and Base Solution":
        try:
            pkb_res = str(eval(pkb_val))
        except:
            if kb_val != "":
                pkb_res = str(eval("-np.log10(" + kb_val + ")"))
            elif pka_val != "":
                pkb_res = str(eval("14-" + pka_val))
            elif ka_val != "":
                pkb_res = str(eval("14+np.log10(" + ka_val + ")"))
            elif poh_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                pkb_res = str(eval(poh_val + "-np.log10(" + oh_molarity_val + "/" + h_molarity_val + ")"))
            elif ph_val != "" and h_molarity_val != "" and oh_molarity_val != "":
                pkb_res = str(
                    eval("14-" + ph_val + "+np.log(" + oh_molarity_val + "/" + h_molarity_val + ")"))
            else:
                pkb_res = str("Error")
        finally:
            if pkb_i.get() == 1:
                if "e-0" in pkb_res:
                    pkb_res = pkb_res.replace("e-0", "*10^(") + ")"
                elif "e" in pkb_res:
                    pkb_res = pkb_res.replace("e", "*10^(-") + ")"
                pkb_dis.config(text="pKb = " + pkb_res)
                pkb_dis.grid(row=9, column=0, pady=10)
            else:
                pkb_dis.grid_forget()


# Solution_Type
def get_sol_type(*args):
    variables_opt.entryconfig("pH", state="normal")
    variables_opt.entryconfig("pOH", state="normal")
    variables_opt.entryconfig("Concentration of Hydrogen Ions", state="normal")
    variables_opt.entryconfig("Concentration of Hydroxide Ions", state="normal")
    variables_opt.entryconfig("Concentration of Salt", state="normal")
    calculate_opt.entryconfig("pH", state="normal")
    calculate_opt.entryconfig("pOH", state="normal")
    calculate_opt.entryconfig("Concentration of Hydrogen Ions", state="normal")
    calculate_opt.entryconfig("Concentration of Hydroxide Ions", state="normal")
    calculate_opt.entryconfig("Concentration of Salt", state="normal")
    if sol_type.get() == "Strong Acid and Base Solution":
        i_salt_molarity.set(0)
        salt_molarity_variable()
        i_ka.set(0)
        ka_variable()
        i_kb.set(0)
        kb_variable()
        i_pka.set(0)
        pka_variable()
        i_pkb.set(0)
        pkb_variable()
        variables_opt.entryconfig("Concentration of Hydrogen Ions", state="normal")
        variables_opt.entryconfig("Concentration of Hydroxide Ions", state="normal")
        variables_opt.entryconfig("Concentration of Salt", state="disabled")
        variables_opt.entryconfig("Ka", state="disabled")
        variables_opt.entryconfig("pKa", state="disabled")
        variables_opt.entryconfig("Kb", state="disabled")
        variables_opt.entryconfig("pKb", state="disabled")
        calculate_opt.entryconfig("Concentration of Hydrogen Ions", state="normal")
        calculate_opt.entryconfig("Concentration of Hydroxide Ions", state="normal")
        calculate_opt.entryconfig("Concentration of Salt", state="disabled")
        calculate_opt.entryconfig("Ka", state="disabled")
        calculate_opt.entryconfig("pKa", state="disabled")
        calculate_opt.entryconfig("Kb", state="disabled")
        calculate_opt.entryconfig("pKb", state="disabled")
        ka_dis.grid_forget()
        kb_dis.grid_forget()
        pka_dis.grid_forget()
        pkb_dis.grid_forget()
        salt_molarity_dis.grid_forget()
        salt_molarity_i.set(0)
        ka_i.set(0)
        pka_i.set(0)
        kb_i.set(0)
        pkb_i.set(0)
        space1.grid_forget()
        space2.grid_forget()
    elif sol_type.get() == "Weak Acid Buffer Solution":
        i_salt_molarity.set(0)
        salt_molarity_variable()
        i_ka.set(1)
        ka_variable()
        i_kb.set(0)
        kb_variable()
        i_pka.set(0)
        pka_variable()
        i_pkb.set(0)
        pkb_variable()
        variables_opt.entryconfig("Concentration of Hydrogen Ions", state="normal")
        variables_opt.entryconfig("Concentration of Hydroxide Ions", state="normal")
        variables_opt.entryconfig("Concentration of Salt", state="disabled")
        variables_opt.entryconfig("Ka", state="normal")
        variables_opt.entryconfig("pKa", state="normal")
        variables_opt.entryconfig("Kb", state="disabled")
        variables_opt.entryconfig("pKb", state="disabled")
        calculate_opt.entryconfig("Concentration of Hydrogen Ions", state="disabled")
        calculate_opt.entryconfig("Concentration of Hydroxide Ions", state="disabled")
        calculate_opt.entryconfig("Concentration of Salt", state="disabled")
        calculate_opt.entryconfig("Ka", state="normal")
        calculate_opt.entryconfig("pKa", state="normal")
        calculate_opt.entryconfig("Kb", state="disabled")
        calculate_opt.entryconfig("pKb", state="disabled")
        h_molarity_dis.grid_forget()
        oh_molarity_dis.grid_forget()
        salt_molarity_dis.grid_forget()
        kb_dis.grid_forget()
        pkb_dis.grid_forget()
        h_molarity_i.set(0)
        oh_molarity_i.set(0)
        salt_molarity_i.set(0)
        ka_i.set(0)
        pka_i.set(0)
        kb_i.set(0)
        pkb_i.set(0)
        space1.grid_forget()
        space2.grid_forget()
    elif sol_type.get() == "Weak Base Buffer Solution":
        i_salt_molarity.set(0)
        salt_molarity_variable()
        i_kb.set(1)
        kb_variable()
        i_ka.set(0)
        ka_variable()
        i_pkb.set(0)
        pkb_variable()
        i_pka.set(0)
        pka_variable()
        variables_opt.entryconfig("Concentration of Hydrogen Ions", state="normal")
        variables_opt.entryconfig("Concentration of Hydroxide Ions", state="normal")
        variables_opt.entryconfig("Concentration of Salt", state="disabled")
        variables_opt.entryconfig("Ka", state="disabled")
        variables_opt.entryconfig("pKa", state="disabled")
        variables_opt.entryconfig("Kb", state="normal")
        variables_opt.entryconfig("pKb", state="normal")
        calculate_opt.entryconfig("Concentration of Hydrogen Ions", state="disabled")
        calculate_opt.entryconfig("Concentration of Hydroxide Ions", state="disabled")
        calculate_opt.entryconfig("Concentration of Salt", state="disabled")
        calculate_opt.entryconfig("Ka", state="disabled")
        calculate_opt.entryconfig("pKa", state="disabled")
        calculate_opt.entryconfig("Kb", state="normal")
        calculate_opt.entryconfig("pKb", state="normal")
        h_molarity_dis.grid_forget()
        oh_molarity_dis.grid_forget()
        salt_molarity_dis.grid_forget()
        ka_dis.grid_forget()
        pka_dis.grid_forget()
        h_molarity_i.set(0)
        oh_molarity_i.set(0)
        salt_molarity_i.set(0)
        ka_i.set(0)
        pka_i.set(0)
        kb_i.set(0)
        pkb_i.set(0)
        space1.grid_forget()
        space2.grid_forget()
    elif sol_type.get() == "Weak Acid and Strong Base Salt Hydrolysis":
        i_h_molarity.set(0)
        h_molarity_variable()
        i_oh_molarity.set(0)
        oh_molarity_variable()
        i_salt_molarity.set(1)
        salt_molarity_variable()
        i_ka.set(1)
        ka_variable()
        i_kb.set(0)
        kb_variable()
        i_pka.set(0)
        pka_variable()
        i_pkb.set(0)
        pkb_variable()
        variables_opt.entryconfig("Concentration of Hydrogen Ions", state="disabled")
        variables_opt.entryconfig("Concentration of Hydroxide Ions", state="disabled")
        variables_opt.entryconfig("Concentration of Salt", state="normal")
        variables_opt.entryconfig("Ka", state="normal")
        variables_opt.entryconfig("pKa", state="normal")
        variables_opt.entryconfig("Kb", state="disabled")
        variables_opt.entryconfig("pKb", state="disabled")
        calculate_opt.entryconfig("Concentration of Hydrogen Ions", state="normal")
        calculate_opt.entryconfig("Concentration of Hydroxide Ions", state="normal")
        calculate_opt.entryconfig("Concentration of Salt", state="normal")
        calculate_opt.entryconfig("Ka", state="normal")
        calculate_opt.entryconfig("pKa", state="normal")
        calculate_opt.entryconfig("Kb", state="disabled")
        calculate_opt.entryconfig("pKb", state="disabled")
        kb_dis.grid_forget()
        pkb_dis.grid_forget()
        salt_molarity_dis.grid_forget()
        salt_molarity_i.set(0)
        ka_i.set(0)
        pka_i.set(0)
        kb_i.set(0)
        pkb_i.set(0)
        space1.grid_forget()
        space2.grid_forget()
    elif sol_type.get() == "Weak Base and Strong Acid Salt Hydrolysis":
        i_h_molarity.set(0)
        h_molarity_variable()
        i_oh_molarity.set(0)
        oh_molarity_variable()
        i_salt_molarity.set(1)
        salt_molarity_variable()
        i_kb.set(1)
        kb_variable()
        i_ka.set(0)
        ka_variable()
        i_pkb.set(0)
        pkb_variable()
        i_pka.set(0)
        pka_variable()
        variables_opt.entryconfig("Concentration of Hydrogen Ions", state="disabled")
        variables_opt.entryconfig("Concentration of Hydroxide Ions", state="disabled")
        variables_opt.entryconfig("Concentration of Salt", state="normal")
        variables_opt.entryconfig("Ka", state="disabled")
        variables_opt.entryconfig("pKa", state="disabled")
        variables_opt.entryconfig("Kb", state="normal")
        variables_opt.entryconfig("pKb", state="normal")
        calculate_opt.entryconfig("Concentration of Hydrogen Ions", state="normal")
        calculate_opt.entryconfig("Concentration of Hydroxide Ions", state="normal")
        calculate_opt.entryconfig("Concentration of Salt", state="normal")
        calculate_opt.entryconfig("Ka", state="disabled")
        calculate_opt.entryconfig("pKa", state="disabled")
        calculate_opt.entryconfig("Kb", state="normal")
        calculate_opt.entryconfig("pKb", state="normal")
        ka_dis.grid_forget()
        pka_dis.grid_forget()
        salt_molarity_dis.grid_forget()
        salt_molarity_i.set(0)
        ka_i.set(0)
        pka_i.set(0)
        kb_i.set(0)
        pkb_i.set(0)
        space1.grid_forget()
        space2.grid_forget()
    elif sol_type.get() == "Weak Acid and Base Salt Hydrolysis":
        i_h_molarity.set(0)
        h_molarity_variable()
        i_oh_molarity.set(0)
        oh_molarity_variable()
        i_salt_molarity.set(0)
        salt_molarity_variable()
        i_kb.set(1)
        kb_variable()
        i_ka.set(1)
        ka_variable()
        i_pkb.set(0)
        pkb_variable()
        i_pka.set(0)
        pka_variable()
        variables_opt.entryconfig("Concentration of Hydrogen Ions", state="disabled")
        variables_opt.entryconfig("Concentration of Hydroxide Ions", state="disabled")
        variables_opt.entryconfig("Concentration of Salt", state="disabled")
        variables_opt.entryconfig("Ka", state="normal")
        variables_opt.entryconfig("pKa", state="normal")
        variables_opt.entryconfig("Kb", state="normal")
        variables_opt.entryconfig("pKb", state="normal")
        calculate_opt.entryconfig("Concentration of Hydrogen Ions", state="normal")
        calculate_opt.entryconfig("Concentration of Hydroxide Ions", state="normal")
        calculate_opt.entryconfig("Concentration of Salt", state="disabled")
        calculate_opt.entryconfig("Ka", state="normal")
        calculate_opt.entryconfig("pKa", state="normal")
        calculate_opt.entryconfig("Kb", state="normal")
        calculate_opt.entryconfig("pKb", state="normal")
        ka_dis.grid_forget()
        pka_dis.grid_forget()
        salt_molarity_dis.grid_forget()
        salt_molarity_i.set(0)
        ka_i.set(0)
        pka_i.set(0)
        kb_i.set(0)
        pkb_i.set(0)
        space1.grid_forget()
        space2.grid_forget()


# Known_Variables
def ph_variable(*args):
    if i_ph.get() == 1:
        ph_label.grid(row=4, column=0, padx=10, pady=10, sticky="w")
        ph.grid(row=4, column=1, padx=10, pady=10, sticky="e")
    else:
        ph.delete(0, "end")
        ph_label.grid_forget()
        ph.grid_forget()


def poh_variable(*args):
    if i_poh.get() == 1:
        poh_label.grid(row=5, column=0, padx=10, pady=10, sticky="w")
        poh.grid(row=5, column=1, padx=10, pady=10, sticky="e")
    else:
        poh.delete(0, "end")
        poh_label.grid_forget()
        poh.grid_forget()


def h_molarity_variable(*args):
    if i_h_molarity.get() == 1:
        h_molarity_label.grid(row=6, column=0, padx=10, pady=10, sticky="w")
        h_molarity.grid(row=6, column=1, padx=10, pady=10, sticky="e")
    else:
        h_molarity.delete(0, "end")
        h_molarity_label.grid_forget()
        h_molarity.grid_forget()


def oh_molarity_variable(*args):
    if i_oh_molarity.get() == 1:
        oh_molarity_label.grid(row=7, column=0, padx=10, pady=10, sticky="w")
        oh_molarity.grid(row=7, column=1, padx=10, pady=10, sticky="e")
    else:
        oh_molarity.delete(0, "end")
        oh_molarity_label.grid_forget()
        oh_molarity.grid_forget()


def salt_molarity_variable(*args):
    if i_salt_molarity.get() == 1:
        salt_molarity_label.grid(row=8, column=0, padx=10, pady=10, sticky="w")
        salt_molarity.grid(row=8, column=1, padx=10, pady=10, sticky="e")
    else:
        salt_molarity.delete(0, "end")
        salt_molarity_label.grid_forget()
        salt_molarity.grid_forget()


def ka_variable(*args):
    if i_ka.get() == 1:
        ka_label.grid(row=0, column=0, padx=10, pady=10, sticky="w")
        ka.grid(row=0, column=1, padx=10, pady=10, sticky="e")
    else:
        ka.delete(0, "end")
        ka_label.grid_forget()
        ka.grid_forget()


def kb_variable(*args):
    if i_kb.get() == 1:
        kb_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")
        kb.grid(row=1, column=1, padx=10, pady=10, sticky="e")
    else:
        kb.delete(0, "end")
        kb_label.grid_forget()
        kb.grid_forget()


def pka_variable(*args):
    if i_pka.get() == 1:
        pka_label.grid(row=2, column=0, padx=10, pady=10, sticky="w")
        pka.grid(row=2, column=1, padx=10, pady=10, sticky="e")
    else:
        pka.delete(0, "end")
        pka_label.grid_forget()
        pka.grid_forget()


def pkb_variable(*args):
    if i_pkb.get() == 1:
        pkb_label.grid(row=3, column=0, padx=10, pady=10, sticky="w")
        pkb.grid(row=3, column=1, padx=10, pady=10, sticky="e")
    else:
        pkb.delete(0, "end")
        pkb_label.grid_forget()
        pkb.grid_forget()


# Window
root = tk.Tk()
root.title("pHelp 65.44")
root.configure(bg="#91D8E4")
root.resizable(False, False)
root.eval("tk::PlaceWindow . center")
# Tutorial
root.bind('<Shift-H>', lambda e: show_help(e))
tutorial_label = tk.Label(root, text="Press Shift+H to Show Tutorial", bg="#91D8E4", fg="#808080",
                          font=("Trebuchet MS", 10))
tutorial_label.grid(row=5, column=0, columnspan=2, pady=3)


def show_help(*args):
    tutorial_window = tk.Toplevel()
    tutorial_window.title("pHelper How to Use")
    img = ImageTk.PhotoImage(Image.open("pHelper_Tutorial.png").resize((500, 700)))
    panel = tk.Label(tutorial_window, image=img)
    panel.photo = img
    panel.grid(row=0, column=0)


# Left_Side
first_frame = tk.Frame(root, bg="#91D8E4")
first_frame.grid(row=3, column=0, columnspan=2)
# Right_Side
second_frame = tk.Frame(root, bg="#91D8E4")
second_frame.grid(row=4, column=0, columnspan=2)
# Choosing_Solution
sol_opt = ["Strong Acid and Base Solution", "Weak Acid Buffer Solution", "Weak Base Buffer Solution",
           "Weak Acid and Strong Base Salt Hydrolysis", "Weak Base and Strong Acid Salt Hydrolysis",
           "Weak Acid and Base Salt Hydrolysis"]
sol_type = ttk.Combobox(root, values=sol_opt, width=30, state="readonly", font=("Trebuchet MS", 12))
root.option_add("*TCombobox*Listbox.font", ("Trebuchet MS", 10))
sol_type.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="n")
sol_type.set("Choose a Solution Type")
sol_type.bind("<<ComboboxSelected>>", get_sol_type)
# Variable_Options
variables = tk.Menubutton(root, text="Choose What is Known", background="#91D8E4", font=("Trebuchet MS", 12))
variables.grid(row=1, column=1, pady=10, sticky="w")
i_ph = tk.IntVar()
i_poh = tk.IntVar()
i_h_molarity = tk.IntVar()
i_oh_molarity = tk.IntVar()
i_salt_molarity = tk.IntVar()
i_ka = tk.IntVar()
i_kb = tk.IntVar()
i_pka = tk.IntVar()
i_pkb = tk.IntVar()
variables_opt = tk.Menu(variables, tearoff=1, background="#C5DFF8", selectcolor="#91D8E4", font=("Trebuchet MS", 12))
variables_opt.add_checkbutton(label="pH", variable=i_ph, command=ph_variable, font=("Trebuchet MS", 12))
variables_opt.add_checkbutton(label="pOH", variable=i_poh, command=poh_variable, font=("Trebuchet MS", 12))
variables_opt.add_checkbutton(label="Concentration of Hydrogen Ions", variable=i_h_molarity,
                              command=h_molarity_variable,
                              font=("Trebuchet MS", 12))
variables_opt.add_checkbutton(label="Concentration of Hydroxide Ions", variable=i_oh_molarity,
                              command=oh_molarity_variable,
                              font=("Trebuchet MS", 12))
variables_opt.add_checkbutton(label="Concentration of Salt", variable=i_salt_molarity,
                              command=salt_molarity_variable,
                              font=("Trebuchet MS", 12))
variables_opt.add_checkbutton(label="Ka", variable=i_ka, command=ka_variable, font=("Trebuchet MS", 12))
variables_opt.add_checkbutton(label="pKa", variable=i_pka, command=pka_variable, font=("Trebuchet MS", 12))
variables_opt.add_checkbutton(label="Kb", variable=i_kb, command=kb_variable, font=("Trebuchet MS", 12))
variables_opt.add_checkbutton(label="pKb", variable=i_pkb, command=pkb_variable, font=("Trebuchet MS", 12))
variables["menu"] = variables_opt
variables_label = tk.Label(root, text="From :", bg="#91D8E4", fg="#FF0060", font=("Trebuchet MS", 12))
variables_label.grid(row=1, column=0, pady=10, sticky="e")
variables_opt.entryconfig("pH", state="disabled")
variables_opt.entryconfig("pOH", state="disabled")
variables_opt.entryconfig("Concentration of Hydrogen Ions", state="disabled")
variables_opt.entryconfig("Concentration of Hydroxide Ions", state="disabled")
variables_opt.entryconfig("Concentration of Salt", state="disabled")
variables_opt.entryconfig("Ka", state="disabled")
variables_opt.entryconfig("Kb", state="disabled")
variables_opt.entryconfig("pKa", state="disabled")
variables_opt.entryconfig("pKb", state="disabled")
# Calculation_Options
calculate = tk.Menubutton(root, text="Choose What to Calculate", background="#91D8E4", font=("Trebuchet MS", 12))
calculate.grid(row=2, column=1, pady=10, sticky="w")
ph_i = tk.IntVar()
poh_i = tk.IntVar()
h_molarity_i = tk.IntVar()
oh_molarity_i = tk.IntVar()
salt_molarity_i = tk.IntVar()
ka_i = tk.IntVar()
kb_i = tk.IntVar()
pka_i = tk.IntVar()
pkb_i = tk.IntVar()
calculate_opt = tk.Menu(calculate, tearoff=0, background="#C5DFF8", selectcolor="#91D8E4", font=("Trebuchet MS", 12))
calculate_opt.add_checkbutton(label="pH", variable=ph_i, command=ph_calculation, font=("Trebuchet MS", 12))
calculate_opt.add_checkbutton(label="pOH", variable=poh_i, command=poh_calculation, font=("Trebuchet MS", 12))
calculate_opt.add_checkbutton(label="Concentration of Hydrogen Ions", variable=h_molarity_i,
                              command=h_molarity_calculation,
                              font=("Trebuchet MS", 12))
calculate_opt.add_checkbutton(label="Concentration of Hydroxide Ions", variable=oh_molarity_i,
                              command=oh_molarity_calculation,
                              font=("Trebuchet MS", 12))
calculate_opt.add_checkbutton(label="Concentration of Salt", variable=salt_molarity_i,
                              command=salt_molarity_calculation,
                              font=("Trebuchet MS", 12))
calculate_opt.add_checkbutton(label="Ka", variable=ka_i, command=ka_calculation, font=("Trebuchet MS", 12))
calculate_opt.add_checkbutton(label="pKa", variable=pka_i, command=pka_calculation, font=("Trebuchet MS", 12))
calculate_opt.add_checkbutton(label="Kb", variable=kb_i, command=kb_calculation, font=("Trebuchet MS", 12))
calculate_opt.add_checkbutton(label="pKb", variable=pkb_i, command=pkb_calculation, font=("Trebuchet MS", 12))
calculate["menu"] = calculate_opt
calculate_opt.entryconfig("pH", state="disabled")
calculate_opt.entryconfig("pOH", state="disabled")
calculate_opt.entryconfig("Concentration of Hydrogen Ions", state="disabled")
calculate_opt.entryconfig("Concentration of Hydroxide Ions", state="disabled")
calculate_opt.entryconfig("Concentration of Salt", state="disabled")
calculate_opt.entryconfig("Ka", state="disabled")
calculate_opt.entryconfig("Kb", state="disabled")
calculate_opt.entryconfig("pKa", state="disabled")
calculate_opt.entryconfig("pKb", state="disabled")
calculate_label = tk.Label(root, text="Find :", bg="#91D8E4", fg="#FF0060", font=("Trebuchet MS", 12))
calculate_label.grid(row=2, column=0, pady=10, sticky="e")
# PH
ph_label = tk.Label(first_frame, text="pH", bg="#91D8E4", font=("Trebuchet MS", 12))
s_ph = tk.StringVar()
ph = tk.Entry(first_frame, highlightthickness=0, textvariable=s_ph, width=10, bg="#C5DFF8", relief="ridge",
              font=("Trebuchet MS", 12))
s_ph.trace_add("write", ph_calculation)
s_ph.trace_add("write", poh_calculation)
s_ph.trace_add("write", h_molarity_calculation)
s_ph.trace_add("write", oh_molarity_calculation)
s_ph.trace_add("write", salt_molarity_calculation)
s_ph.trace_add("write", ka_calculation)
s_ph.trace_add("write", kb_calculation)
s_ph.trace_add("write", pka_calculation)
s_ph.trace_add("write", pkb_calculation)
ph_dis = tk.Label(second_frame, bg="#91D8E4", font=("Trebuchet MS", 12))
# POH
poh_label = tk.Label(first_frame, text="pOH", bg="#91D8E4", font=("Trebuchet MS", 12))
s_poh = tk.StringVar()
poh = tk.Entry(first_frame, highlightthickness=0, textvariable=s_poh, width=10, bg="#C5DFF8", relief="ridge",
               font=("Trebuchet MS", 12))
s_poh.trace_add("write", ph_calculation)
s_poh.trace_add("write", poh_calculation)
s_poh.trace_add("write", h_molarity_calculation)
s_poh.trace_add("write", oh_molarity_calculation)
s_poh.trace_add("write", salt_molarity_calculation)
s_poh.trace_add("write", ka_calculation)
s_poh.trace_add("write", kb_calculation)
s_poh.trace_add("write", pka_calculation)
s_poh.trace_add("write", pkb_calculation)
poh_dis = tk.Label(second_frame, bg="#91D8E4", font=("Trebuchet MS", 12))
# [H+]
h_molarity_label = tk.Label(first_frame, text="[H+]", bg="#91D8E4", font=("Trebuchet MS", 12))
s_h_molarity = tk.StringVar()
h_molarity = tk.Entry(first_frame, highlightthickness=0, textvariable=s_h_molarity, width=10, bg="#C5DFF8",
                      relief="ridge", font=("Trebuchet MS", 12))
s_h_molarity.trace_add("write", ph_calculation)
s_h_molarity.trace_add("write", poh_calculation)
s_h_molarity.trace_add("write", h_molarity_calculation)
s_h_molarity.trace_add("write", oh_molarity_calculation)
s_h_molarity.trace_add("write", salt_molarity_calculation)
s_h_molarity.trace_add("write", ka_calculation)
s_h_molarity.trace_add("write", kb_calculation)
s_h_molarity.trace_add("write", pka_calculation)
s_h_molarity.trace_add("write", pkb_calculation)
h_molarity_dis = tk.Label(second_frame, bg="#91D8E4", font=("Trebuchet MS", 12))

# [OH-]
oh_molarity_label = tk.Label(first_frame, text="[OH-]", bg="#91D8E4", font=("Trebuchet MS", 12))
s_oh_molarity = tk.StringVar()
oh_molarity = tk.Entry(first_frame, highlightthickness=0, textvariable=s_oh_molarity, width=10, bg="#C5DFF8",
                       relief="ridge", font=("Trebuchet MS", 12))
s_oh_molarity.trace_add("write", ph_calculation)
s_oh_molarity.trace_add("write", poh_calculation)
s_oh_molarity.trace_add("write", h_molarity_calculation)
s_oh_molarity.trace_add("write", oh_molarity_calculation)
s_oh_molarity.trace_add("write", salt_molarity_calculation)
s_oh_molarity.trace_add("write", ka_calculation)
s_oh_molarity.trace_add("write", kb_calculation)
s_oh_molarity.trace_add("write", pka_calculation)
s_oh_molarity.trace_add("write", pkb_calculation)
oh_molarity_dis = tk.Label(second_frame, bg="#91D8E4", font=("Trebuchet MS", 12))
# [Salt]
salt_molarity_label = tk.Label(first_frame, text="[Salt]", bg="#91D8E4", font=("Trebuchet MS", 12))
s_salt_molarity = tk.StringVar()
salt_molarity = tk.Entry(first_frame, highlightthickness=0, textvariable=s_salt_molarity, width=10, bg="#C5DFF8",
                         relief="ridge", font=("Trebuchet MS", 12))
s_salt_molarity.trace_add("write", ph_calculation)
s_salt_molarity.trace_add("write", poh_calculation)
s_salt_molarity.trace_add("write", h_molarity_calculation)
s_salt_molarity.trace_add("write", oh_molarity_calculation)
s_salt_molarity.trace_add("write", salt_molarity_calculation)
s_salt_molarity.trace_add("write", ka_calculation)
s_salt_molarity.trace_add("write", kb_calculation)
s_salt_molarity.trace_add("write", pka_calculation)
s_salt_molarity.trace_add("write", pkb_calculation)
salt_molarity_dis = tk.Label(second_frame, bg="#91D8E4", font=("Trebuchet MS", 12))
# Ka
ka_label = tk.Label(first_frame, text="Ka", bg="#91D8E4", font=("Trebuchet MS", 12))
s_ka = tk.StringVar()
ka = tk.Entry(first_frame, highlightthickness=0, textvariable=s_ka, width=10, bg="#C5DFF8", relief="ridge",
              font=("Trebuchet MS", 12))
s_ka.trace_add("write", ph_calculation)
s_ka.trace_add("write", poh_calculation)
s_ka.trace_add("write", h_molarity_calculation)
s_ka.trace_add("write", oh_molarity_calculation)
s_ka.trace_add("write", salt_molarity_calculation)
s_ka.trace_add("write", ka_calculation)
s_ka.trace_add("write", kb_calculation)
s_ka.trace_add("write", pka_calculation)
s_ka.trace_add("write", pkb_calculation)
ka_dis = tk.Label(second_frame, bg="#91D8E4", font=("Trebuchet MS", 12))
# Kb
kb_label = tk.Label(first_frame, text="Kb", bg="#91D8E4", font=("Trebuchet MS", 12))
s_kb = tk.StringVar()
kb = tk.Entry(first_frame, highlightthickness=0, textvariable=s_kb, width=10, bg="#C5DFF8", relief="ridge",
              font=("Trebuchet MS", 12))
s_kb.trace_add("write", ph_calculation)
s_kb.trace_add("write", poh_calculation)
s_kb.trace_add("write", h_molarity_calculation)
s_kb.trace_add("write", oh_molarity_calculation)
s_kb.trace_add("write", salt_molarity_calculation)
s_kb.trace_add("write", ka_calculation)
s_kb.trace_add("write", kb_calculation)
s_kb.trace_add("write", pka_calculation)
s_kb.trace_add("write", pkb_calculation)
kb_dis = tk.Label(second_frame, bg="#91D8E4", font=("Trebuchet MS", 12))
# PKa
pka_label = tk.Label(first_frame, text="pKa", bg="#91D8E4", font=("Trebuchet MS", 12))
s_pka = tk.StringVar()
pka = tk.Entry(first_frame, highlightthickness=0, textvariable=s_pka, width=10, bg="#C5DFF8", relief="ridge",
               font=("Trebuchet MS", 12))
s_pka.trace_add("write", ph_calculation)
s_pka.trace_add("write", poh_calculation)
s_pka.trace_add("write", h_molarity_calculation)
s_pka.trace_add("write", oh_molarity_calculation)
s_pka.trace_add("write", salt_molarity_calculation)
s_pka.trace_add("write", ka_calculation)
s_pka.trace_add("write", kb_calculation)
s_pka.trace_add("write", pka_calculation)
s_pka.trace_add("write", pkb_calculation)
pka_dis = tk.Label(second_frame, bg="#91D8E4", font=("Trebuchet MS", 12))
# PKb
pkb_label = tk.Label(first_frame, text="pKb", bg="#91D8E4", font=("Trebuchet MS", 12))
s_pkb = tk.StringVar()
pkb = tk.Entry(first_frame, highlightthickness=0, textvariable=s_pkb, width=10, bg="#C5DFF8", relief="ridge",
               font=("Trebuchet MS", 12))
s_pkb.trace_add("write", ph_calculation)
s_pkb.trace_add("write", poh_calculation)
s_pkb.trace_add("write", h_molarity_calculation)
s_pkb.trace_add("write", oh_molarity_calculation)
s_pkb.trace_add("write", salt_molarity_calculation)
s_pkb.trace_add("write", ka_calculation)
s_pkb.trace_add("write", kb_calculation)
s_pkb.trace_add("write", pka_calculation)
s_pkb.trace_add("write", pkb_calculation)
pkb_dis = tk.Label(second_frame, bg="#91D8E4", font=("Trebuchet MS", 12))
# Result_Label
res_label = tk.Label(second_frame, text="Result", bg="#91D8E4", fg="#FF0060", font=("Trebuchet MS", 12))
res_label.grid(row=0, column=0, padx=10, pady=10, sticky="n")
# Consistency
space1 = tk.Label(first_frame, bg="#91D8E4", font=("Trebuchet MS", 12))
space1.grid(row=0, column=0, columnspan=2, pady=10, sticky="w")
space2 = tk.Label(second_frame, bg="#91D8E4", font=("Trebuchet MS", 12))
space2.grid(row=1, column=0, pady=10, sticky="w")
# Running
root.mainloop()
