---
layout: page
title: Tutorial (RTM Seminar, Part 4)
---

<!-- Title: Tutorial (RTM Seminar, Part 4) -->
#contents

## Introduction

This page explains how to verify the operation of RTCs using the RTC for LibreOffice Calc.

You can check the behavior of a target RTC by entering values from Calc cells into an InPort and displaying values output from an OutPort in Calc cells.

<div align="center"><a href="calc1.png"><img src="calc1.png" width="70%;"></a></div>

In the RTM seminar, a portable version of LibreOffice and RTCs are distributed on a USB memory stick.

They can be run on Windows.

Ubuntu is not supported because there is no omniORB package for Python 3. Laptops will be provided during the seminar.

In this exercise, we use the RobotController component created in [Part 2]({{ site.baseurl }}/ja/doc/casestudy/raspberrypi_mouse/raspimouse_tutorial_rtm_seminar/tutorial_rtm_seminar_win_part2).

## What is LibreOffice?

LibreOffice is an office suite that provides spreadsheet, presentation, and word processing functions.

It is distributed as free software, and in this seminar we use the following portable version.

- [Portable Version: LibreOffice Portable](https://ja.libreoffice.org/download/portable-versions/)

## Starting the RTC for LibreOffice Calc

Run **Portable LibreOffice\run_CalcRTC.bat** from the distributed USB memory stick.

LibreOffice Calc will start. Click the **Start RTC** button to launch the RTC named **OOoCalcControl**.

<div align="center"><a href="calc2.png"><img src="calc2.png" width="50%;"></a></div>

## Connecting an OutPort

Connect the RobotController OutPort so that output data can be monitored in Calc.

Click the **Launch Control Dialog** button in Calc.

<div align="center"><a href="calc3.png"><img src="calc3.png" width="50%;"></a></div>

First, connect to the OutPort whose output data you want to monitor.

Click the **Tree View** button to display the list of RTC ports registered in the Name Server, then select **RobotController0 → out** from the tree.

<div align="center"><a href="calc4.png"><img src="calc4.png" width="50%;"></a></div>

Next, change some settings.

Uncheck **Move Columns**.

When this option is enabled, the cell position moves every time data is received.

This mode is useful when plotting graphs, but for this exercise we only want to monitor values, so disable it.

Enter **C** in the box to the right of **Column Number**.

This will display the OutPort output data in columns **A** through **C** of row **2**.

After completing the settings, click the **Create** button.

<div align="center"><a href="calc9.png"><img src="calc9.png" width="50%;"></a></div>

## Verifying OutPort Operation

Activate the RTC in RT System Editor and verify its operation.

<div align="center"><a href="calc6.png"><img src="calc6.png" width="70%;"></a></div>

While the RTC is active, change the configuration parameters and verify that the values displayed in the Calc cells change accordingly.

<div align="center"><a href="calc7.png"><img src="calc7.png" width="70%;"></a></div>

## Connecting an InPort

Connect the RobotController InPort so that data can be entered from Calc.

Click the **Tree View** button to display the list of RTC ports registered in the Name Server, then select **RobotController0 → in** from the tree.

<div align="center"><a href="calc8.png"><img src="calc8.png" width="50%;"></a></div>

Next, change some settings.

Uncheck **Move Columns**.

''''
Enter **D** in the box to the right of **Column Number**.

This will display the OutPort output data in columns **A** through **C** of row **3**.

After completing the settings, click the **Create** button.

<div align="center"><a href="calc12.png"><img src="calc12.png" width="50%;"></a></div>

## Verifying InPort Operation

Activate the RTC in RT System Editor and verify its operation.

While the RTC is active, configure it so that a forward velocity is output through the OutPort.

Then, enter either **1** or **0** into columns **A** and **B** of row **3** in Calc, and verify that the behavior changes accordingly.

<div align="center"><a href="calc13.png"><img src="calc13.png" width="70%;"></a></div>
