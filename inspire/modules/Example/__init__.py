from inspire import app, db
from flask import Flask, request, flash, redirect, url_for, render_template, g, session
from database import populate_tables, upgrade_tables
from config import visible, public_name, internal_name, blueprint
import pages
import conspyre

