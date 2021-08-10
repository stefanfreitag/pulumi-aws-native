// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package lambda

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html
type EventSourceMapping struct {
	pulumi.CustomResourceState

	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-batchsize
	BatchSize pulumi.IntPtrOutput `pulumi:"batchSize"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror
	BisectBatchOnFunctionError pulumi.BoolPtrOutput `pulumi:"bisectBatchOnFunctionError"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-destinationconfig
	DestinationConfig EventSourceMappingDestinationConfigPtrOutput `pulumi:"destinationConfig"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-enabled
	Enabled pulumi.BoolPtrOutput `pulumi:"enabled"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-eventsourcearn
	EventSourceArn pulumi.StringPtrOutput `pulumi:"eventSourceArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionname
	FunctionName pulumi.StringOutput `pulumi:"functionName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionresponsetypes
	FunctionResponseTypes pulumi.StringArrayOutput `pulumi:"functionResponseTypes"`
	Id                    pulumi.StringOutput      `pulumi:"id"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds
	MaximumBatchingWindowInSeconds pulumi.IntPtrOutput `pulumi:"maximumBatchingWindowInSeconds"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumrecordageinseconds
	MaximumRecordAgeInSeconds pulumi.IntPtrOutput `pulumi:"maximumRecordAgeInSeconds"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumretryattempts
	MaximumRetryAttempts pulumi.IntPtrOutput `pulumi:"maximumRetryAttempts"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-parallelizationfactor
	ParallelizationFactor pulumi.IntPtrOutput `pulumi:"parallelizationFactor"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-partialbatchresponse
	PartialBatchResponse pulumi.BoolPtrOutput `pulumi:"partialBatchResponse"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-queues
	Queues pulumi.StringArrayOutput `pulumi:"queues"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-selfmanagedeventsource
	SelfManagedEventSource EventSourceMappingSelfManagedEventSourcePtrOutput `pulumi:"selfManagedEventSource"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-sourceaccessconfigurations
	SourceAccessConfigurations EventSourceMappingSourceAccessConfigurationArrayOutput `pulumi:"sourceAccessConfigurations"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingposition
	StartingPosition pulumi.StringPtrOutput `pulumi:"startingPosition"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-topics
	Topics pulumi.StringArrayOutput `pulumi:"topics"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-tumblingwindowinseconds
	TumblingWindowInSeconds pulumi.IntPtrOutput `pulumi:"tumblingWindowInSeconds"`
}

// NewEventSourceMapping registers a new resource with the given unique name, arguments, and options.
func NewEventSourceMapping(ctx *pulumi.Context,
	name string, args *EventSourceMappingArgs, opts ...pulumi.ResourceOption) (*EventSourceMapping, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FunctionName == nil {
		return nil, errors.New("invalid value for required argument 'FunctionName'")
	}
	var resource EventSourceMapping
	err := ctx.RegisterResource("aws-native:Lambda:EventSourceMapping", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEventSourceMapping gets an existing EventSourceMapping resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEventSourceMapping(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EventSourceMappingState, opts ...pulumi.ResourceOption) (*EventSourceMapping, error) {
	var resource EventSourceMapping
	err := ctx.ReadResource("aws-native:Lambda:EventSourceMapping", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EventSourceMapping resources.
type eventSourceMappingState struct {
}

type EventSourceMappingState struct {
}

func (EventSourceMappingState) ElementType() reflect.Type {
	return reflect.TypeOf((*eventSourceMappingState)(nil)).Elem()
}

type eventSourceMappingArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-batchsize
	BatchSize *int `pulumi:"batchSize"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror
	BisectBatchOnFunctionError *bool `pulumi:"bisectBatchOnFunctionError"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-destinationconfig
	DestinationConfig *EventSourceMappingDestinationConfig `pulumi:"destinationConfig"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-enabled
	Enabled *bool `pulumi:"enabled"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-eventsourcearn
	EventSourceArn *string `pulumi:"eventSourceArn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionname
	FunctionName string `pulumi:"functionName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionresponsetypes
	FunctionResponseTypes []string `pulumi:"functionResponseTypes"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds
	MaximumBatchingWindowInSeconds *int `pulumi:"maximumBatchingWindowInSeconds"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumrecordageinseconds
	MaximumRecordAgeInSeconds *int `pulumi:"maximumRecordAgeInSeconds"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumretryattempts
	MaximumRetryAttempts *int `pulumi:"maximumRetryAttempts"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-parallelizationfactor
	ParallelizationFactor *int `pulumi:"parallelizationFactor"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-partialbatchresponse
	PartialBatchResponse *bool `pulumi:"partialBatchResponse"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-queues
	Queues []string `pulumi:"queues"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-selfmanagedeventsource
	SelfManagedEventSource *EventSourceMappingSelfManagedEventSource `pulumi:"selfManagedEventSource"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-sourceaccessconfigurations
	SourceAccessConfigurations []EventSourceMappingSourceAccessConfiguration `pulumi:"sourceAccessConfigurations"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingposition
	StartingPosition *string `pulumi:"startingPosition"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-topics
	Topics []string `pulumi:"topics"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-tumblingwindowinseconds
	TumblingWindowInSeconds *int `pulumi:"tumblingWindowInSeconds"`
}

// The set of arguments for constructing a EventSourceMapping resource.
type EventSourceMappingArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-batchsize
	BatchSize pulumi.IntPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-bisectbatchonfunctionerror
	BisectBatchOnFunctionError pulumi.BoolPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-destinationconfig
	DestinationConfig EventSourceMappingDestinationConfigPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-enabled
	Enabled pulumi.BoolPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-eventsourcearn
	EventSourceArn pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionname
	FunctionName pulumi.StringInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-functionresponsetypes
	FunctionResponseTypes pulumi.StringArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumbatchingwindowinseconds
	MaximumBatchingWindowInSeconds pulumi.IntPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumrecordageinseconds
	MaximumRecordAgeInSeconds pulumi.IntPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-maximumretryattempts
	MaximumRetryAttempts pulumi.IntPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-parallelizationfactor
	ParallelizationFactor pulumi.IntPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-partialbatchresponse
	PartialBatchResponse pulumi.BoolPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-queues
	Queues pulumi.StringArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-selfmanagedeventsource
	SelfManagedEventSource EventSourceMappingSelfManagedEventSourcePtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-sourceaccessconfigurations
	SourceAccessConfigurations EventSourceMappingSourceAccessConfigurationArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-startingposition
	StartingPosition pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-topics
	Topics pulumi.StringArrayInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-lambda-eventsourcemapping.html#cfn-lambda-eventsourcemapping-tumblingwindowinseconds
	TumblingWindowInSeconds pulumi.IntPtrInput
}

func (EventSourceMappingArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*eventSourceMappingArgs)(nil)).Elem()
}

type EventSourceMappingInput interface {
	pulumi.Input

	ToEventSourceMappingOutput() EventSourceMappingOutput
	ToEventSourceMappingOutputWithContext(ctx context.Context) EventSourceMappingOutput
}

func (*EventSourceMapping) ElementType() reflect.Type {
	return reflect.TypeOf((*EventSourceMapping)(nil))
}

func (i *EventSourceMapping) ToEventSourceMappingOutput() EventSourceMappingOutput {
	return i.ToEventSourceMappingOutputWithContext(context.Background())
}

func (i *EventSourceMapping) ToEventSourceMappingOutputWithContext(ctx context.Context) EventSourceMappingOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EventSourceMappingOutput)
}

type EventSourceMappingOutput struct{ *pulumi.OutputState }

func (EventSourceMappingOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EventSourceMapping)(nil))
}

func (o EventSourceMappingOutput) ToEventSourceMappingOutput() EventSourceMappingOutput {
	return o
}

func (o EventSourceMappingOutput) ToEventSourceMappingOutputWithContext(ctx context.Context) EventSourceMappingOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(EventSourceMappingOutput{})
}
