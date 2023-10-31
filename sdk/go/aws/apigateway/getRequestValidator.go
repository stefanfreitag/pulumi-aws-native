// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package apigateway

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// The “AWS::ApiGateway::RequestValidator“ resource sets up basic validation rules for incoming requests to your API. For more information, see [Enable Basic Request Validation for an API in API Gateway](https://docs.aws.amazon.com/apigateway/latest/developerguide/api-gateway-method-request-validation.html) in the *API Gateway Developer Guide*.
func LookupRequestValidator(ctx *pulumi.Context, args *LookupRequestValidatorArgs, opts ...pulumi.InvokeOption) (*LookupRequestValidatorResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupRequestValidatorResult
	err := ctx.Invoke("aws-native:apigateway:getRequestValidator", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupRequestValidatorArgs struct {
	// ID of the request validator.
	RequestValidatorId string `pulumi:"requestValidatorId"`
	// The string identifier of the associated RestApi.
	RestApiId string `pulumi:"restApiId"`
}

type LookupRequestValidatorResult struct {
	// ID of the request validator.
	RequestValidatorId *string `pulumi:"requestValidatorId"`
	// A Boolean flag to indicate whether to validate a request body according to the configured Model schema.
	ValidateRequestBody *bool `pulumi:"validateRequestBody"`
	// A Boolean flag to indicate whether to validate request parameters (``true``) or not (``false``).
	ValidateRequestParameters *bool `pulumi:"validateRequestParameters"`
}

func LookupRequestValidatorOutput(ctx *pulumi.Context, args LookupRequestValidatorOutputArgs, opts ...pulumi.InvokeOption) LookupRequestValidatorResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupRequestValidatorResult, error) {
			args := v.(LookupRequestValidatorArgs)
			r, err := LookupRequestValidator(ctx, &args, opts...)
			var s LookupRequestValidatorResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupRequestValidatorResultOutput)
}

type LookupRequestValidatorOutputArgs struct {
	// ID of the request validator.
	RequestValidatorId pulumi.StringInput `pulumi:"requestValidatorId"`
	// The string identifier of the associated RestApi.
	RestApiId pulumi.StringInput `pulumi:"restApiId"`
}

func (LookupRequestValidatorOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRequestValidatorArgs)(nil)).Elem()
}

type LookupRequestValidatorResultOutput struct{ *pulumi.OutputState }

func (LookupRequestValidatorResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupRequestValidatorResult)(nil)).Elem()
}

func (o LookupRequestValidatorResultOutput) ToLookupRequestValidatorResultOutput() LookupRequestValidatorResultOutput {
	return o
}

func (o LookupRequestValidatorResultOutput) ToLookupRequestValidatorResultOutputWithContext(ctx context.Context) LookupRequestValidatorResultOutput {
	return o
}

func (o LookupRequestValidatorResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupRequestValidatorResult] {
	return pulumix.Output[LookupRequestValidatorResult]{
		OutputState: o.OutputState,
	}
}

// ID of the request validator.
func (o LookupRequestValidatorResultOutput) RequestValidatorId() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupRequestValidatorResult) *string { return v.RequestValidatorId }).(pulumi.StringPtrOutput)
}

// A Boolean flag to indicate whether to validate a request body according to the configured Model schema.
func (o LookupRequestValidatorResultOutput) ValidateRequestBody() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupRequestValidatorResult) *bool { return v.ValidateRequestBody }).(pulumi.BoolPtrOutput)
}

// A Boolean flag to indicate whether to validate request parameters (“true“) or not (“false“).
func (o LookupRequestValidatorResultOutput) ValidateRequestParameters() pulumi.BoolPtrOutput {
	return o.ApplyT(func(v LookupRequestValidatorResult) *bool { return v.ValidateRequestParameters }).(pulumi.BoolPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupRequestValidatorResultOutput{})
}
