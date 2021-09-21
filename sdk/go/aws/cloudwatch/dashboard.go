// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package cloudwatch

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CloudWatch::Dashboard
//
// Deprecated: Dashboard is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Dashboard struct {
	pulumi.CustomResourceState

	DashboardBody pulumi.StringOutput    `pulumi:"dashboardBody"`
	DashboardName pulumi.StringPtrOutput `pulumi:"dashboardName"`
}

// NewDashboard registers a new resource with the given unique name, arguments, and options.
func NewDashboard(ctx *pulumi.Context,
	name string, args *DashboardArgs, opts ...pulumi.ResourceOption) (*Dashboard, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DashboardBody == nil {
		return nil, errors.New("invalid value for required argument 'DashboardBody'")
	}
	var resource Dashboard
	err := ctx.RegisterResource("aws-native:cloudwatch:Dashboard", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetDashboard gets an existing Dashboard resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetDashboard(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *DashboardState, opts ...pulumi.ResourceOption) (*Dashboard, error) {
	var resource Dashboard
	err := ctx.ReadResource("aws-native:cloudwatch:Dashboard", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Dashboard resources.
type dashboardState struct {
}

type DashboardState struct {
}

func (DashboardState) ElementType() reflect.Type {
	return reflect.TypeOf((*dashboardState)(nil)).Elem()
}

type dashboardArgs struct {
	DashboardBody string  `pulumi:"dashboardBody"`
	DashboardName *string `pulumi:"dashboardName"`
}

// The set of arguments for constructing a Dashboard resource.
type DashboardArgs struct {
	DashboardBody pulumi.StringInput
	DashboardName pulumi.StringPtrInput
}

func (DashboardArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*dashboardArgs)(nil)).Elem()
}

type DashboardInput interface {
	pulumi.Input

	ToDashboardOutput() DashboardOutput
	ToDashboardOutputWithContext(ctx context.Context) DashboardOutput
}

func (*Dashboard) ElementType() reflect.Type {
	return reflect.TypeOf((*Dashboard)(nil))
}

func (i *Dashboard) ToDashboardOutput() DashboardOutput {
	return i.ToDashboardOutputWithContext(context.Background())
}

func (i *Dashboard) ToDashboardOutputWithContext(ctx context.Context) DashboardOutput {
	return pulumi.ToOutputWithContext(ctx, i).(DashboardOutput)
}

type DashboardOutput struct{ *pulumi.OutputState }

func (DashboardOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*Dashboard)(nil))
}

func (o DashboardOutput) ToDashboardOutput() DashboardOutput {
	return o
}

func (o DashboardOutput) ToDashboardOutputWithContext(ctx context.Context) DashboardOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(DashboardOutput{})
}
