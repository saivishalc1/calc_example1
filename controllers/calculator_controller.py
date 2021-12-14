"""R"""
from flask import render_template, request, flash
from app.controllers.controller import ControllerBase
from calc.calculator import Calculator


class CalculatorController(ControllerBase):
    """R"""

    @staticmethod
    def post():
        """R"""
        if request.form['value1'] == '' or request.form['value2'] == '':
            error = 'You must enter a value for value 1 and or value 2'
        else:
            flash('You successfully calculated')
            flash('You are awesome')

            # get the values out of the form
            value1 = request.form['value1']
            value2 = request.form['value2']
            operation = request.form['operation']
            # make the tuple
            my_tuple = (value1, value2)
            # this will call the correct operation
            getattr(Calculator, operation)(my_tuple)
            result = str(Calculator.get_last_result_value())
            return render_template('result.html',
                                   value1=value1,value2=value2,operation=operation,result=result)
        return render_template('calculator2.html', error=error)

    @staticmethod
    def get():
        """R"""
        return render_template('calculator2.html')
