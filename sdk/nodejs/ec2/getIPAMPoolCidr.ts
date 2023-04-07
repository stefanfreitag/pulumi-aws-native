// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as utilities from "../utilities";

/**
 * Resource Schema of AWS::EC2::IPAMPoolCidr Type
 */
export function getIPAMPoolCidr(args: GetIPAMPoolCidrArgs, opts?: pulumi.InvokeOptions): Promise<GetIPAMPoolCidrResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ec2:getIPAMPoolCidr", {
        "ipamPoolCidrId": args.ipamPoolCidrId,
        "ipamPoolId": args.ipamPoolId,
    }, opts);
}

export interface GetIPAMPoolCidrArgs {
    /**
     * Id of the IPAM Pool Cidr.
     */
    ipamPoolCidrId: string;
    /**
     * Id of the IPAM Pool.
     */
    ipamPoolId: string;
}

export interface GetIPAMPoolCidrResult {
    /**
     * Id of the IPAM Pool Cidr.
     */
    readonly ipamPoolCidrId?: string;
    /**
     * Provisioned state of the cidr.
     */
    readonly state?: string;
}
/**
 * Resource Schema of AWS::EC2::IPAMPoolCidr Type
 */
export function getIPAMPoolCidrOutput(args: GetIPAMPoolCidrOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetIPAMPoolCidrResult> {
    return pulumi.output(args).apply((a: any) => getIPAMPoolCidr(a, opts))
}

export interface GetIPAMPoolCidrOutputArgs {
    /**
     * Id of the IPAM Pool Cidr.
     */
    ipamPoolCidrId: pulumi.Input<string>;
    /**
     * Id of the IPAM Pool.
     */
    ipamPoolId: pulumi.Input<string>;
}
