// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package globalaccelerator

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::GlobalAccelerator::Listener
type Listener struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the accelerator.
	AcceleratorArn pulumi.StringOutput `pulumi:"acceleratorArn"`
	// Client affinity lets you direct all requests from a user to the same endpoint.
	ClientAffinity ListenerClientAffinityPtrOutput `pulumi:"clientAffinity"`
	// The Amazon Resource Name (ARN) of the listener.
	ListenerArn pulumi.StringOutput          `pulumi:"listenerArn"`
	PortRanges  ListenerPortRangeArrayOutput `pulumi:"portRanges"`
	// The protocol for the listener.
	Protocol ListenerProtocolOutput `pulumi:"protocol"`
}

// NewListener registers a new resource with the given unique name, arguments, and options.
func NewListener(ctx *pulumi.Context,
	name string, args *ListenerArgs, opts ...pulumi.ResourceOption) (*Listener, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.AcceleratorArn == nil {
		return nil, errors.New("invalid value for required argument 'AcceleratorArn'")
	}
	if args.PortRanges == nil {
		return nil, errors.New("invalid value for required argument 'PortRanges'")
	}
	if args.Protocol == nil {
		return nil, errors.New("invalid value for required argument 'Protocol'")
	}
	var resource Listener
	err := ctx.RegisterResource("aws-native:globalaccelerator:Listener", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetListener gets an existing Listener resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetListener(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *ListenerState, opts ...pulumi.ResourceOption) (*Listener, error) {
	var resource Listener
	err := ctx.ReadResource("aws-native:globalaccelerator:Listener", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Listener resources.
type listenerState struct {
}

type ListenerState struct {
}

func (ListenerState) ElementType() reflect.Type {
	return reflect.TypeOf((*listenerState)(nil)).Elem()
}

type listenerArgs struct {
	// The Amazon Resource Name (ARN) of the accelerator.
	AcceleratorArn string `pulumi:"acceleratorArn"`
	// Client affinity lets you direct all requests from a user to the same endpoint.
	ClientAffinity *ListenerClientAffinity `pulumi:"clientAffinity"`
	PortRanges     []ListenerPortRange     `pulumi:"portRanges"`
	// The protocol for the listener.
	Protocol ListenerProtocol `pulumi:"protocol"`
}

// The set of arguments for constructing a Listener resource.
type ListenerArgs struct {
	// The Amazon Resource Name (ARN) of the accelerator.
	AcceleratorArn pulumi.StringInput
	// Client affinity lets you direct all requests from a user to the same endpoint.
	ClientAffinity ListenerClientAffinityPtrInput
	PortRanges     ListenerPortRangeArrayInput
	// The protocol for the listener.
	Protocol ListenerProtocolInput
}

func (ListenerArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*listenerArgs)(nil)).Elem()
}

type ListenerInput interface {
	pulumi.Input

	ToListenerOutput() ListenerOutput
	ToListenerOutputWithContext(ctx context.Context) ListenerOutput
}

func (*Listener) ElementType() reflect.Type {
	return reflect.TypeOf((*Listener)(nil))
}

func (i *Listener) ToListenerOutput() ListenerOutput {
	return i.ToListenerOutputWithContext(context.Background())
}

func (i *Listener) ToListenerOutputWithContext(ctx context.Context) ListenerOutput {
	return pulumi.ToOutputWithContext(ctx, i).(ListenerOutput)
}

type ListenerOutput struct{ *pulumi.OutputState }

func (ListenerOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Listener)(nil))
}

func (o ListenerOutput) ToListenerOutput() ListenerOutput {
	return o
}

func (o ListenerOutput) ToListenerOutputWithContext(ctx context.Context) ListenerOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(ListenerOutput{})
}
