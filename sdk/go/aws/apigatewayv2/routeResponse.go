// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package apigatewayv2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::ApiGatewayV2::RouteResponse
//
// Deprecated: RouteResponse is not yet supported by AWS Cloud Control API, so its creation will currently fail. Please use the classic AWS provider, if possible.
type RouteResponse struct {
	pulumi.CustomResourceState

	ApiId                    pulumi.StringOutput    `pulumi:"apiId"`
	ModelSelectionExpression pulumi.StringPtrOutput `pulumi:"modelSelectionExpression"`
	ResponseModels           pulumi.AnyOutput       `pulumi:"responseModels"`
	ResponseParameters       pulumi.AnyOutput       `pulumi:"responseParameters"`
	RouteId                  pulumi.StringOutput    `pulumi:"routeId"`
	RouteResponseKey         pulumi.StringOutput    `pulumi:"routeResponseKey"`
}

// NewRouteResponse registers a new resource with the given unique name, arguments, and options.
func NewRouteResponse(ctx *pulumi.Context,
	name string, args *RouteResponseArgs, opts ...pulumi.ResourceOption) (*RouteResponse, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.ApiId == nil {
		return nil, errors.New("invalid value for required argument 'ApiId'")
	}
	if args.RouteId == nil {
		return nil, errors.New("invalid value for required argument 'RouteId'")
	}
	if args.RouteResponseKey == nil {
		return nil, errors.New("invalid value for required argument 'RouteResponseKey'")
	}
	var resource RouteResponse
	err := ctx.RegisterResource("aws-native:apigatewayv2:RouteResponse", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetRouteResponse gets an existing RouteResponse resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetRouteResponse(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *RouteResponseState, opts ...pulumi.ResourceOption) (*RouteResponse, error) {
	var resource RouteResponse
	err := ctx.ReadResource("aws-native:apigatewayv2:RouteResponse", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering RouteResponse resources.
type routeResponseState struct {
}

type RouteResponseState struct {
}

func (RouteResponseState) ElementType() reflect.Type {
	return reflect.TypeOf((*routeResponseState)(nil)).Elem()
}

type routeResponseArgs struct {
	ApiId                    string      `pulumi:"apiId"`
	ModelSelectionExpression *string     `pulumi:"modelSelectionExpression"`
	ResponseModels           interface{} `pulumi:"responseModels"`
	ResponseParameters       interface{} `pulumi:"responseParameters"`
	RouteId                  string      `pulumi:"routeId"`
	RouteResponseKey         string      `pulumi:"routeResponseKey"`
}

// The set of arguments for constructing a RouteResponse resource.
type RouteResponseArgs struct {
	ApiId                    pulumi.StringInput
	ModelSelectionExpression pulumi.StringPtrInput
	ResponseModels           pulumi.Input
	ResponseParameters       pulumi.Input
	RouteId                  pulumi.StringInput
	RouteResponseKey         pulumi.StringInput
}

func (RouteResponseArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*routeResponseArgs)(nil)).Elem()
}

type RouteResponseInput interface {
	pulumi.Input

	ToRouteResponseOutput() RouteResponseOutput
	ToRouteResponseOutputWithContext(ctx context.Context) RouteResponseOutput
}

func (*RouteResponse) ElementType() reflect.Type {
	return reflect.TypeOf((*RouteResponse)(nil))
}

func (i *RouteResponse) ToRouteResponseOutput() RouteResponseOutput {
	return i.ToRouteResponseOutputWithContext(context.Background())
}

func (i *RouteResponse) ToRouteResponseOutputWithContext(ctx context.Context) RouteResponseOutput {
	return pulumi.ToOutputWithContext(ctx, i).(RouteResponseOutput)
}

type RouteResponseOutput struct{ *pulumi.OutputState }

func (RouteResponseOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*RouteResponse)(nil))
}

func (o RouteResponseOutput) ToRouteResponseOutput() RouteResponseOutput {
	return o
}

func (o RouteResponseOutput) ToRouteResponseOutputWithContext(ctx context.Context) RouteResponseOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(RouteResponseOutput{})
}
