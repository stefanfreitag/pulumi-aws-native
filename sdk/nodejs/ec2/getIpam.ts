// *** WARNING: this file was generated by the Pulumi SDK Generator. ***
// *** Do not edit by hand unless you're certain you know what you are doing! ***

import * as pulumi from "@pulumi/pulumi";
import * as inputs from "../types/input";
import * as outputs from "../types/output";
import * as enums from "../types/enums";
import * as utilities from "../utilities";

/**
 * Resource Schema of AWS::EC2::IPAM Type
 */
export function getIpam(args: GetIpamArgs, opts?: pulumi.InvokeOptions): Promise<GetIpamResult> {

    opts = pulumi.mergeOptions(utilities.resourceOptsDefaults(), opts || {});
    return pulumi.runtime.invoke("aws-native:ec2:getIpam", {
        "ipamId": args.ipamId,
    }, opts);
}

export interface GetIpamArgs {
    /**
     * Id of the IPAM.
     */
    ipamId: string;
}

export interface GetIpamResult {
    /**
     * The Amazon Resource Name (ARN) of the IPAM.
     */
    readonly arn?: string;
    /**
     * The Id of the default association to the default resource discovery, created with this IPAM.
     */
    readonly defaultResourceDiscoveryAssociationId?: string;
    /**
     * The Id of the default resource discovery, created with this IPAM.
     */
    readonly defaultResourceDiscoveryId?: string;
    readonly description?: string;
    /**
     * Id of the IPAM.
     */
    readonly ipamId?: string;
    /**
     * The regions IPAM is enabled for. Allows pools to be created in these regions, as well as enabling monitoring
     */
    readonly operatingRegions?: outputs.ec2.IpamOperatingRegion[];
    /**
     * The Id of the default scope for publicly routable IP space, created with this IPAM.
     */
    readonly privateDefaultScopeId?: string;
    /**
     * The Id of the default scope for publicly routable IP space, created with this IPAM.
     */
    readonly publicDefaultScopeId?: string;
    /**
     * The count of resource discoveries associated with this IPAM.
     */
    readonly resourceDiscoveryAssociationCount?: number;
    /**
     * The number of scopes that currently exist in this IPAM.
     */
    readonly scopeCount?: number;
    /**
     * An array of key-value pairs to apply to this resource.
     */
    readonly tags?: outputs.ec2.IpamTag[];
    /**
     * The tier of the IPAM.
     */
    readonly tier?: enums.ec2.IpamTier;
}
/**
 * Resource Schema of AWS::EC2::IPAM Type
 */
export function getIpamOutput(args: GetIpamOutputArgs, opts?: pulumi.InvokeOptions): pulumi.Output<GetIpamResult> {
    return pulumi.output(args).apply((a: any) => getIpam(a, opts))
}

export interface GetIpamOutputArgs {
    /**
     * Id of the IPAM.
     */
    ipamId: pulumi.Input<string>;
}
