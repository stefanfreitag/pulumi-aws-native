// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package ses

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Resource Type definition for AWS::SES::ConfigurationSetEventDestination
type ConfigurationSetEventDestination struct {
	pulumi.CustomResourceState

	// The name of the configuration set that contains the event destination.
	ConfigurationSetName pulumi.StringOutput `pulumi:"configurationSetName"`
	// The event destination object.
	EventDestination ConfigurationSetEventDestinationEventDestinationOutput `pulumi:"eventDestination"`
}

// NewConfigurationSetEventDestination registers a new resource with the given unique name, arguments, and options.
func NewConfigurationSetEventDestination(ctx *pulumi.Context,
	name string, args *ConfigurationSetEventDestinationArgs, opts ...pulumi.ResourceOption) (*ConfigurationSetEventDestination, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ConfigurationSetName == nil {
		return nil, errors.New("invalid value for required argument 'ConfigurationSetName'")
	}
	if args.EventDestination == nil {
		return nil, errors.New("invalid value for required argument 'EventDestination'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"configurationSetName",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource ConfigurationSetEventDestination
	err := ctx.RegisterResource("aws-native:ses:ConfigurationSetEventDestination", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetConfigurationSetEventDestination gets an existing ConfigurationSetEventDestination resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetConfigurationSetEventDestination(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ConfigurationSetEventDestinationState, opts ...pulumi.ResourceOption) (*ConfigurationSetEventDestination, error) {
	var resource ConfigurationSetEventDestination
	err := ctx.ReadResource("aws-native:ses:ConfigurationSetEventDestination", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering ConfigurationSetEventDestination resources.
type configurationSetEventDestinationState struct {
}

type ConfigurationSetEventDestinationState struct {
}

func (ConfigurationSetEventDestinationState) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationSetEventDestinationState)(nil)).Elem()
}

type configurationSetEventDestinationArgs struct {
	// The name of the configuration set that contains the event destination.
	ConfigurationSetName string `pulumi:"configurationSetName"`
	// The event destination object.
	EventDestination ConfigurationSetEventDestinationEventDestination `pulumi:"eventDestination"`
}

// The set of arguments for constructing a ConfigurationSetEventDestination resource.
type ConfigurationSetEventDestinationArgs struct {
	// The name of the configuration set that contains the event destination.
	ConfigurationSetName pulumi.StringInput
	// The event destination object.
	EventDestination ConfigurationSetEventDestinationEventDestinationInput
}

func (ConfigurationSetEventDestinationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*configurationSetEventDestinationArgs)(nil)).Elem()
}

type ConfigurationSetEventDestinationInput interface {
	pulumi.Input

	ToConfigurationSetEventDestinationOutput() ConfigurationSetEventDestinationOutput
	ToConfigurationSetEventDestinationOutputWithContext(ctx context.Context) ConfigurationSetEventDestinationOutput
}

func (*ConfigurationSetEventDestination) ElementType() reflect.Type {
	return reflect.TypeOf((**ConfigurationSetEventDestination)(nil)).Elem()
}

func (i *ConfigurationSetEventDestination) ToConfigurationSetEventDestinationOutput() ConfigurationSetEventDestinationOutput {
	return i.ToConfigurationSetEventDestinationOutputWithContext(context.Background())
}

func (i *ConfigurationSetEventDestination) ToConfigurationSetEventDestinationOutputWithContext(ctx context.Context) ConfigurationSetEventDestinationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ConfigurationSetEventDestinationOutput)
}

func (i *ConfigurationSetEventDestination) ToOutput(ctx context.Context) pulumix.Output[*ConfigurationSetEventDestination] {
	return pulumix.Output[*ConfigurationSetEventDestination]{
		OutputState: i.ToConfigurationSetEventDestinationOutputWithContext(ctx).OutputState,
	}
}

type ConfigurationSetEventDestinationOutput struct{ *pulumi.OutputState }

func (ConfigurationSetEventDestinationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**ConfigurationSetEventDestination)(nil)).Elem()
}

func (o ConfigurationSetEventDestinationOutput) ToConfigurationSetEventDestinationOutput() ConfigurationSetEventDestinationOutput {
	return o
}

func (o ConfigurationSetEventDestinationOutput) ToConfigurationSetEventDestinationOutputWithContext(ctx context.Context) ConfigurationSetEventDestinationOutput {
	return o
}

func (o ConfigurationSetEventDestinationOutput) ToOutput(ctx context.Context) pulumix.Output[*ConfigurationSetEventDestination] {
	return pulumix.Output[*ConfigurationSetEventDestination]{
		OutputState: o.OutputState,
	}
}

// The name of the configuration set that contains the event destination.
func (o ConfigurationSetEventDestinationOutput) ConfigurationSetName() pulumi.StringOutput {
	return o.ApplyT(func(v *ConfigurationSetEventDestination) pulumi.StringOutput { return v.ConfigurationSetName }).(pulumi.StringOutput)
}

// The event destination object.
func (o ConfigurationSetEventDestinationOutput) EventDestination() ConfigurationSetEventDestinationEventDestinationOutput {
	return o.ApplyT(func(v *ConfigurationSetEventDestination) ConfigurationSetEventDestinationEventDestinationOutput {
		return v.EventDestination
	}).(ConfigurationSetEventDestinationEventDestinationOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*ConfigurationSetEventDestinationInput)(nil)).Elem(), &ConfigurationSetEventDestination{})
	pulumi.RegisterOutputType(ConfigurationSetEventDestinationOutput{})
}
