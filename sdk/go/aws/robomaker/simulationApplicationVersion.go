// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package robomaker

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// An example resource schema demonstrating some basic constructs and validation rules.
type SimulationApplicationVersion struct {
	pulumi.CustomResourceState

	Application        pulumi.StringOutput `pulumi:"application"`
	ApplicationVersion pulumi.StringOutput `pulumi:"applicationVersion"`
	Arn                pulumi.StringOutput `pulumi:"arn"`
	// The revision ID of robot application.
	CurrentRevisionId pulumi.StringPtrOutput `pulumi:"currentRevisionId"`
}

// NewSimulationApplicationVersion registers a new resource with the given unique name, arguments, and options.
func NewSimulationApplicationVersion(ctx *pulumi.Context,
	name string, args *SimulationApplicationVersionArgs, opts ...pulumi.ResourceOption) (*SimulationApplicationVersion, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.Application == nil {
		return nil, errors.New("invalid value for required argument 'Application'")
	}
	var resource SimulationApplicationVersion
	err := ctx.RegisterResource("aws-native:robomaker:SimulationApplicationVersion", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetSimulationApplicationVersion gets an existing SimulationApplicationVersion resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetSimulationApplicationVersion(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *SimulationApplicationVersionState, opts ...pulumi.ResourceOption) (*SimulationApplicationVersion, error) {
	var resource SimulationApplicationVersion
	err := ctx.ReadResource("aws-native:robomaker:SimulationApplicationVersion", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering SimulationApplicationVersion resources.
type simulationApplicationVersionState struct {
}

type SimulationApplicationVersionState struct {
}

func (SimulationApplicationVersionState) ElementType() reflect.Type {
	return reflect.TypeOf((*simulationApplicationVersionState)(nil)).Elem()
}

type simulationApplicationVersionArgs struct {
	Application string `pulumi:"application"`
	// The revision ID of robot application.
	CurrentRevisionId *string `pulumi:"currentRevisionId"`
}

// The set of arguments for constructing a SimulationApplicationVersion resource.
type SimulationApplicationVersionArgs struct {
	Application pulumi.StringInput
	// The revision ID of robot application.
	CurrentRevisionId pulumi.StringPtrInput
}

func (SimulationApplicationVersionArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*simulationApplicationVersionArgs)(nil)).Elem()
}

type SimulationApplicationVersionInput interface {
	pulumi.Input

	ToSimulationApplicationVersionOutput() SimulationApplicationVersionOutput
	ToSimulationApplicationVersionOutputWithContext(ctx context.Context) SimulationApplicationVersionOutput
}

func (*SimulationApplicationVersion) ElementType() reflect.Type {
	return reflect.TypeOf((*SimulationApplicationVersion)(nil))
}

func (i *SimulationApplicationVersion) ToSimulationApplicationVersionOutput() SimulationApplicationVersionOutput {
	return i.ToSimulationApplicationVersionOutputWithContext(context.Background())
}

func (i *SimulationApplicationVersion) ToSimulationApplicationVersionOutputWithContext(ctx context.Context) SimulationApplicationVersionOutput {
	return pulumi.ToOutputWithContext(ctx, i).(SimulationApplicationVersionOutput)
}

type SimulationApplicationVersionOutput struct{ *pulumi.OutputState }

func (SimulationApplicationVersionOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*SimulationApplicationVersion)(nil))
}

func (o SimulationApplicationVersionOutput) ToSimulationApplicationVersionOutput() SimulationApplicationVersionOutput {
	return o
}

func (o SimulationApplicationVersionOutput) ToSimulationApplicationVersionOutputWithContext(ctx context.Context) SimulationApplicationVersionOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(SimulationApplicationVersionOutput{})
}
