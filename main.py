import click
from data_processing.input_handler import input_handler, list_excel_files
from data_processing.coord_excel_handler import *
from data_processing.make_periodic_table import periodic_table
from make_data import *
from display_data import *
from data_processing.compound_object import pick_what_separate  

@click.command()
def main():
    """
    Processes Excel file and visualizes binary compounds via periodic table.
    Maintained by Brian Hoang & Danila Shiryaev.
    """

    # Get the file_path from the user's selection
    file_path = list_excel_files()
    if not file_path:
        return  # Exit if no valid file is chosen

    # Process the selected Excel file
    user_input_sheet_numbers = input_handler(file_path)
    coord_df, coord_sheet_name = excel_to_dataframe()
    element_dict = create_element_dict(coord_df)
    periodic_table_ax = periodic_table(coord_df, coord_sheet_name)

    # Generate the compound data
    compounds = make_binary_data(file_path, user_input_sheet_numbers)
    target_element = pick_what_separate()
    if target_element:
        for compound in compounds:
            compound.separate_by_element(target_element)
        # Sort compounds to move modified structures with "(with {element})" to the end
        compounds.sort(key=lambda x: f"(with {target_element})" in x.structure)
    display_binary_data_type(periodic_table_ax, compounds, element_dict, coord_sheet_name)

    return 0


if __name__ == '__main__':
    main()