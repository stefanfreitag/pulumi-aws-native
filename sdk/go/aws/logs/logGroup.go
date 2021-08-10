// *** WARNING: this file was generated by pulumigen. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package logs

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html
type LogGroup struct {
	pulumi.CustomResourceState

	Arn pulumi.StringOutput `pulumi:"arn"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-kmskeyid
	KmsKeyId pulumi.StringPtrOutput `pulumi:"kmsKeyId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-loggroupname
	LogGroupName pulumi.StringPtrOutput `pulumi:"logGroupName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-retentionindays
	RetentionInDays pulumi.IntPtrOutput `pulumi:"retentionInDays"`
}

// NewLogGroup registers a new resource with the given unique name, arguments, and options.
func NewLogGroup(ctx *pulumi.Context,
	name string, args *LogGroupArgs, opts ...pulumi.ResourceOption) (*LogGroup, error) {
	if args == nil {
		args = &LogGroupArgs{}
	}

	var resource LogGroup
	err := ctx.RegisterResource("aws-native:Logs:LogGroup", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetLogGroup gets an existing LogGroup resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetLogGroup(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *LogGroupState, opts ...pulumi.ResourceOption) (*LogGroup, error) {
	var resource LogGroup
	err := ctx.ReadResource("aws-native:Logs:LogGroup", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering LogGroup resources.
type logGroupState struct {
}

type LogGroupState struct {
}

func (LogGroupState) ElementType() reflect.Type {
	return reflect.TypeOf((*logGroupState)(nil)).Elem()
}

type logGroupArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-kmskeyid
	KmsKeyId *string `pulumi:"kmsKeyId"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-loggroupname
	LogGroupName *string `pulumi:"logGroupName"`
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-retentionindays
	RetentionInDays *int `pulumi:"retentionInDays"`
}

// The set of arguments for constructing a LogGroup resource.
type LogGroupArgs struct {
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-kmskeyid
	KmsKeyId pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-loggroupname
	LogGroupName pulumi.StringPtrInput
	// http://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-logs-loggroup.html#cfn-logs-loggroup-retentionindays
	RetentionInDays pulumi.IntPtrInput
}

func (LogGroupArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*logGroupArgs)(nil)).Elem()
}

type LogGroupInput interface {
	pulumi.Input

	ToLogGroupOutput() LogGroupOutput
	ToLogGroupOutputWithContext(ctx context.Context) LogGroupOutput
}

func (*LogGroup) ElementType() reflect.Type {
	return reflect.TypeOf((*LogGroup)(nil))
}

func (i *LogGroup) ToLogGroupOutput() LogGroupOutput {
	return i.ToLogGroupOutputWithContext(context.Background())
}

func (i *LogGroup) ToLogGroupOutputWithContext(ctx context.Context) LogGroupOutput {
	return pulumi.ToOutputWithContext(ctx, i).(LogGroupOutput)
}

type LogGroupOutput struct{ *pulumi.OutputState }

func (LogGroupOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LogGroup)(nil))
}

func (o LogGroupOutput) ToLogGroupOutput() LogGroupOutput {
	return o
}

func (o LogGroupOutput) ToLogGroupOutputWithContext(ctx context.Context) LogGroupOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(LogGroupOutput{})
}
