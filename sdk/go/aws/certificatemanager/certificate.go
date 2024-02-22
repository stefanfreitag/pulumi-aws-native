// Code generated by the Pulumi SDK Generator DO NOT EDIT.
// *** WARNING: Do not edit by hand unless you're certain you know what you are doing! ***

package certificatemanager

import (
	"context"
	"reflect"

	"errors"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws"
	"github.com/pulumi/pulumi-aws-native/sdk/go/aws/internal"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Resource Type definition for AWS::CertificateManager::Certificate
//
// Deprecated: Certificate is not yet supported by AWS Native, so its creation will currently fail. Please use the classic AWS provider, if possible.
type Certificate struct {
	pulumi.CustomResourceState

	CertificateAuthorityArn                  pulumi.StringPtrOutput                       `pulumi:"certificateAuthorityArn"`
	CertificateTransparencyLoggingPreference pulumi.StringPtrOutput                       `pulumi:"certificateTransparencyLoggingPreference"`
	DomainName                               pulumi.StringOutput                          `pulumi:"domainName"`
	DomainValidationOptions                  CertificateDomainValidationOptionArrayOutput `pulumi:"domainValidationOptions"`
	KeyAlgorithm                             pulumi.StringPtrOutput                       `pulumi:"keyAlgorithm"`
	SubjectAlternativeNames                  pulumi.StringArrayOutput                     `pulumi:"subjectAlternativeNames"`
	Tags                                     aws.TagArrayOutput                           `pulumi:"tags"`
	ValidationMethod                         pulumi.StringPtrOutput                       `pulumi:"validationMethod"`
}

// NewCertificate registers a new resource with the given unique name, arguments, and options.
func NewCertificate(ctx *pulumi.Context,
	name string, args *CertificateArgs, opts ...pulumi.ResourceOption) (*Certificate, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.DomainName == nil {
		return nil, errors.New("invalid value for required argument 'DomainName'")
	}
	replaceOnChanges := pulumi.ReplaceOnChanges([]string{
		"certificateAuthorityArn",
		"domainName",
		"domainValidationOptions[*]",
		"keyAlgorithm",
		"subjectAlternativeNames[*]",
		"validationMethod",
	})
	opts = append(opts, replaceOnChanges)
	opts = internal.PkgResourceDefaultOpts(opts)
	var resource Certificate
	err := ctx.RegisterResource("aws-native:certificatemanager:Certificate", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetCertificate gets an existing Certificate resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetCertificate(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *CertificateState, opts ...pulumi.ResourceOption) (*Certificate, error) {
	var resource Certificate
	err := ctx.ReadResource("aws-native:certificatemanager:Certificate", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering Certificate resources.
type certificateState struct {
}

type CertificateState struct {
}

func (CertificateState) ElementType() reflect.Type {
	return reflect.TypeOf((*certificateState)(nil)).Elem()
}

type certificateArgs struct {
	CertificateAuthorityArn                  *string                             `pulumi:"certificateAuthorityArn"`
	CertificateTransparencyLoggingPreference *string                             `pulumi:"certificateTransparencyLoggingPreference"`
	DomainName                               string                              `pulumi:"domainName"`
	DomainValidationOptions                  []CertificateDomainValidationOption `pulumi:"domainValidationOptions"`
	KeyAlgorithm                             *string                             `pulumi:"keyAlgorithm"`
	SubjectAlternativeNames                  []string                            `pulumi:"subjectAlternativeNames"`
	Tags                                     []aws.Tag                           `pulumi:"tags"`
	ValidationMethod                         *string                             `pulumi:"validationMethod"`
}

// The set of arguments for constructing a Certificate resource.
type CertificateArgs struct {
	CertificateAuthorityArn                  pulumi.StringPtrInput
	CertificateTransparencyLoggingPreference pulumi.StringPtrInput
	DomainName                               pulumi.StringInput
	DomainValidationOptions                  CertificateDomainValidationOptionArrayInput
	KeyAlgorithm                             pulumi.StringPtrInput
	SubjectAlternativeNames                  pulumi.StringArrayInput
	Tags                                     aws.TagArrayInput
	ValidationMethod                         pulumi.StringPtrInput
}

func (CertificateArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*certificateArgs)(nil)).Elem()
}

type CertificateInput interface {
	pulumi.Input

	ToCertificateOutput() CertificateOutput
	ToCertificateOutputWithContext(ctx context.Context) CertificateOutput
}

func (*Certificate) ElementType() reflect.Type {
	return reflect.TypeOf((**Certificate)(nil)).Elem()
}

func (i *Certificate) ToCertificateOutput() CertificateOutput {
	return i.ToCertificateOutputWithContext(context.Background())
}

func (i *Certificate) ToCertificateOutputWithContext(ctx context.Context) CertificateOutput {
	return pulumi.ToOutputWithContext(ctx, i).(CertificateOutput)
}

type CertificateOutput struct{ *pulumi.OutputState }

func (CertificateOutput) ElementType() reflect.Type {
	return reflect.TypeOf((**Certificate)(nil)).Elem()
}

func (o CertificateOutput) ToCertificateOutput() CertificateOutput {
	return o
}

func (o CertificateOutput) ToCertificateOutputWithContext(ctx context.Context) CertificateOutput {
	return o
}

func (o CertificateOutput) CertificateAuthorityArn() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Certificate) pulumi.StringPtrOutput { return v.CertificateAuthorityArn }).(pulumi.StringPtrOutput)
}

func (o CertificateOutput) CertificateTransparencyLoggingPreference() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Certificate) pulumi.StringPtrOutput { return v.CertificateTransparencyLoggingPreference }).(pulumi.StringPtrOutput)
}

func (o CertificateOutput) DomainName() pulumi.StringOutput {
	return o.ApplyT(func(v *Certificate) pulumi.StringOutput { return v.DomainName }).(pulumi.StringOutput)
}

func (o CertificateOutput) DomainValidationOptions() CertificateDomainValidationOptionArrayOutput {
	return o.ApplyT(func(v *Certificate) CertificateDomainValidationOptionArrayOutput { return v.DomainValidationOptions }).(CertificateDomainValidationOptionArrayOutput)
}

func (o CertificateOutput) KeyAlgorithm() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Certificate) pulumi.StringPtrOutput { return v.KeyAlgorithm }).(pulumi.StringPtrOutput)
}

func (o CertificateOutput) SubjectAlternativeNames() pulumi.StringArrayOutput {
	return o.ApplyT(func(v *Certificate) pulumi.StringArrayOutput { return v.SubjectAlternativeNames }).(pulumi.StringArrayOutput)
}

func (o CertificateOutput) Tags() aws.TagArrayOutput {
	return o.ApplyT(func(v *Certificate) aws.TagArrayOutput { return v.Tags }).(aws.TagArrayOutput)
}

func (o CertificateOutput) ValidationMethod() pulumi.StringPtrOutput {
	return o.ApplyT(func(v *Certificate) pulumi.StringPtrOutput { return v.ValidationMethod }).(pulumi.StringPtrOutput)
}

func init() {
	pulumi.RegisterInputType(reflect.TypeOf((*CertificateInput)(nil)).Elem(), &Certificate{})
	pulumi.RegisterOutputType(CertificateOutput{})
}
