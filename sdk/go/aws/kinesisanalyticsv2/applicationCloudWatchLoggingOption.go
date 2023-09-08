// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package kinesisanalyticsv2

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::KinesisAnalyticsV2::ApplicationCloudWatchLoggingOption
//
// Deprecated: ApplicationCloudWatchLoggingOption is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type ApplicationCloudWatchLoggingOption struct {
	pulumi.CustomResourceState

	ApplicationName         pulumi.StringOutput                                             `pulumi:"applicationName"`
	CloudWatchLoggingOption ApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionOutput `pulumi:"cloudWatchLoggingOption"`
}

// NewApplicationCloudWatchLoggingOption registers a new resource with the given unique name, arguments, and options.
func NewApplicationCloudWatchLoggingOption(ctx *pulumi.Context,
	name string, args *ApplicationCloudWatchLoggingOptionArgs, opts ...pulumi.ResourceOption) (*ApplicationCloudWatchLoggingOption, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApplicationName == nil {
		return nil, errors.New("invalid value for required argument 'ApplicationName'")
	}
	if args.CloudWatchLoggingOption == nil {
		return nil, errors.New("invalid value for required argument 'CloudWatchLoggingOption'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"applicationName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ApplicationCloudWatchLoggingOption
	err := ctx.RegisterResource("aws-native:kinesisanalyticsv2:ApplicationCloudWatchLoggingOption", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetApplicationCloudWatchLoggingOption gets an existing ApplicationCloudWatchLoggingOption resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetApplicationCloudWatchLoggingOption(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ApplicationCloudWatchLoggingOptionState, opts ...pulumi.ResourceOption) (*ApplicationCloudWatchLoggingOption, error) {
	var resource ApplicationCloudWatchLoggingOption
	err := ctx.ReadResource("aws-native:kinesisanalyticsv2:ApplicationCloudWatchLoggingOption", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ApplicationCloudWatchLoggingOption resources.
type applicationCloudWatchLoggingOptionState struct {
}

type ApplicationCloudWatchLoggingOptionState struct {
}

func (ApplicationCloudWatchLoggingOptionState) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationCloudWatchLoggingOptionState)(nil)).Elem()
}

type applicationCloudWatchLoggingOptionArgs struct {
	ApplicationName         string                                                    `pulumi:"applicationName"`
	CloudWatchLoggingOption ApplicationCloudWatchLoggingOptionCloudWatchLoggingOption `pulumi:"cloudWatchLoggingOption"`
}

// The set of arguments for constructing a ApplicationCloudWatchLoggingOption resource.
type ApplicationCloudWatchLoggingOptionArgs struct {
	ApplicationName         pulumi.StringInput
	CloudWatchLoggingOption ApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionInput
}

func (ApplicationCloudWatchLoggingOptionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*applicationCloudWatchLoggingOptionArgs)(nil)).Elem()
}

type ApplicationCloudWatchLoggingOptionInput interface {
	pulumi.Input

	ToApplicationCloudWatchLoggingOptionOutput() ApplicationCloudWatchLoggingOptionOutput
	ToApplicationCloudWatchLoggingOptionOutputWithContext(ctx context.Context) ApplicationCloudWatchLoggingOptionOutput
}

func (*ApplicationCloudWatchLoggingOption) ElementType() reflect.Type {
	return reflect.TypeOf((**ApplicationCloudWatchLoggingOption)(nil)).Elem()
}

func (i *ApplicationCloudWatchLoggingOption) ToApplicationCloudWatchLoggingOptionOutput() ApplicationCloudWatchLoggingOptionOutput {
	return i.ToApplicationCloudWatchLoggingOptionOutputWithContext(context.Background())
}

func (i *ApplicationCloudWatchLoggingOption) ToApplicationCloudWatchLoggingOptionOutputWithContext(ctx context.Context) ApplicationCloudWatchLoggingOptionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ApplicationCloudWatchLoggingOptionOutput)
}

func (i *ApplicationCloudWatchLoggingOption) ToOutput(ctx context.Context) pulumix.Output[*ApplicationCloudWatchLoggingOption] {
	return pulumix.Output[*ApplicationCloudWatchLoggingOption]{
		OutputState: i.ToApplicationCloudWatchLoggingOptionOutputWithContext(ctx).OutputState,
	}
}

type ApplicationCloudWatchLoggingOptionOutput struct{ *pulumi.OutputState }

func (ApplicationCloudWatchLoggingOptionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ApplicationCloudWatchLoggingOption)(nil)).Elem()
}

func (o ApplicationCloudWatchLoggingOptionOutput) ToApplicationCloudWatchLoggingOptionOutput() ApplicationCloudWatchLoggingOptionOutput {
	return o
}

func (o ApplicationCloudWatchLoggingOptionOutput) ToApplicationCloudWatchLoggingOptionOutputWithContext(ctx context.Context) ApplicationCloudWatchLoggingOptionOutput {
	return o
}

func (o ApplicationCloudWatchLoggingOptionOutput) ToOutput(ctx context.Context) pulumix.Output[*ApplicationCloudWatchLoggingOption] {
	return pulumix.Output[*ApplicationCloudWatchLoggingOption]{
		OutputState: o.OutputState,
	}
}

func (o ApplicationCloudWatchLoggingOptionOutput) ApplicationName() pulumi.StringOutput {
	return o.ApplyT(func(v *ApplicationCloudWatchLoggingOption) pulumi.StringOutput { return v.ApplicationName }).(pulumi.StringOutput)
}

func (o ApplicationCloudWatchLoggingOptionOutput) CloudWatchLoggingOption() ApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionOutput {
	return o.ApplyT(func(v *ApplicationCloudWatchLoggingOption) ApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionOutput {
		return v.CloudWatchLoggingOption
	}).(ApplicationCloudWatchLoggingOptionCloudWatchLoggingOptionOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ApplicationCloudWatchLoggingOptionInput)(nil)).Elem(), &ApplicationCloudWatchLoggingOption{})
	pulumi.RegisterOutputType(ApplicationCloudWatchLoggingOptionOutput{})
}
