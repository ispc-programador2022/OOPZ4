from google_sheet.spreadsheet import send_data_sheets
from logic.functions import post_scrapings_to_database, get_scrapings_list_values
from scrap.bloomberg_scrap import Bloomberg
from scrap.cme_scrap import Cme
from scrap.dollar_scrap import Dollar

if __name__ == '__main__':
    dollar, cme, bloomberg = Dollar(), Cme(), Bloomberg()

    # Valores de retorno de los Scrapings
    scrap_dollar = dollar.get_data_from_pages()
    scrap_cme = cme.get_data_from_pages()
    scrap_bloomberg = bloomberg.get_data_from_pages()

    # Cargo los scrapings a la base de datos
    post_scrapings_to_database(scrap_dollar=scrap_dollar, scrap_cme=scrap_cme, scrap_bloomberg=scrap_bloomberg)

    # Retorno los Scrapings en formato de Lista
    data_scraping = get_scrapings_list_values()
    
    # Envio la fila nueva a google sheets
    send_data_sheets(data_scraping)
