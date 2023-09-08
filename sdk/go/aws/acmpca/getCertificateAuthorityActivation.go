// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package acmpca

import (
	"context"
	"reflect"

	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumix"
)

// Used to install the certificate authority certificate and update the certificate authority status.
func LookupCertificateAuthorityActivation(ctx *pulumi.Context, args *LookupCertificateAuthorityActivationArgs, opts ...pulumi.InvokeOption) (*LookupCertificateAuthorityActivationResult, error) {
	opts = internal.PkgInvokeDefaultOpts(opts)
	var rv LookupCertificateAuthorityActivationResult
	err := ctx.Invoke("aws-native:acmpca:getCertificateAuthorityActivation", args, &rv, opts...)
	if err != nil {
		return nil, err
	}
	return &rv, nil
}

type LookupCertificateAuthorityActivationArgs struct {
	// Arn of the Certificate Authority.
	CertificateAuthorityArn string `pulumi:"certificateAuthorityArn"`
}

type LookupCertificateAuthorityActivationResult struct {
	// The complete certificate chain, including the Certificate Authority certificate.
	CompleteCertificateChain *string `pulumi:"completeCertificateChain"`
	// The status of the Certificate Authority.
	Status *string `pulumi:"status"`
}

func LookupCertificateAuthorityActivationOutput(ctx *pulumi.Context, args LookupCertificateAuthorityActivationOutputArgs, opts ...pulumi.InvokeOption) LookupCertificateAuthorityActivationResultOutput {
	return pulumi.ToOutputWithContext(context.Background(), args).
		ApplyT(func(v interface{}) (LookupCertificateAuthorityActivationResult, error) {
			args := v.(LookupCertificateAuthorityActivationArgs)
			r, err := LookupCertificateAuthorityActivation(ctx, &args, opts...)
			var s LookupCertificateAuthorityActivationResult
			if r != nil {
				s = *r
			}
			return s, err
		}).(LookupCertificateAuthorityActivationResultOutput)
}

type LookupCertificateAuthorityActivationOutputArgs struct {
	// Arn of the Certificate Authority.
	CertificateAuthorityArn pulumi.StringInput `pulumi:"certificateAuthorityArn"`
}

func (LookupCertificateAuthorityActivationOutputArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCertificateAuthorityActivationArgs)(nil)).Elem()
}

type LookupCertificateAuthorityActivationResultOutput struct{ *pulumi.OutputState }

func (LookupCertificateAuthorityActivationResultOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*LookupCertificateAuthorityActivationResult)(nil)).Elem()
}

func (o LookupCertificateAuthorityActivationResultOutput) ToLookupCertificateAuthorityActivationResultOutput() LookupCertificateAuthorityActivationResultOutput {
	return o
}

func (o LookupCertificateAuthorityActivationResultOutput) ToLookupCertificateAuthorityActivationResultOutputWithContext(ctx context.Context) LookupCertificateAuthorityActivationResultOutput {
	return o
}

func (o LookupCertificateAuthorityActivationResultOutput) ToOutput(ctx context.Context) pulumix.Output[LookupCertificateAuthorityActivationResult] {
	return pulumix.Output[LookupCertificateAuthorityActivationResult]{
		OutputState: o.OutputState,
	}
}

// The complete certificate chain, including the Certificate Authority certificate.
func (o LookupCertificateAuthorityActivationResultOutput) CompleteCertificateChain() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCertificateAuthorityActivationResult) *string { return v.CompleteCertificateChain }).(pulumi.StringPtrOutput)
}

// The status of the Certificate Authority.
func (o LookupCertificateAuthorityActivationResultOutput) Status() pulumi.StringPtrOutput {
	return o.ApplyT(func(v LookupCertificateAuthorityActivationResult) *string { return v.Status }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterOutputType(LookupCertificateAuthorityActivationResultOutput{})
}
