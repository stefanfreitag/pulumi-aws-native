// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package refactorspaces

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Definition of AWS::RefactorSpaces::Route Resource Type
func LookupRoute(ctx *pulumi.Context, args *LookupRouteArgs, opts ...pulumi.InvokeOption) (*LookupRouteResult, error) {
	var rv LookupRouteResult
	err := ctx.Invoke("aws-native:refactorspaces:getRoute", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupRouteArgs struct {
	ApplicationIdentifier string `pulumi:"applicationIdentifier"`
	EnvironmentIdentifier string `pulumi:"environmentIdentifier"`
	RouteIdentifier       string `pulumi:"routeIdentifier"`
}

type LookupRouteResult struct {
	Arn              *string `pulumi:"arn"`
	PathResourceToId *string `pulumi:"pathResourceToId"`
	RouteIdentifier  *string `pulumi:"routeIdentifier"`
	// Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
	Tags []RouteTag `pulumi:"tags"`
}

func LookupRouteOutput(ctx *pulumi.Context, args LookupRouteOutputArgs, opts ...pulumi.InvokeOption) LookupRouteResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupRouteResult, error) {
			args := v.(LookupRouteArgs)
			r, err := LookupRoute(ctx, &args, opts...)
			var s LookupRouteResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupRouteResultOutput)
}

type LookupRouteOutputArgs struct {
	ApplicationIdentifier pulumi.StringInput `pulumi:"applicationIdentifier"`
	EnvironmentIdentifier pulumi.StringInput `pulumi:"environmentIdentifier"`
	RouteIdentifier       pulumi.StringInput `pulumi:"routeIdentifier"`
}

func (LookupRouteOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRouteArgs)(nil)).Elem()
}

type LookupRouteResultOutput struct{ *pulumi.OutputState }

func (LookupRouteResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRouteResult)(nil)).Elem()
}

func (o LookupRouteResultOutput) ToLookupRouteResultOutput() LookupRouteResultOutput {
	return o
}

func (o LookupRouteResultOutput) ToLookupRouteResultOutputWithContext(ctx context.Context) LookupRouteResultOutput {
	return o
}

func (o LookupRouteResultOutput) Arn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRouteResult) *string { return v.Arn }).(pulumi.StringPtrOutput)
}

func (o LookupRouteResultOutput) PathResourceToId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRouteResult) *string { return v.PathResourceToId }).(pulumi.StringPtrOutput)
}

func (o LookupRouteResultOutput) RouteIdentifier() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRouteResult) *string { return v.RouteIdentifier }).(pulumi.StringPtrOutput)
}

// Metadata that you can assign to help organize the frameworks that you create. Each tag is a key-value pair.
func (o LookupRouteResultOutput) Tags() RouteTagArrayOutput {
	return o.ApplyT(func(v LookupRouteResult) []RouteTag { return v.Tags }).(RouteTagArrayOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupRouteResultOutput{})
}
