// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudwatch

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for Metric Stream
type MetricStream struct {
	pulumi.CustomResourceState

	// Amazon Resource Name of the metric stream.
	Arn pulumi.StringOutput `pulumi:"arn"`
	// The date of creation of the metric stream.
	CreationDate pulumi.StringOutput `pulumi:"creationDate"`
	// Define which metrics will be not streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
	ExcludeFilters MetricStreamMetricStreamFilterArrayOutput `pulumi:"excludeFilters"`
	// The ARN of the Kinesis Firehose where to stream the data.
	FirehoseArn pulumi.StringOutput `pulumi:"firehoseArn"`
	// Define which metrics will be streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
	IncludeFilters MetricStreamMetricStreamFilterArrayOutput `pulumi:"includeFilters"`
	// The date of the last update of the metric stream.
	LastUpdateDate pulumi.StringOutput `pulumi:"lastUpdateDate"`
	// Name of the metric stream.
	Name pulumi.StringPtrOutput `pulumi:"name"`
	// The output format of the data streamed to the Kinesis Firehose.
	OutputFormat pulumi.StringOutput `pulumi:"outputFormat"`
	// The ARN of the role that provides access to the Kinesis Firehose.
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
	// Displays the state of the Metric Stream.
	State pulumi.StringOutput `pulumi:"state"`
	// A set of tags to assign to the delivery stream.
	Tags MetricStreamTagArrayOutput `pulumi:"tags"`
}

// NewMetricStream registers a new resource with the given unique name, arguments, and options.
func NewMetricStream(ctx *pulumi.Context,
	name string, args *MetricStreamArgs, opts ...pulumi.ResourceOption) (*MetricStream, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.FirehoseArn == nil {
		return nil, errors.New("invalid value for required argument 'FirehoseArn'")
	}
	if args.OutputFormat == nil {
		return nil, errors.New("invalid value for required argument 'OutputFormat'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	var resource MetricStream
	err := ctx.RegisterResource("aws-native:cloudwatch:MetricStream", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetMetricStream gets an existing MetricStream resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetMetricStream(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *MetricStreamState, opts ...pulumi.ResourceOption) (*MetricStream, error) {
	var resource MetricStream
	err := ctx.ReadResource("aws-native:cloudwatch:MetricStream", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering MetricStream resources.
type metricStreamState struct {
}

type MetricStreamState struct {
}

func (MetricStreamState) ElementType() reflect.Type {
	return reflect.TypeOf((*metricStreamState)(nil)).Elem()
}

type metricStreamArgs struct {
	// Define which metrics will be not streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
	ExcludeFilters []MetricStreamMetricStreamFilter `pulumi:"excludeFilters"`
	// The ARN of the Kinesis Firehose where to stream the data.
	FirehoseArn string `pulumi:"firehoseArn"`
	// Define which metrics will be streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
	IncludeFilters []MetricStreamMetricStreamFilter `pulumi:"includeFilters"`
	// Name of the metric stream.
	Name *string `pulumi:"name"`
	// The output format of the data streamed to the Kinesis Firehose.
	OutputFormat string `pulumi:"outputFormat"`
	// The ARN of the role that provides access to the Kinesis Firehose.
	RoleArn string `pulumi:"roleArn"`
	// A set of tags to assign to the delivery stream.
	Tags []MetricStreamTag `pulumi:"tags"`
}

// The set of arguments for constructing a MetricStream resource.
type MetricStreamArgs struct {
	// Define which metrics will be not streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
	ExcludeFilters MetricStreamMetricStreamFilterArrayInput
	// The ARN of the Kinesis Firehose where to stream the data.
	FirehoseArn pulumi.StringInput
	// Define which metrics will be streamed. Metrics matched by multiple instances of MetricStreamFilter are joined with an OR operation by default. If both IncludeFilters and ExcludeFilters are omitted, all metrics in the account will be streamed. IncludeFilters and ExcludeFilters are mutually exclusive. Default to null.
	IncludeFilters MetricStreamMetricStreamFilterArrayInput
	// Name of the metric stream.
	Name pulumi.StringPtrInput
	// The output format of the data streamed to the Kinesis Firehose.
	OutputFormat pulumi.StringInput
	// The ARN of the role that provides access to the Kinesis Firehose.
	RoleArn pulumi.StringInput
	// A set of tags to assign to the delivery stream.
	Tags MetricStreamTagArrayInput
}

func (MetricStreamArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*metricStreamArgs)(nil)).Elem()
}

type MetricStreamInput interface {
	pulumi.Input

	ToMetricStreamOutput() MetricStreamOutput
	ToMetricStreamOutputWithContext(ctx context.Context) MetricStreamOutput
}

func (*MetricStream) ElementType() reflect.Type {
	return reflect.TypeOf((*MetricStream)(nil))
}

func (i *MetricStream) ToMetricStreamOutput() MetricStreamOutput {
	return i.ToMetricStreamOutputWithContext(context.Background())
}

func (i *MetricStream) ToMetricStreamOutputWithContext(ctx context.Context) MetricStreamOutput {
	return pulumi.ToOutputWithContext(ctx, i).(MetricStreamOutput)
}

type MetricStreamOutput struct{ *pulumi.OutputState }

func (MetricStreamOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*MetricStream)(nil))
}

func (o MetricStreamOutput) ToMetricStreamOutput() MetricStreamOutput {
	return o
}

func (o MetricStreamOutput) ToMetricStreamOutputWithContext(ctx context.Context) MetricStreamOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(MetricStreamOutput{})
}
