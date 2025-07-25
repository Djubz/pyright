import time
from _typeshed import FileDescriptorOrPath
from collections.abc import Callable, Iterable
from logging import Logger
from typing import Any

from .context import Context
from .emitters.udp_emitter import UDPEmitter
from .models.default_dynamic_naming import DefaultDynamicNaming
from .models.dummy_entities import DummySegment, DummySubsegment
from .models.segment import Segment, SegmentContextManager
from .models.subsegment import Subsegment, SubsegmentContextManager
from .sampling.local.sampler import LocalSampler
from .sampling.sampler import DefaultSampler
from .streaming.default_streaming import DefaultStreaming

log: Logger
TRACING_NAME_KEY: str
DAEMON_ADDR_KEY: str
CONTEXT_MISSING_KEY: str
XRAY_META: dict[str, dict[str, str]]
SERVICE_INFO: dict[str, str]

class AWSXRayRecorder:
    def __init__(self) -> None: ...
    def configure(
        self,
        sampling: bool | None = None,
        plugins: Iterable[str] | None = None,
        context_missing: str | None = None,
        sampling_rules: dict[str, Any] | FileDescriptorOrPath | None = None,
        daemon_address: str | None = None,
        service: str | None = None,
        context: Context | None = None,
        emitter: UDPEmitter | None = None,
        streaming: DefaultStreaming | None = None,
        dynamic_naming: DefaultDynamicNaming | None = None,
        streaming_threshold: int | None = None,
        max_trace_back: int | None = None,
        sampler: LocalSampler | DefaultSampler | None = None,
        stream_sql: bool | None = True,
    ) -> None: ...
    def in_segment(self, name: str | None = None, **segment_kwargs) -> SegmentContextManager: ...
    def in_subsegment(self, name: str | None = None, **subsegment_kwargs) -> SubsegmentContextManager: ...
    def begin_segment(
        self, name: str | None = None, traceid: str | None = None, parent_id: str | None = None, sampling: bool | None = None
    ) -> Segment | DummySegment: ...
    def end_segment(self, end_time: time.struct_time | None = None) -> None: ...
    def current_segment(self) -> Segment: ...
    def begin_subsegment(self, name: str, namespace: str = "local") -> DummySubsegment | Subsegment | None: ...
    def begin_subsegment_without_sampling(self, name: str) -> DummySubsegment | Subsegment | None: ...
    def current_subsegment(self) -> Subsegment | DummySubsegment | None: ...
    def end_subsegment(self, end_time: time.struct_time | None = None) -> None: ...
    def put_annotation(self, key: str, value: Any) -> None: ...
    def put_metadata(self, key: str, value: Any, namespace: str = "default") -> None: ...
    def is_sampled(self) -> bool: ...
    def get_trace_entity(self) -> Segment | Subsegment | DummySegment | DummySubsegment: ...
    def set_trace_entity(self, trace_entity: Segment | Subsegment | DummySegment | DummySubsegment) -> None: ...
    def clear_trace_entities(self) -> None: ...
    def stream_subsegments(self) -> None: ...
    def capture(self, name: str | None = None) -> SubsegmentContextManager: ...
    def record_subsegment(
        self,
        wrapped: Callable[..., Any],
        instance: Any,
        args: list[Any],
        kwargs: dict[str, Any],
        name: str,
        namespace: str,
        meta_processor: Callable[..., object],
    ) -> Any: ...
    @property
    def enabled(self) -> bool: ...
    @enabled.setter
    def enabled(self, value: bool) -> None: ...
    @property
    def sampling(self) -> bool: ...
    @sampling.setter
    def sampling(self, value: bool) -> None: ...
    @property
    def sampler(self) -> LocalSampler | DefaultSampler: ...
    @sampler.setter
    def sampler(self, value: LocalSampler | DefaultSampler) -> None: ...
    @property
    def service(self) -> str: ...
    @service.setter
    def service(self, value: str) -> None: ...
    @property
    def dynamic_naming(self) -> DefaultDynamicNaming | None: ...
    @dynamic_naming.setter
    def dynamic_naming(self, value: DefaultDynamicNaming | str) -> None: ...
    @property
    def context(self) -> Context: ...
    @context.setter
    def context(self, cxt: Context) -> None: ...
    @property
    def emitter(self) -> UDPEmitter: ...
    @emitter.setter
    def emitter(self, value: UDPEmitter) -> None: ...
    @property
    def streaming(self) -> DefaultStreaming: ...
    @streaming.setter
    def streaming(self, value: DefaultStreaming) -> None: ...
    @property
    def streaming_threshold(self) -> int: ...
    @streaming_threshold.setter
    def streaming_threshold(self, value: int) -> None: ...
    @property
    def max_trace_back(self) -> int: ...
    @max_trace_back.setter
    def max_trace_back(self, value: int) -> None: ...
    @property
    def stream_sql(self) -> bool: ...
    @stream_sql.setter
    def stream_sql(self, value: bool) -> None: ...
