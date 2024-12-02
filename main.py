from mlProject import logger
from mlProject.pipeline.stage_01_data_ingestion import DataIngetionTrainingPipeline

STAGE_NAME="Data Ingestion Stage"
try:
        logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
        obj=DataIngetionTrainingPipeline()
        obj.main()
        logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx======x")
except Exception as e:
    logger.exception(e)
    raise e
