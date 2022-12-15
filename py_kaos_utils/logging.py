import logging
from dataclasses import dataclass, field
from logging import Logger

logger = logging.getLogger()


@dataclass
class ProgressLogger:
    count_total: int
    checkpoints: int = 10
    logger: Logger = logger
    count_processed: int = field(default=0, repr=False, init=False)
    _checkpoints_log: list = field(default_factory=list, repr=False, init=False)

    @property
    def _each_checkpoint_length(self):
        return (self.count_total // self.checkpoints) + 1

    def report_progress(self):
        checkpoint = self.count_processed // self._each_checkpoint_length
        if checkpoint > len(self._checkpoints_log):
            logger.info(f"{checkpoint / self.checkpoints:.0%} there: {self.count_processed}/{self.count_total}")
            self._checkpoints_log.append(self.count_processed)

    def log_progress(self, count_this_round, report=True):
        self.count_processed += count_this_round
        if report:
            self.report_progress()


__all__ = (
    'ProgressLogger',
)
