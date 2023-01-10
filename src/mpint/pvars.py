"""
mpint.pvars
----------
MPint variables = classes + methods for global variables.
"""

import numpy as np
import pandas as pd

class peak:
    """
    This class defines peak objects
    = containers for important peak properties.
    """
    
    def __init__(self, x_pos, x_min, x_max):
        """
        Initialize properties of peak.

        Parameters
        ----------
        x_pos : float
            X-position of the peak center.
        x_min : float
            X-position of the left/minimal border of the peak.
        x_max : float
            X-position of the right/maximal border of the peak.

        Returns
        -------
        * Peak object defined by three properties (x_pos, x_min, x_max).
        * Other properties (ymin, ymax, peak_area...) are set to None.
        * These properties are to be calculated later.
        """
        self.x_pos = x_pos
        self.x_min = x_min
        self.x_max = x_max
        self.y_min = None
        self.y_max = None
        self.area  = None
        
    def __str__(self):
        """
        Overwritten __str__ method to get nice output with print.
        """
        # Define output lines
        lines = [
            f'* Peak at position = {self.x_pos}',
            f'x_min, x_max = {self.x_min}, {self.x_max}']
        # Format of additional output lines differs if the parameters were set
        # (None values cannot be formated as floats
        if self.y_min != None and self.y_max != None and self.area != None:
            lines.append(f'y_min, y_max = {self.y_min:.3f}, {self.y_max:.3f}')
            lines.append(f'Integrated peak area = {self.area:.3f}')
        else:
            lines.append('The peak has not been integrated yet!')
        # Add initial space in front of each output line
        lines = ['  '+line for line in lines]
        # Combine lines into one string
        text  = '\n'.join(lines)
        # Return the final string
        return(text)
        
    def integrate(self, XYdata):
        """
        Integrate peak = calculate area of the peak.

        Parameters
        ----------
        XYdata : 2D numpy array
            XY-data = data defining the spectrum.
            
        Returns
        -------
        None.
            The integrated peak area is just saved in object property
            self.area.
        """
        # Split spectrum = XYdata to X,Ydata
        Xdata,Ydata = XYdata[0],XYdata[1]
        # Find limits for integration = indexes of xmin and xmax in Xdata
        i_min = peak.find_nearest(Xdata, self.x_min)
        i_max = peak.find_nearest(Xdata, self.x_max)
        # Save the limits to object properties
        self.y_min = Ydata[i_min]
        self.y_max = Ydata[i_max]
        # Calcululate linear background: y = m*x + n
        xmin,xmax = Xdata[i_min],Xdata[i_max]
        ymin,ymax = Ydata[i_min],Ydata[i_max]
        m = (ymax - ymin) / (xmax - xmin)
        n = ymin - xmin * m
        # Calculate area of the peak
        net_area = np.sum(Ydata[i_min:i_max+1])
        bkg_area = np.sum(Xdata[i_min:i_max+1] * m + n)
        # Save the calclated area to object property
        self.area = net_area - bkg_area
        
    def find_nearest(arr, value):
        '''
        Find index of the element with the nearest `value` in 1D-array.
        
        Parameters
        ----------
        arr : 1D numpy array
            * The array, in which we search the element with closest value.          
            * IMPORTANT prerequisite: the array is sorted from min to max.
        value : float
            The value, for which we search the closest element.
    
        Returns
        -------
        idx : int
            Index of the element with the closest value.
        '''
        # Find index of the element with nearest value in 1D-array.
        # Important prerequisite: the array must be sorted.
        # https://stackoverflow.com/q/2566412
        # 1) Key step = np.searchsorted
        idx = np.searchsorted(arr, value, side="left")
        # 2) finalization = consider special cases and return final value
        if idx > 0 and (
                idx == len(arr) or abs(value-arr[idx-1]) < abs(value-arr[idx])):
            return(idx-1)
        else:
            return(idx)

class table_of_results():
    """
    This class defines `table_of_results` object,
    which is used to collect and save the calculation results in one place.
    This object contains methods for easy appending, printing and saving data.
    """

    def __init__(self):
        self.df = pd.DataFrame()

    def append_row(self, filename, indexes):
        """
        * Append one row to table_of_results.
        * One row in table_of_results = one processed spectrum.
        * One row = [filename of spectrum] + [all calculated indexes].

        Parameters
        ----------
        filename : string
            Name of the spectrum, from which the indexes were calculated.
        indexes : dict
            Dictionary of indexes calculated from given spectrum.

        Returns
        -------
        self: table_of_results object
            Table_of_results after modification = with the appended row.
        """
        # If we add to an emtpy DataFrame, initialize columns
        # (reason: we want to have the columns in specific order
        if self.df.empty :
            self.df = pd.DataFrame(columns = indexes.keys())
        # Add new series to the end of dataframe
        self.df.loc[filename] = indexes
        return(self)
    
    def print_table(self):
        """
        Print `table_of_results`.

        Returns
        -------
        None.
            The method just prints the table_of_results to stdout.
        """
        s = self.df.to_string(float_format='%7.3f')
        print(s)
    
    def save_as_txt(self, output_filename):
        """
        Save `table_of_results` as TXT-file.

        Parameters
        ----------
        output_filename : str or pathlib object
            Name of the output file.

        Returns
        -------
        None.
            The method just saves the table_of_results to TXT-file.
        """
        # s = self.df.to_string(float_format='%7.3f')
        s = self.df.to_string()
        with open(output_filename, 'w') as f: f.write(s)
    
    def save_as_png(self, output_filename):
        """
        Save `table_of_results` as a simple PNG graph.

        Parameters
        ----------
        output_filename : str or pathlib object
            Name of the output PNG file.

        Returns
        -------
        None.
            The method just saves the table_of_results as of PNG-graph.
        """
        ymax = np.max(self.df.max()) * 1.1
        ax = self.df.plot(use_index=False)
        ax.set_title('Final calculated indexes')
        ax.set_xlabel('Number of spectrum')
        ax.set_ylabel('Indexes')
        ax.set_ylim(0,ymax)
        ax.grid()
        ax.legend(bbox_to_anchor=(1.04,1), loc='upper left', handlelength=1)
        fig = ax.get_figure()
        fig.tight_layout()
        fig.savefig(output_filename, dpi=100)
        
