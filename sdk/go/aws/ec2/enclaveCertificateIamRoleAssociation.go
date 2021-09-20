// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

package ec2

import (
	"context"
	"reflect"

	"github.com/pkg/errors"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

// Associates an AWS Identity and Access Management (IAM) role with an AWS Certificate Manager (ACM) certificate. This association is based on Amazon Resource Names and it enables the certificate to be used by the ACM for Nitro Enclaves application inside an enclave.
type EnclaveCertificateIamRoleAssociation struct {
	pulumi.CustomResourceState

	// The Amazon Resource Name (ARN) of the ACM certificate with which to associate the IAM role.
	CertificateArn pulumi.StringOutput `pulumi:"certificateArn"`
	// The name of the Amazon S3 bucket to which the certificate was uploaded.
	CertificateS3BucketName pulumi.StringOutput `pulumi:"certificateS3BucketName"`
	// The Amazon S3 object key where the certificate, certificate chain, and encrypted private key bundle are stored.
	CertificateS3ObjectKey pulumi.StringOutput `pulumi:"certificateS3ObjectKey"`
	// The ID of the AWS KMS CMK used to encrypt the private key of the certificate.
	EncryptionKmsKeyId pulumi.StringOutput `pulumi:"encryptionKmsKeyId"`
	// The Amazon Resource Name (ARN) of the IAM role to associate with the ACM certificate. You can associate up to 16 IAM roles with an ACM certificate.
	RoleArn pulumi.StringOutput `pulumi:"roleArn"`
}

// NewEnclaveCertificateIamRoleAssociation registers a new resource with the given unique name, arguments, and options.
func NewEnclaveCertificateIamRoleAssociation(ctx *pulumi.Context,
	name string, args *EnclaveCertificateIamRoleAssociationArgs, opts ...pulumi.ResourceOption) (*EnclaveCertificateIamRoleAssociation, error) {
	if args == nil {
		return nil, errors.New("missing one or more required arguments")
	}

	if args.CertificateArn == nil {
		return nil, errors.New("invalid value for required argument 'CertificateArn'")
	}
	if args.RoleArn == nil {
		return nil, errors.New("invalid value for required argument 'RoleArn'")
	}
	var resource EnclaveCertificateIamRoleAssociation
	err := ctx.RegisterResource("aws-native:ec2:EnclaveCertificateIamRoleAssociation", name, args, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// GetEnclaveCertificateIamRoleAssociation gets an existing EnclaveCertificateIamRoleAssociation resource's state with the given name, ID, and optional
// state properties that are used to uniquely qualify the lookup (nil if not required).
func GetEnclaveCertificateIamRoleAssociation(ctx *pulumi.Context,
	name string, id pulumi.IDInput, state *EnclaveCertificateIamRoleAssociationState, opts ...pulumi.ResourceOption) (*EnclaveCertificateIamRoleAssociation, error) {
	var resource EnclaveCertificateIamRoleAssociation
	err := ctx.ReadResource("aws-native:ec2:EnclaveCertificateIamRoleAssociation", name, id, state, &resource, opts...)
	if err != nil {
		return nil, err
	}
	return &resource, nil
}

// Input properties used for looking up and filtering EnclaveCertificateIamRoleAssociation resources.
type enclaveCertificateIamRoleAssociationState struct {
}

type EnclaveCertificateIamRoleAssociationState struct {
}

func (EnclaveCertificateIamRoleAssociationState) ElementType() reflect.Type {
	return reflect.TypeOf((*enclaveCertificateIamRoleAssociationState)(nil)).Elem()
}

type enclaveCertificateIamRoleAssociationArgs struct {
	// The Amazon Resource Name (ARN) of the ACM certificate with which to associate the IAM role.
	CertificateArn string `pulumi:"certificateArn"`
	// The Amazon Resource Name (ARN) of the IAM role to associate with the ACM certificate. You can associate up to 16 IAM roles with an ACM certificate.
	RoleArn string `pulumi:"roleArn"`
}

// The set of arguments for constructing a EnclaveCertificateIamRoleAssociation resource.
type EnclaveCertificateIamRoleAssociationArgs struct {
	// The Amazon Resource Name (ARN) of the ACM certificate with which to associate the IAM role.
	CertificateArn pulumi.StringInput
	// The Amazon Resource Name (ARN) of the IAM role to associate with the ACM certificate. You can associate up to 16 IAM roles with an ACM certificate.
	RoleArn pulumi.StringInput
}

func (EnclaveCertificateIamRoleAssociationArgs) ElementType() reflect.Type {
	return reflect.TypeOf((*enclaveCertificateIamRoleAssociationArgs)(nil)).Elem()
}

type EnclaveCertificateIamRoleAssociationInput interface {
	pulumi.Input

	ToEnclaveCertificateIamRoleAssociationOutput() EnclaveCertificateIamRoleAssociationOutput
	ToEnclaveCertificateIamRoleAssociationOutputWithContext(ctx context.Context) EnclaveCertificateIamRoleAssociationOutput
}

func (*EnclaveCertificateIamRoleAssociation) ElementType() reflect.Type {
	return reflect.TypeOf((*EnclaveCertificateIamRoleAssociation)(nil))
}

func (i *EnclaveCertificateIamRoleAssociation) ToEnclaveCertificateIamRoleAssociationOutput() EnclaveCertificateIamRoleAssociationOutput {
	return i.ToEnclaveCertificateIamRoleAssociationOutputWithContext(context.Background())
}

func (i *EnclaveCertificateIamRoleAssociation) ToEnclaveCertificateIamRoleAssociationOutputWithContext(ctx context.Context) EnclaveCertificateIamRoleAssociationOutput {
	return pulumi.ToOutputWithContext(ctx, i).(EnclaveCertificateIamRoleAssociationOutput)
}

type EnclaveCertificateIamRoleAssociationOutput struct{ *pulumi.OutputState }

func (EnclaveCertificateIamRoleAssociationOutput) ElementType() reflect.Type {
	return reflect.TypeOf((*EnclaveCertificateIamRoleAssociation)(nil))
}

func (o EnclaveCertificateIamRoleAssociationOutput) ToEnclaveCertificateIamRoleAssociationOutput() EnclaveCertificateIamRoleAssociationOutput {
	return o
}

func (o EnclaveCertificateIamRoleAssociationOutput) ToEnclaveCertificateIamRoleAssociationOutputWithContext(ctx context.Context) EnclaveCertificateIamRoleAssociationOutput {
	return o
}

func init() {
	pulumi.RegisterOutputType(EnclaveCertificateIamRoleAssociationOutput{})
}
