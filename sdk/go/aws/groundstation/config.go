// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package groundstation

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// AWS Ground Station config resource type for CloudFormation.
type Config struct {
	pulumi.CustomResourceState

	Arn        pulumi.StringOutput    `pulumi:"arn"`
	ConfigData ConfigConfigDataOutput `pulumi:"configData"`
	Name       pulumi.StringOutput    `pulumi:"name"`
	Tags       ConfigTagArrayOutput   `pulumi:"tags"`
	Type       pulumi.StringOutput    `pulumi:"type"`
}

// NewConfig registers a new resource with the given unique name, arguments, and options.
func NewConfig(ctx *pulumi.Context,
	name string, args *ConfigArgs, opts ...pulumi.ResourceOption) (*Config, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConfigData == nil {
		return nil, errors.New("invalid value for required argument 'ConfigData'")
	}
	if args.Name == nil {
		return nil, errors.New("invalid value for required argument 'Name'")
	}
	var resource Config
	err := ctx.RegisterResource("aws-native:groundstation:Config", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConfig gets an existing Config resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConfig(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConfigState, opts ...pulumi.ResourceOption) (*Config, error) {
	var resource Config
	err := ctx.ReadResource("aws-native:groundstation:Config", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Config resources.
type configState struct {
}

type ConfigState struct {
}

func (ConfigState) ElementType() reflect.Type {
	return reflect.TypeOf((*configState)(nil)).Elem()
}

type configArgs struct {
	ConfigData ConfigConfigData `pulumi:"configData"`
	Name       string           `pulumi:"name"`
	Tags       []ConfigTag      `pulumi:"tags"`
}

// The set of arguments for constructing a Config resource.
type ConfigArgs struct {
	ConfigData ConfigConfigDataInput
	Name       pulumi.StringInput
	Tags       ConfigTagArrayInput
}

func (ConfigArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*configArgs)(nil)).Elem()
}

type ConfigInput interface {
	pulumi.Input

	ToConfigOutput() ConfigOutput
	ToConfigOutputWithContext(ctx context.Context) ConfigOutput
}

func (*Config) ElementType() reflect.Type {
	return reflect.TypeOf((*Config)(nil))
}

func (i *Config) ToConfigOutput() ConfigOutput {
	return i.ToConfigOutputWithContext(context.Background())
}

func (i *Config) ToConfigOutputWithContext(ctx context.Context) ConfigOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigOutput)
}

type ConfigOutput struct{ *pulumi.OutputState }

func (ConfigOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Config)(nil))
}

func (o ConfigOutput) ToConfigOutput() ConfigOutput {
	return o
}

func (o ConfigOutput) ToConfigOutputWithContext(ctx context.Context) ConfigOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ConfigOutput{})
}
