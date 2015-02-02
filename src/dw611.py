#!/usr/bin/env python
import os
from scad import *

class Deflector(SCAD_Object):
    outer_dia = 75
    inner_dia = 41.5
    thickness = 11
    #
    spindle_inner_dia = 26
    spindle_dia = inner_dia
    spindle_thickness = thickness - 2
    #
    led_offset_x = 26
    led_dia = 8.5
    #
    screw_y_offset = 25.3
    screw_x_offset = 10.25
    screw_dia = 4.7
    screw_head_height = 4.1
    screw_head_dia = 7
    #
    port_width = 8
    port_depth = 10
    port_height = 4
    #
    vacuum_dia = inch2mm(1.25)
    vacuum_plate_dia = vacuum_dia + 20
    vacuum_flag = True
    vacuum_offset = 5.0
    #
    magnet_dia = inch2mm(.25) + 0.2
    magnet_height = inch2mm(1 / 16.0)
    magnet_offset = 2.0
    #
    screw_spacer_dia = inch2mm(0.345)
    screw_spacer_height = 2.4

    def ports(self):
        body = Pipe(od1=self.outer_dia + 20.0, od2=self.inner_dia, iD=self.inner_dia + 2.0, h=self.thickness - 2.95, center=True, padding=1.2)
        points = [[-12, 0], [12, 0], [self.screw_x_offset + self.screw_dia + 8.0, -20], [-self.screw_x_offset - self.screw_dia - 8.0, -20]]
        screw_plate = Polygon(points=points)
        screw_plate = LinearExtrude(h=self.thickness)(screw_plate)
        screw_plate = Translate(y=-18, z=self.thickness / -2.0)(screw_plate)
        led_plate = Cube(x=self.outer_dia, y=self.led_dia + 5.0, z=self.thickness, center=True)
        plates = Union()(led_plate, screw_plate)
        port = Difference()(body, led_plate, screw_plate)
        return port

    def body(self):
        body = Cylinder(dia=self.outer_dia, h=self.thickness, center=True, padding=1.2)
        if self.vacuum_flag:
            x_offset = (self.outer_dia + self.vacuum_dia) / 2.0 + self.vacuum_offset
            vacuum_plate = Cylinder(dia=self.vacuum_plate_dia, h=self.thickness, center=True)
            vacuum_plate = Translate(x=x_offset)(vacuum_plate)
            vacuum_port = Cylinder(dia=self.vacuum_dia, h=self.thickness + 2.0, center=True)
            vacuum_port = Translate(x=x_offset)(vacuum_port)
            body = Hull()(body, vacuum_plate)
            body = Difference()(body, vacuum_port)
        spindle_hole = Cylinder(dia=self.inner_dia, h=self.thickness + 2.0, center=True)
        body = Difference()(body, spindle_hole)
        return body

    def magnets(self):
        if not self.vacuum_flag:
            return Union()()
        magnet = Cylinder(dia=self.magnet_dia, h=self.magnet_height, center=True)
        magnet = Translate(z=(self.thickness - self.magnet_height) / 2.0 + 0.1)(magnet)
        x_offset = (self.outer_dia + self.vacuum_dia) / 2.0 + self.vacuum_offset
        y_offset = (self.vacuum_plate_dia - self.magnet_dia) / 2.0 - self.magnet_offset
        m1 = Translate(y=y_offset, x=x_offset)(magnet)
        m2 = Translate(y=-y_offset, x=x_offset)(magnet)
        x_offset = (self.outer_dia - self.magnet_dia) / 2.0 - self.magnet_offset
        m3 = Translate(y=x_offset)(magnet)
        m4 = Translate(y=-x_offset)(magnet)
        magnets = Union()(m1, m2, m3, m4)
        return magnets

    def scad(self):
        body = self.body()
        spindle = Pipe(od=self.spindle_dia, iD=self.spindle_inner_dia, h=self.spindle_thickness, center=True, padding=1.2)
        spindle = Translate(z=(self.thickness - self.spindle_thickness) / 2.0)(spindle)
        body = Union()(spindle, body)
        # leds
        led = Cylinder(d1=self.led_dia, d2=self.led_dia + 5.0, h=self.thickness + 2, center=True)
        led1 = Translate(x=self.led_offset_x)(led)
        led2 = Translate(x=-self.led_offset_x)(led)
        # screws
        screw = Cylinder(d=self.screw_dia, h=self.thickness + 2, center=True)
        screw_head = Cylinder(d=self.screw_head_dia, h=self.screw_head_height, center=True)
        screw_head = Translate(z=(self.thickness - self.screw_head_height) / 2.0)(screw_head)
        screw = Union()(screw, screw_head)
        sh1 = Translate(x=self.screw_x_offset, y=-self.screw_y_offset)(screw)
        sh2 = Translate(x=-self.screw_x_offset, y=-self.screw_y_offset)(screw)
        # ports
        ports = self.ports()
        ports = Translate(z=self.thickness / -2.0 + 4.0)(ports)
        # magnets
        magnets = self.magnets()
        deflector = Difference()(body, sh1, sh2, led1, led2, ports, magnets)
        # spacer
        screw_spacer = Pipe(iD=self.screw_dia, od=self.screw_spacer_dia, h=self.screw_spacer_height, center=True)
        z_offset = (self.thickness + self.screw_spacer_height) / -2.0
        sp1 = Translate(x=self.screw_x_offset, y=-self.screw_y_offset, z=z_offset)(screw_spacer)
        sp2 = Translate(x=-self.screw_x_offset, y=-self.screw_y_offset, z=z_offset)(screw_spacer)
        deflector = Union()(deflector, sp1, sp2)
        deflector = SCAD_Globals(fn=40)(deflector)
        return deflector

def render(obj, fn):
    scad_fn = fn + ".scad"
    stl_fn = fn + ".stl"
    obj.render(scad_fn)
    if not os.path.exists(stl_fn):
        obj.render(stl_fn)

deflector = Deflector(vacuum_flag=False)
render(deflector, "dw611_deflector")
deflector = Deflector(vacuum_flag=True)
render(deflector, "dw611_deflector_vacuum")

