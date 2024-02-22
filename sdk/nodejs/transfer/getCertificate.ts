// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Type definition for AWS::Transfer::Certificate
 */
export function getCertificate(args: GetCertificateArgs, opts?: pulumi.InvokeOptions): Promise<GetCertificateResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:transfer:getCertificate", {
        "certificateId": args.certificateId,
    }, opts);
}

export interface GetCertificateArgs {
    /**
     * A unique identifier for the certificate.
     */
    certificateId: string;
}

export interface GetCertificateResult {
    /**
     * Specifies the active date for the certificate.
     */
    readonly activeDate?: string;
    /**
     * Specifies the unique Amazon Resource Name (ARN) for the agreement.
     */
    readonly arn?: string;
    /**
     * A unique identifier for the certificate.
     */
    readonly certificateId?: string;
    /**
     * A textual description for the certificate.
     */
    readonly description?: string;
    /**
     * Specifies the inactive date for the certificate.
     */
    readonly inactiveDate?: string;
    /**
     * Specifies the not after date for the certificate.
     */
    readonly notAfterDate?: string;
    /**
     * Specifies the not before date for the certificate.
     */
    readonly notBeforeDate?: string;
    /**
     * Specifies Certificate's serial.
     */
    readonly serial?: string;
    /**
     * A status description for the certificate.
     */
    readonly status?: enums.transfer.CertificateStatus;
    /**
     * Key-value pairs that can be used to group and search for certificates. Tags are metadata attached to certificates for any purpose.
     */
    readonly tags?: outputs.Tag[];
    /**
     * Describing the type of certificate. With or without a private key.
     */
    readonly type?: enums.transfer.CertificateType;
    /**
     * Specifies the usage type for the certificate.
     */
    readonly usage?: enums.transfer.CertificateUsage;
}
/**
 * Resource Type definition for AWS::Transfer::Certificate
 */
export function getCertificateOutput(args: GetCertificateOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetCertificateResult> {
    return pulumi.output(args).apply((a: any) => getCertificate(a, opts))
}

export interface GetCertificateOutputArgs {
    /**
     * A unique identifier for the certificate.
     */
    certificateId: pulumi.Input<string>;
}
