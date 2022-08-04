from mangum import Mangum
from app.main import app
import uvicorn


###############################################################################
#   Run the self contained application                                        #
###############################################################################
handler = Mangum(app)

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=5000)