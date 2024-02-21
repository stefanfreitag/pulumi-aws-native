// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package apigatewayv2

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// The “AWS::ApiGatewayV2::Route“ resource creates a route for an API.
func LookupRoute(ctx *pulumi.Context, args *LookupRouteArgs, opts ...pulumi.InvokeOption) (*LookupRouteResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupRouteResult
	err := ctx.Invoke("aws-native:apigatewayv2:getRoute", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupRouteArgs struct {
	// The API identifier.
	ApiId   string `pulumi:"apiId"`
	RouteId string `pulumi:"routeId"`
}

type LookupRouteResult struct {
	// Specifies whether an API key is required for the route. Supported only for WebSocket APIs.
	ApiKeyRequired *bool `pulumi:"apiKeyRequired"`
	// The authorization scopes supported by this route.
	AuthorizationScopes []string `pulumi:"authorizationScopes"`
	// The authorization type for the route. For WebSocket APIs, valid values are ``NONE`` for open access, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer. For HTTP APIs, valid values are ``NONE`` for open access, ``JWT`` for using JSON Web Tokens, ``AWS_IAM`` for using AWS IAM permissions, and ``CUSTOM`` for using a Lambda authorizer.
	AuthorizationType *string `pulumi:"authorizationType"`
	// The model selection expression for the route. Supported only for WebSocket APIs.
	ModelSelectionExpression *string `pulumi:"modelSelectionExpression"`
	// The operation name for the route.
	OperationName *string `pulumi:"operationName"`
	// The request models for the route. Supported only for WebSocket APIs.
	//
	// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::Route` for more information about the expected schema for this property.
	RequestModels interface{} `pulumi:"requestModels"`
	RouteId       *string     `pulumi:"routeId"`
	// The route key for the route. For HTTP APIs, the route key can be either ``$default``, or a combination of an HTTP method and resource path, for example, ``GET /pets``.
	RouteKey *string `pulumi:"routeKey"`
	// The route response selection expression for the route. Supported only for WebSocket APIs.
	RouteResponseSelectionExpression *string `pulumi:"routeResponseSelectionExpression"`
	// The target for the route.
	Target *string `pulumi:"target"`
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
	// The API identifier.
	ApiId   pulumi.StringInput `pulumi:"apiId"`
	RouteId pulumi.StringInput `pulumi:"routeId"`
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

// Specifies whether an API key is required for the route. Supported only for WebSocket APIs.
func (o LookupRouteResultOutput) ApiKeyRequired() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupRouteResult) *bool { return v.ApiKeyRequired }).(pulumi.BoolPtrOutput)
}

// The authorization scopes supported by this route.
func (o LookupRouteResultOutput) AuthorizationScopes() pulumi.StringArrayOutput {
	return o.ApplyT(func(v LookupRouteResult) []string { return v.AuthorizationScopes }).(pulumi.StringArrayOutput)
}

// The authorization type for the route. For WebSocket APIs, valid values are “NONE“ for open access, “AWS_IAM“ for using AWS IAM permissions, and “CUSTOM“ for using a Lambda authorizer. For HTTP APIs, valid values are “NONE“ for open access, “JWT“ for using JSON Web Tokens, “AWS_IAM“ for using AWS IAM permissions, and “CUSTOM“ for using a Lambda authorizer.
func (o LookupRouteResultOutput) AuthorizationType() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRouteResult) *string { return v.AuthorizationType }).(pulumi.StringPtrOutput)
}

// The model selection expression for the route. Supported only for WebSocket APIs.
func (o LookupRouteResultOutput) ModelSelectionExpression() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRouteResult) *string { return v.ModelSelectionExpression }).(pulumi.StringPtrOutput)
}

// The operation name for the route.
func (o LookupRouteResultOutput) OperationName() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRouteResult) *string { return v.OperationName }).(pulumi.StringPtrOutput)
}

// The request models for the route. Supported only for WebSocket APIs.
//
// Search the [CloudFormation User Guide](https://docs.aws.amazon.com/cloudformation/) for `AWS::ApiGatewayV2::Route` for more information about the expected schema for this property.
func (o LookupRouteResultOutput) RequestModels() pulumi.AnyOutput {
	return o.ApplyT(func(v LookupRouteResult) interface{} { return v.RequestModels }).(pulumi.AnyOutput)
}

func (o LookupRouteResultOutput) RouteId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRouteResult) *string { return v.RouteId }).(pulumi.StringPtrOutput)
}

// The route key for the route. For HTTP APIs, the route key can be either “$default“, or a combination of an HTTP method and resource path, for example, “GET /pets“.
func (o LookupRouteResultOutput) RouteKey() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRouteResult) *string { return v.RouteKey }).(pulumi.StringPtrOutput)
}

// The route response selection expression for the route. Supported only for WebSocket APIs.
func (o LookupRouteResultOutput) RouteResponseSelectionExpression() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRouteResult) *string { return v.RouteResponseSelectionExpression }).(pulumi.StringPtrOutput)
}

// The target for the route.
func (o LookupRouteResultOutput) Target() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRouteResult) *string { return v.Target }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupRouteResultOutput{})
}
