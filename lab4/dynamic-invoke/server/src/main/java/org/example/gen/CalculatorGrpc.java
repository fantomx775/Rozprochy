package org.example.gen;

import static io.grpc.MethodDescriptor.generateFullMethodName;

/**
 */
@javax.annotation.Generated(
    value = "by gRPC proto compiler (version 1.62.2)",
    comments = "Source: calculator.proto")
@io.grpc.stub.annotations.GrpcGenerated
public final class CalculatorGrpc {

  private CalculatorGrpc() {}

  public static final java.lang.String SERVICE_NAME = "calculator.Calculator";

  // Static method descriptors that strictly reflect the proto.
  private static volatile io.grpc.MethodDescriptor<org.example.gen.ArithmeticOpArguments,
      org.example.gen.ArithmeticOpResult> getAddMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "Add",
      requestType = org.example.gen.ArithmeticOpArguments.class,
      responseType = org.example.gen.ArithmeticOpResult.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<org.example.gen.ArithmeticOpArguments,
      org.example.gen.ArithmeticOpResult> getAddMethod() {
    io.grpc.MethodDescriptor<org.example.gen.ArithmeticOpArguments, org.example.gen.ArithmeticOpResult> getAddMethod;
    if ((getAddMethod = CalculatorGrpc.getAddMethod) == null) {
      synchronized (CalculatorGrpc.class) {
        if ((getAddMethod = CalculatorGrpc.getAddMethod) == null) {
          CalculatorGrpc.getAddMethod = getAddMethod =
              io.grpc.MethodDescriptor.<org.example.gen.ArithmeticOpArguments, org.example.gen.ArithmeticOpResult>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "Add"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  org.example.gen.ArithmeticOpArguments.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  org.example.gen.ArithmeticOpResult.getDefaultInstance()))
              .setSchemaDescriptor(new CalculatorMethodDescriptorSupplier("Add"))
              .build();
        }
      }
    }
    return getAddMethod;
  }

  private static volatile io.grpc.MethodDescriptor<org.example.gen.ArithmeticOpArguments,
      org.example.gen.ArithmeticOpResult> getSubtractMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "Subtract",
      requestType = org.example.gen.ArithmeticOpArguments.class,
      responseType = org.example.gen.ArithmeticOpResult.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<org.example.gen.ArithmeticOpArguments,
      org.example.gen.ArithmeticOpResult> getSubtractMethod() {
    io.grpc.MethodDescriptor<org.example.gen.ArithmeticOpArguments, org.example.gen.ArithmeticOpResult> getSubtractMethod;
    if ((getSubtractMethod = CalculatorGrpc.getSubtractMethod) == null) {
      synchronized (CalculatorGrpc.class) {
        if ((getSubtractMethod = CalculatorGrpc.getSubtractMethod) == null) {
          CalculatorGrpc.getSubtractMethod = getSubtractMethod =
              io.grpc.MethodDescriptor.<org.example.gen.ArithmeticOpArguments, org.example.gen.ArithmeticOpResult>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "Subtract"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  org.example.gen.ArithmeticOpArguments.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  org.example.gen.ArithmeticOpResult.getDefaultInstance()))
              .setSchemaDescriptor(new CalculatorMethodDescriptorSupplier("Subtract"))
              .build();
        }
      }
    }
    return getSubtractMethod;
  }

  private static volatile io.grpc.MethodDescriptor<org.example.gen.ComplexArithmeticOpArguments,
      org.example.gen.ComplexArithmeticOpResult> getComplexOperationMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "ComplexOperation",
      requestType = org.example.gen.ComplexArithmeticOpArguments.class,
      responseType = org.example.gen.ComplexArithmeticOpResult.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<org.example.gen.ComplexArithmeticOpArguments,
      org.example.gen.ComplexArithmeticOpResult> getComplexOperationMethod() {
    io.grpc.MethodDescriptor<org.example.gen.ComplexArithmeticOpArguments, org.example.gen.ComplexArithmeticOpResult> getComplexOperationMethod;
    if ((getComplexOperationMethod = CalculatorGrpc.getComplexOperationMethod) == null) {
      synchronized (CalculatorGrpc.class) {
        if ((getComplexOperationMethod = CalculatorGrpc.getComplexOperationMethod) == null) {
          CalculatorGrpc.getComplexOperationMethod = getComplexOperationMethod =
              io.grpc.MethodDescriptor.<org.example.gen.ComplexArithmeticOpArguments, org.example.gen.ComplexArithmeticOpResult>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "ComplexOperation"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  org.example.gen.ComplexArithmeticOpArguments.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  org.example.gen.ComplexArithmeticOpResult.getDefaultInstance()))
              .setSchemaDescriptor(new CalculatorMethodDescriptorSupplier("ComplexOperation"))
              .build();
        }
      }
    }
    return getComplexOperationMethod;
  }

  private static volatile io.grpc.MethodDescriptor<org.example.gen.BatchOperationRequest,
      org.example.gen.BatchOperationResult> getPerformBatchOperationMethod;

  @io.grpc.stub.annotations.RpcMethod(
      fullMethodName = SERVICE_NAME + '/' + "PerformBatchOperation",
      requestType = org.example.gen.BatchOperationRequest.class,
      responseType = org.example.gen.BatchOperationResult.class,
      methodType = io.grpc.MethodDescriptor.MethodType.UNARY)
  public static io.grpc.MethodDescriptor<org.example.gen.BatchOperationRequest,
      org.example.gen.BatchOperationResult> getPerformBatchOperationMethod() {
    io.grpc.MethodDescriptor<org.example.gen.BatchOperationRequest, org.example.gen.BatchOperationResult> getPerformBatchOperationMethod;
    if ((getPerformBatchOperationMethod = CalculatorGrpc.getPerformBatchOperationMethod) == null) {
      synchronized (CalculatorGrpc.class) {
        if ((getPerformBatchOperationMethod = CalculatorGrpc.getPerformBatchOperationMethod) == null) {
          CalculatorGrpc.getPerformBatchOperationMethod = getPerformBatchOperationMethod =
              io.grpc.MethodDescriptor.<org.example.gen.BatchOperationRequest, org.example.gen.BatchOperationResult>newBuilder()
              .setType(io.grpc.MethodDescriptor.MethodType.UNARY)
              .setFullMethodName(generateFullMethodName(SERVICE_NAME, "PerformBatchOperation"))
              .setSampledToLocalTracing(true)
              .setRequestMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  org.example.gen.BatchOperationRequest.getDefaultInstance()))
              .setResponseMarshaller(io.grpc.protobuf.ProtoUtils.marshaller(
                  org.example.gen.BatchOperationResult.getDefaultInstance()))
              .setSchemaDescriptor(new CalculatorMethodDescriptorSupplier("PerformBatchOperation"))
              .build();
        }
      }
    }
    return getPerformBatchOperationMethod;
  }

  /**
   * Creates a new async stub that supports all call types for the service
   */
  public static CalculatorStub newStub(io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<CalculatorStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<CalculatorStub>() {
        @java.lang.Override
        public CalculatorStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new CalculatorStub(channel, callOptions);
        }
      };
    return CalculatorStub.newStub(factory, channel);
  }

  /**
   * Creates a new blocking-style stub that supports unary and streaming output calls on the service
   */
  public static CalculatorBlockingStub newBlockingStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<CalculatorBlockingStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<CalculatorBlockingStub>() {
        @java.lang.Override
        public CalculatorBlockingStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new CalculatorBlockingStub(channel, callOptions);
        }
      };
    return CalculatorBlockingStub.newStub(factory, channel);
  }

  /**
   * Creates a new ListenableFuture-style stub that supports unary calls on the service
   */
  public static CalculatorFutureStub newFutureStub(
      io.grpc.Channel channel) {
    io.grpc.stub.AbstractStub.StubFactory<CalculatorFutureStub> factory =
      new io.grpc.stub.AbstractStub.StubFactory<CalculatorFutureStub>() {
        @java.lang.Override
        public CalculatorFutureStub newStub(io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
          return new CalculatorFutureStub(channel, callOptions);
        }
      };
    return CalculatorFutureStub.newStub(factory, channel);
  }

  /**
   */
  public interface AsyncService {

    /**
     */
    default void add(org.example.gen.ArithmeticOpArguments request,
        io.grpc.stub.StreamObserver<org.example.gen.ArithmeticOpResult> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getAddMethod(), responseObserver);
    }

    /**
     */
    default void subtract(org.example.gen.ArithmeticOpArguments request,
        io.grpc.stub.StreamObserver<org.example.gen.ArithmeticOpResult> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getSubtractMethod(), responseObserver);
    }

    /**
     */
    default void complexOperation(org.example.gen.ComplexArithmeticOpArguments request,
        io.grpc.stub.StreamObserver<org.example.gen.ComplexArithmeticOpResult> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getComplexOperationMethod(), responseObserver);
    }

    /**
     * <pre>
     * New rpc for batch operation
     * </pre>
     */
    default void performBatchOperation(org.example.gen.BatchOperationRequest request,
        io.grpc.stub.StreamObserver<org.example.gen.BatchOperationResult> responseObserver) {
      io.grpc.stub.ServerCalls.asyncUnimplementedUnaryCall(getPerformBatchOperationMethod(), responseObserver);
    }
  }

  /**
   * Base class for the server implementation of the service Calculator.
   */
  public static abstract class CalculatorImplBase
      implements io.grpc.BindableService, AsyncService {

    @java.lang.Override public final io.grpc.ServerServiceDefinition bindService() {
      return CalculatorGrpc.bindService(this);
    }
  }

  /**
   * A stub to allow clients to do asynchronous rpc calls to service Calculator.
   */
  public static final class CalculatorStub
      extends io.grpc.stub.AbstractAsyncStub<CalculatorStub> {
    private CalculatorStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected CalculatorStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new CalculatorStub(channel, callOptions);
    }

    /**
     */
    public void add(org.example.gen.ArithmeticOpArguments request,
        io.grpc.stub.StreamObserver<org.example.gen.ArithmeticOpResult> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getAddMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void subtract(org.example.gen.ArithmeticOpArguments request,
        io.grpc.stub.StreamObserver<org.example.gen.ArithmeticOpResult> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getSubtractMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     */
    public void complexOperation(org.example.gen.ComplexArithmeticOpArguments request,
        io.grpc.stub.StreamObserver<org.example.gen.ComplexArithmeticOpResult> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getComplexOperationMethod(), getCallOptions()), request, responseObserver);
    }

    /**
     * <pre>
     * New rpc for batch operation
     * </pre>
     */
    public void performBatchOperation(org.example.gen.BatchOperationRequest request,
        io.grpc.stub.StreamObserver<org.example.gen.BatchOperationResult> responseObserver) {
      io.grpc.stub.ClientCalls.asyncUnaryCall(
          getChannel().newCall(getPerformBatchOperationMethod(), getCallOptions()), request, responseObserver);
    }
  }

  /**
   * A stub to allow clients to do synchronous rpc calls to service Calculator.
   */
  public static final class CalculatorBlockingStub
      extends io.grpc.stub.AbstractBlockingStub<CalculatorBlockingStub> {
    private CalculatorBlockingStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected CalculatorBlockingStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new CalculatorBlockingStub(channel, callOptions);
    }

    /**
     */
    public org.example.gen.ArithmeticOpResult add(org.example.gen.ArithmeticOpArguments request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getAddMethod(), getCallOptions(), request);
    }

    /**
     */
    public org.example.gen.ArithmeticOpResult subtract(org.example.gen.ArithmeticOpArguments request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getSubtractMethod(), getCallOptions(), request);
    }

    /**
     */
    public org.example.gen.ComplexArithmeticOpResult complexOperation(org.example.gen.ComplexArithmeticOpArguments request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getComplexOperationMethod(), getCallOptions(), request);
    }

    /**
     * <pre>
     * New rpc for batch operation
     * </pre>
     */
    public org.example.gen.BatchOperationResult performBatchOperation(org.example.gen.BatchOperationRequest request) {
      return io.grpc.stub.ClientCalls.blockingUnaryCall(
          getChannel(), getPerformBatchOperationMethod(), getCallOptions(), request);
    }
  }

  /**
   * A stub to allow clients to do ListenableFuture-style rpc calls to service Calculator.
   */
  public static final class CalculatorFutureStub
      extends io.grpc.stub.AbstractFutureStub<CalculatorFutureStub> {
    private CalculatorFutureStub(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      super(channel, callOptions);
    }

    @java.lang.Override
    protected CalculatorFutureStub build(
        io.grpc.Channel channel, io.grpc.CallOptions callOptions) {
      return new CalculatorFutureStub(channel, callOptions);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<org.example.gen.ArithmeticOpResult> add(
        org.example.gen.ArithmeticOpArguments request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getAddMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<org.example.gen.ArithmeticOpResult> subtract(
        org.example.gen.ArithmeticOpArguments request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getSubtractMethod(), getCallOptions()), request);
    }

    /**
     */
    public com.google.common.util.concurrent.ListenableFuture<org.example.gen.ComplexArithmeticOpResult> complexOperation(
        org.example.gen.ComplexArithmeticOpArguments request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getComplexOperationMethod(), getCallOptions()), request);
    }

    /**
     * <pre>
     * New rpc for batch operation
     * </pre>
     */
    public com.google.common.util.concurrent.ListenableFuture<org.example.gen.BatchOperationResult> performBatchOperation(
        org.example.gen.BatchOperationRequest request) {
      return io.grpc.stub.ClientCalls.futureUnaryCall(
          getChannel().newCall(getPerformBatchOperationMethod(), getCallOptions()), request);
    }
  }

  private static final int METHODID_ADD = 0;
  private static final int METHODID_SUBTRACT = 1;
  private static final int METHODID_COMPLEX_OPERATION = 2;
  private static final int METHODID_PERFORM_BATCH_OPERATION = 3;

  private static final class MethodHandlers<Req, Resp> implements
      io.grpc.stub.ServerCalls.UnaryMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ServerStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.ClientStreamingMethod<Req, Resp>,
      io.grpc.stub.ServerCalls.BidiStreamingMethod<Req, Resp> {
    private final AsyncService serviceImpl;
    private final int methodId;

    MethodHandlers(AsyncService serviceImpl, int methodId) {
      this.serviceImpl = serviceImpl;
      this.methodId = methodId;
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public void invoke(Req request, io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        case METHODID_ADD:
          serviceImpl.add((org.example.gen.ArithmeticOpArguments) request,
              (io.grpc.stub.StreamObserver<org.example.gen.ArithmeticOpResult>) responseObserver);
          break;
        case METHODID_SUBTRACT:
          serviceImpl.subtract((org.example.gen.ArithmeticOpArguments) request,
              (io.grpc.stub.StreamObserver<org.example.gen.ArithmeticOpResult>) responseObserver);
          break;
        case METHODID_COMPLEX_OPERATION:
          serviceImpl.complexOperation((org.example.gen.ComplexArithmeticOpArguments) request,
              (io.grpc.stub.StreamObserver<org.example.gen.ComplexArithmeticOpResult>) responseObserver);
          break;
        case METHODID_PERFORM_BATCH_OPERATION:
          serviceImpl.performBatchOperation((org.example.gen.BatchOperationRequest) request,
              (io.grpc.stub.StreamObserver<org.example.gen.BatchOperationResult>) responseObserver);
          break;
        default:
          throw new AssertionError();
      }
    }

    @java.lang.Override
    @java.lang.SuppressWarnings("unchecked")
    public io.grpc.stub.StreamObserver<Req> invoke(
        io.grpc.stub.StreamObserver<Resp> responseObserver) {
      switch (methodId) {
        default:
          throw new AssertionError();
      }
    }
  }

  public static final io.grpc.ServerServiceDefinition bindService(AsyncService service) {
    return io.grpc.ServerServiceDefinition.builder(getServiceDescriptor())
        .addMethod(
          getAddMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              org.example.gen.ArithmeticOpArguments,
              org.example.gen.ArithmeticOpResult>(
                service, METHODID_ADD)))
        .addMethod(
          getSubtractMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              org.example.gen.ArithmeticOpArguments,
              org.example.gen.ArithmeticOpResult>(
                service, METHODID_SUBTRACT)))
        .addMethod(
          getComplexOperationMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              org.example.gen.ComplexArithmeticOpArguments,
              org.example.gen.ComplexArithmeticOpResult>(
                service, METHODID_COMPLEX_OPERATION)))
        .addMethod(
          getPerformBatchOperationMethod(),
          io.grpc.stub.ServerCalls.asyncUnaryCall(
            new MethodHandlers<
              org.example.gen.BatchOperationRequest,
              org.example.gen.BatchOperationResult>(
                service, METHODID_PERFORM_BATCH_OPERATION)))
        .build();
  }

  private static abstract class CalculatorBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoFileDescriptorSupplier, io.grpc.protobuf.ProtoServiceDescriptorSupplier {
    CalculatorBaseDescriptorSupplier() {}

    @java.lang.Override
    public com.google.protobuf.Descriptors.FileDescriptor getFileDescriptor() {
      return org.example.gen.CalculatorProto.getDescriptor();
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.ServiceDescriptor getServiceDescriptor() {
      return getFileDescriptor().findServiceByName("Calculator");
    }
  }

  private static final class CalculatorFileDescriptorSupplier
      extends CalculatorBaseDescriptorSupplier {
    CalculatorFileDescriptorSupplier() {}
  }

  private static final class CalculatorMethodDescriptorSupplier
      extends CalculatorBaseDescriptorSupplier
      implements io.grpc.protobuf.ProtoMethodDescriptorSupplier {
    private final java.lang.String methodName;

    CalculatorMethodDescriptorSupplier(java.lang.String methodName) {
      this.methodName = methodName;
    }

    @java.lang.Override
    public com.google.protobuf.Descriptors.MethodDescriptor getMethodDescriptor() {
      return getServiceDescriptor().findMethodByName(methodName);
    }
  }

  private static volatile io.grpc.ServiceDescriptor serviceDescriptor;

  public static io.grpc.ServiceDescriptor getServiceDescriptor() {
    io.grpc.ServiceDescriptor result = serviceDescriptor;
    if (result == null) {
      synchronized (CalculatorGrpc.class) {
        result = serviceDescriptor;
        if (result == null) {
          serviceDescriptor = result = io.grpc.ServiceDescriptor.newBuilder(SERVICE_NAME)
              .setSchemaDescriptor(new CalculatorFileDescriptorSupplier())
              .addMethod(getAddMethod())
              .addMethod(getSubtractMethod())
              .addMethod(getComplexOperationMethod())
              .addMethod(getPerformBatchOperationMethod())
              .build();
        }
      }
    }
    return result;
  }
}
